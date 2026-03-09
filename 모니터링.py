import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import json
import time
import threading

POS_JSON = 'monitoring.json'

HR_AVAIL_FLOOR = 50
HR_AVAIL_GUIDE = 0

 #창 크기
W, H = 1024, 768
LABEL_SIZE =N_FLOORS = 0
TEXT_COLOR ='black'#글자색 고정
20_TEXT SIZE = 6 #글자 크기
 
updated False
global updated
while True:
     time.sleep(1)
     updated True
     
def update_labels () :
     if not updated:
         return
     for f in range (1, N FLOORS+1):
         a= [random.randint (0, 100), random.randint (0,100)
         status_labels [str(f)].config (text=f'{pos ['names'] [str (f)]: <5}:
        (a[0]:53)/(a[1]:>3}')
 #각 캔버스에 사각형 + 텍스트 표시
def draw_active():
     global updated
     current_tab= notebook.index ('current')
     canvas canvases [current_tab]
     canvas.delete('all')
     
     # 배경 이미지 다시 그리기
     canvas.create_image (0, 0, image=bg_photo [current_tab+1], anchor='nw')
 
     tab_name = f'(current_tab+1}'
     if tab name in pos:
     for item in pos [tab_name]:
         x= item['x']
         y = item['y']
        id=item['id']
        text=id
        lcu_id =int(id[0])
        sensor_id= int(id [2:]) - 1 idx= sensor id // 16
        mask=1<<(sensor_id % 16)
        
        bg'darkgray'
        if updated:
            bg random.choice (['lightblue', 'lightgreen', 'lightcoral'])
       fg = TEXT_COLOR
       half = LABEL SIZE // 2
       canvas.create_rectangle (x-half, y-half, x+half, y+half, fill=bg, outline='black', width=2)
       canvas.create_text (x, y, text=text, fill=fg, font = ('Arial', TEXT_SIZE,
'bold'))
#우측 하단에 최종 업데이트 시간 표시
timestamp = datetime.now().strftime ('%H:%M:%S')
canvas.create_text (W-60, H-80, text-f'Updated: [timestamp)', fill='black',
                    
SyntaxError: unexpected indent
import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import json
import time
import threading

POS JSON = 'monitoring.json'

HR AVAIL FLOOR = 50
HR AVAIL GUIDE = 0

#창 크기
W, H 1024, 768
LABEL SIZE =
N FLOORS = 0
TEXT COLOR ='black'#글자색 고정
20 TEXT SIZE = 6 #글자 크기

updated False
global updated
while True:
    time.sleep(1)
    updated True

def update_labels () :
    if not updated:
        return
    for f in range (1, N FLOORS+1):
        a= [random.randint (0, 100), random.randint (0,100)
        status_labels [str(f)].config (text=f'(pos ['names'] [str (f)]: <5}:
       (a[0]:53)/(a[1]:>3}')
#각 캔버스에 사각형 + 텍스트 표시
def draw_active():
    global updated
    current_tab= notebook.index ('current')
    canvas canvases [current_tab]
    canvas.delete('all')

    # 배경 이미지 다시 그리기
    canvas.create_image (0, 0, image=bg_photo [current_tab+1], anchor='nw')

    tab_name = f'(current_tab+1}'
    if tab name in pos:
    for item in pos [tab_name]:
        x= item['x']
        y = item['y']
       id=item['id']
       text=id
       lcu_id =int(id[0])
       sensor_id= int(id [2:]) - 1 idx= sensor id // 16
       mask=1<<(sensor_id % 16)

       bg'darkgray'
       if updated:
           bg random.choice (['lightblue', 'lightgreen', 'lightcoral'])
      fg = TEXT_COLOR
      half = LABEL SIZE // 2
      canvas.create_rectangle (x-half, y-half, x+half, y+half, fill=bg, outline='black', width=2)
      canvas.create_text (x, y, text=text, fill=fg, font = ('Arial', TEXT_SIZE,
'bold'))
#우측 하단에 최종 업데이트 시간 표시
timestamp = datetime.now().strftime ('%H:%M:%S')
canvas.create_text (W-60, H-80, text-f'Updated: [timestamp)', fill='black',
                    
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statementimport random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import json
import time
import threading

POS JSON = 'monitoring.json'

HR AVAIL FLOOR = 50
HR AVAIL GUIDE = 0

#창 크기
W, H 1024, 768
LABEL SIZE =
N FLOORS = 0
TEXT COLOR ='black'#글자색 고정
20 TEXT SIZE = 6 #글자 크기

updated False
global updated
while True:
    time.sleep(1)
    updated True

def update_labels () :
    if not updated:
        return
    for f in range (1, N FLOORS+1):
        a= [random.randint (0, 100), random.randint (0,100)
        status_labels [str(f)].config (text=f'(pos ['names'] [str (f)]: <5}:
       (a[0]:53)/(a[1]:>3}')
#각 캔버스에 사각형 + 텍스트 표시
def draw_active():
    global updated
    current_tab= notebook.index ('current')
    canvas canvases [current_tab]
    canvas.delete('all')

    # 배경 이미지 다시 그리기
    canvas.create_image (0, 0, image=bg_photo [current_tab+1], anchor='nw')

    tab_name = f'(current_tab+1}'
    if tab name in pos:
    for item in pos [tab_name]:
        x= item['x']
        y = item['y']
       id=item['id']
       text=id
       lcu_id =int(id[0])
       sensor_id= int(id [2:]) - 1 idx= sensor id // 16
       mask=1<<(sensor_id % 16)

       bg'darkgray'
       if updated:
           bg random.choice (['lightblue', 'lightgreen', 'lightcoral'])
      fg = TEXT_COLOR
      half = LABEL SIZE // 2
      canvas.create_rectangle (x-half, y-half, x+half, y+half, fill=bg, outline='black', width=2)
...       canvas.create_text (x, y, text=text, fill=fg,font = ('Arial', TEXT_SIZE,'bold'))
...  #우측 하단에 최종 업데이트 시간 표시
...      timestamp = datetime.now().strftime ('%H:%M:%S')
...      canvas.create_text (W-60, H-80, text-f'Updated: [timestamp)', fill='black'
...      font= ('Arial', 8))
...      update_labels ()
...      updated = False
...      root.after (1000, draw_active)
...  if_name_=='__main__':
...     root tk. Tk ()
...     root.tiltle('주차유도 시스템 모니터링)
...     root.geometry (f' (W)x{H}')
... #JSON 파일 로드
...    try:
...        with open (POS_JSON, 'r', encoding='utf-8') as f:
...            pos json.load(f)
...            COM_PORT = pos.get('port', 'COM3')
...            BAUD_RATE= pos.get('baud rate',19200)
...   except FileNotFoundError:
...        pos = {}
...  for i in range (1,9):
...      if not str(i) in pos:
...          break
...      N_FLOORS = i
...  if N_FLOORS == 0:
...      messagebox.showerror('오류', '층 데이터가 필요합니다.')
...      exit ()
...  top_frame = tk. Frame (root, bg='#ddd', height=40)
...  top_frame.pack (fill='x')
...  
...  status_labels = {}
...  for i in range (N FLOORS):
...      f=i+1
...      lbl= tk. Label (
...        top_frame,
...        text='',
...        font= ('Arial', 10, 'bold'),
...        width=14,
...        relief='groove',
...        bd=1
...     )
...     lbl.pack (side='left', padx=5, pady=5)
...     status_labels [str (f)] = lbl
...  # Notebook (E)
...  notebook ttk. Notebook (root)
...  notebook.pack (fill='both', expand=True)
...  bg_photo={}
...  # 이미지 로드 (배경용)
...  for i in range (N_FLOORS):
...      f=i+1
...      bg_image = Image.open('img/'+pos['imgs'] [str(f)])
...      bg image bg image.resize((W, H-60))
...      bg_photo [f] = ImageTk. Photo Image (bg_image)
...  tabs = []
...  canvases = []
...  for i in range (N_FLOORS):
...      tab= tk.Frame (notebook)
...      notebook.add(tab, text=pos ['names'] [str(i + 1)])
...      canvas = tk. Canvas (tab, width=W, height=H-60, bg='white')
...      canvas.pack (fill='both', expand=True)
...      canvas.create_image (0, 0, image=bg_photo [i+1], anchor='nw')
...      tabs.append(tab)
...      canvases.append(canvas)
...  t = threading. Thread (target=ccu_worker, daemon=True)
...  t.start()
...  
...  draw_active()
