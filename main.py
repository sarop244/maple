from logging.config import listen
from pynput import mouse # 윈도우 전체화면을 이용해 마우스좌표
from PIL import Image   #이미지 불러오기
from tkinter import*
from matplotlib.backend_bases import MouseEvent
from pyparsing import col    #GUI
import pytesseract      #문자인식
# import pyautogui


# #현재 화면 해상도 인식  #좌표지정을 위한
# pyautogui.size()

#화면 생성
tk=Tk() 
tk.title("경뿌 알리미")   #제목
tk.geometry("640x400")  #창크기
tk.resizable(True,True) #창크기조절 true

#좌표 저장 리스트
CoorList=[]

#클릭했을시
def clicked1():
    if btn1['text'] == '경뿌 찾기':
        btn1['text'] ='경뿌 찾는중'
        btn1['bg'] = 'green'
        btn1['fg'] = 'white'

        # label=Label()
        # for 
    else:
        btn1['text'] = '경뿌 찾기'
        btn1['bg'] = 'yellow'
        btn1['fg'] = 'black'

#마우스 클릭
def MouseClick(x,y,button,pressed):
    if pressed:
        global x1
        global y1
        x1=x
        y1=y
    if not pressed :
        return False
    CorSave(x1,y1)

#버튼2 즉 좌표값생성버튼 클릭
def clicked2():
    CoorList.clear()    #좌표값 초기화
    for i in range(4):
        with mouse.Listener(on_click=MouseClick) as listener:
            listener.join()

# 좌표값저장
def CorSave(x,y):
    x1=x
    y1=y
    CoorList.append([x,y])
    print(CoorList)

label = Label(tk,text='경뿌 채팅창')

#fg 글자색 bg 배경색
btn1 = Button(tk, text="경뿌 찾기",bg='yellow',command=clicked1,width=20)
btn2 = Button(tk, text='채팅창 꼭짓점 좌표 4개 누르기',command=clicked2,width=40)

btn1.grid(row=0,column=1,padx=20,pady=20)  #padx 좌우여백  pady 상하여백
btn2.grid(row=0,column=2,padx=20,pady=20)  #place 절대좌표 pack 상대위치 grid 액자형

#메인루프실행
tk.mainloop()



# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# f=open('rud.txt','w')

# f.write(pytesseract.image_to_string(Image.open('rudQN.jpg'), lang='kor+eng'))






