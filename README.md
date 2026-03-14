//라인트레이서용 적외선 센서
//검은색 테이프 감지=1/흰색 감지=0
#define READ_LEFT_SENSOR() ((PINA & (1<<LEFT_SENSOR)) ? 1 : 0)
#define READ_RIGHT_SENSOR() ((PINA & (1<<RIGHT_SENSOR)) ? 1 : 0)

//적외선 센서의 감지거리가 짧은 것을 이용하여 짐 확인
//짐칸에 짐이 없음=1/짐칸에 짐이 있음=0(혼동 주의)
#define READ_101_SENSOR() ((PINF & (1<<cargo101)) ? 1 : 0)
#define READ_102_SENSOR() ((PINF & (1<<cargo102)) ? 1 : 0)
#define READ_201_SENSOR() ((PINF & (1<<cargo201)) ? 1 : 0)
#define READ_202_SENSOR() ((PINF & (1<<cargo202)) ? 1 : 0)

void servo_init(void)//서보모터는 내부 회로가 20ms 주기로 들어오는 펄스 폭을 읽도록 설계되어 있음
{
  // Timer 4(PH3,PH4, PH5), Fast PWM 50Hz (20ms 주기를 가진 펄스 생성)
  DDRH |= (1<<PH3) | (1<<PH4) | (1<<PH5);
  TCCR4A = (1<<COM4A1) | (1<<COM4B1) | (1<<COM4C1) | (1<<WGM41);
  TCCR4B = (1<<WGM43) | (1<<WGM42) | (1<<CS41);
  ICR4 = 40000; // 20ms PWM

  // Timer5 (PL3), Fast PWM 50Hz (20ms 주기를 가진 펄스 생성)
  DDRL |= (1<<PL3); // OC5A 출력
  TCCR5A |= (1<<COM5A1) | (1<<WGM51);
  TCCR5B |= (1<<WGM53) | (1<<WGM52) | (1<<CS51);
  ICR5 = 40000;
}

void set_servo(uint16_t ch1, uint16_t ch2, uint16_t ch3, uint16_t ch4)
{
  OCR4A = ch1 * 2; // PH3 (OC4A)
  OCR4B = ch2 * 2; // PH4 (OC4B)
  OCR4C = ch3 * 2; // PH5 (OC4C)
  OCR5A = ch4 * 2; // PL3 (OC5A)
}



// 0~255 범위로 각 바퀴 속도를 조절하도록 초기화 함수에서 설정하였음 (생략)
void setMotorSpeed(uint8_t fl, uint8_t fr, uint8_t bl, uint8_t br)
{
  OCR3B = fl; // 앞바퀴 왼쪽
  OCR3C = fr; // 앞바퀴 오른쪽

  OCR1A = bl; // 뒷바퀴 왼쪽
  OCR1B = br; // 뒷바퀴 오른쪽
}

int getDistanceCM(void)
{
  //이전 HIGHtrig신호의 잔상을 지우기 위해 2us간 LOW설정
  PORTE &= ~(1<<TRIG_PIN);
  _delay_us(2);

  // 거리 측정 (재)시작을 알림
  PORTE |= (1<<TRIG_PIN);
  _delay_us(10);
  PORTE &= ~(1<<TRIG_PIN);

  uint32_t timeout = 0;

  // echo가HIGH 될 때까지 대기 
  while(!(PINE & (1<<ECHO_PIN)))
  {
    // 20ms 동안 echo 상승이 없으면 오류
    if(timeout++ > 20000) return -1; 
    _delay_us(1);
  }

  // HIGH 펄스 길이 측정
  uint32_t count = 0;
  while(PINE & (1<<ECHO_PIN))
  {
    count++;
    _delay_us(1);
    if(count > 30000) break; // 최대 측정량(약 5m)
  }

  // count가 너무 크면 잘못된 값임을 알림
  if(count == 0 || count > 30000) return -1;

  // 거리 계산
  int distance = count / 58;
  return distance;
}

void lineTracer(void)
{
  while(1)//정지선을 만나기 전까지 무한 동작
  {
    uint8_t left = READ_LEFT_SENSOR();
    uint8_t right = READ_RIGHT_SENSOR();

    //장애물과의 거리 측정,20cm이하인 경우 정지 및 부저 울림
    int distance = getDistanceCM();
    if(distance > 0 && distance < 20)
    {
      setMotorSpeed(0,0,0,0);
      PORTD |= (1 << BUZZER);
    }
    else//장애물이 없는 경우 부저 off및 라인트레이서 동작
    {
      PORTD &= ~(1 << BUZZER);

      //좌,우 적외선 센서가 검은색 테이프를 감지하지 않을 경우
      if(!left && !right)
      setMotorSpeed(255,255,255,255);//직진


      //좌측 적외선 센서만 검은색 테이프 감지
      else if(left && !right)
      setMotorSpeed(0,255,0,255);//좌회전

      //우측 적외선 센서만 검은색 테이프 감지
      else if(!left && right)
      setMotorSpeed(255,0,255,0);

      //두 적외선 센서 모두 검은색 테이프 감지
      else if(left && right)
      {
        setMotorSpeed(0,0,0,0);//정지 및 라인트레이서 동작 루프 벗어남
        break;
      }
    }
    _delay_ms(100);
  }
}

int main(void)
{
  //초기화
  servo_init();
  io_init();
  setMotorDirection();

  //서보모터 각도 초기화 (모터 위치에 따라 세밀 조정하였음)
  set_servo(2100, 1100, 1150, 2000);
  _delay_ms(5000);

  while(1)
  {
    //각 짐칸의 유무를 확인하여 배열에 저장
    uint16_t box[4] = {
      READ_101_SENSOR(),
      READ_102_SENSOR(),
      READ_201_SENSOR(),
      READ_202_SENSOR()
      };

    if (!box[0] && !box[1]) // (예시)101호,102호 짐칸에 짐이 있는 경우
    {
      lineTracer();

      set_servo(1500, 1100, 1150, 2000);
      _delay_ms(2000);
      PORTD |= (1 << IN2);
      PORTD &= ~(1 << IN1);
      _delay_ms(10000);
      PORTD &= ~((1 << IN1) | (1 << IN2));
      _delay_ms(2000);

      set_servo(2100, 1600, 1150, 2000);
      _delay_ms(2000);
      PORTD |= (1 << IN1);
      PORTD &= ~(1 << IN2);
      _delay_ms(10000);
      PORTD &= ~((1 << IN1) | (1 << IN2));
      _delay_ms(2000);

      set_servo(2100, 1100, 1150, 2000);
      _delay_ms(2000);

      setMotorSpeed(255,255,255,255);
      _delay_ms(600);

      lineTracer();
}
