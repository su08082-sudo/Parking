import time
import random
from pymodbus.client import ModbusTcpClient


def test_parking_display():
    """주차유도판 테스트 - 5초마다 랜덤 값 전송"""

    # Modbus TCP 클라이언트 연결
    client = ModbusTcpClient('127.0.0.1', port=502)

    if not client.connect():
        print("서버 연결 실패! 주차유도판 프로그램이 실행 중인지 확인하세요.")
        return

    print("Modbus TCP 서버에 연결되었습니다.")
    print("5초마다 랜덤 값을 전송합니다. (Ctrl+C로 종료)\n")

    try:
        count = 0
        while True:
            count += 1

            # 랜덤 값 생성
            # 90% 확률로 1~200 사이 숫자
            # 10% 확률로 0 (만차)

            left_value = random.choices(
                [random.randint(1, 200), 0],
                weights=[90, 10]
            )[0]

            right_value = random.choices(
                [random.randint(1, 200), 0],
                weights=[90, 10]
            )[0]

            # 레지스터에 값 쓰기 (한번에 2개)
            result = client.write_registers(0, [left_value, right_value])

            # 결과 출력
            left_display = "만차" if left_value in [0, 65535] else left_value
            right_display = "만차" if right_value in [0, 65535] else right_value

            print(f"[{count}] 좌측: {left_display:>4} | 우측: {right_display:>4}")

            # 5초 대기
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n\n테스트를 종료합니다.")
    finally:
        client.close()
        print("연결을 종료했습니다.")


if __name__ == "__main__":
    test_parking_display()