from sre_parse import State
from numpy import complexfloating
from pynput import mouse        #윈도우 전체화면을 이용해 마우스좌표
import PIL.Image           #이미지 불러오기
from tkinter import*            #GUI
from pyparsing import col       #GUI
import pytesseract              #문자인식
import pyautogui                #스크린샷
import threading                #쓰레드
import winsound as sd           #알림음
import re
#버튼1 경뿌찾는중 클릭했을시


def clicked1():

        Search()    #쓰레드시작

    
 
#버튼2 즉 좌표값생성버튼 클릭
def clicked2():
    CoorList.clear()    #좌표값 초기화
    for i in range(2):
        with mouse.Listener(on_click=MouseClick) as listener:
            listener.join()

def clicked3():
    print('멈춰')

#마우스 버튼 2  클릭시
def MouseClick(x,y,button,pressed):
    if pressed:
        global x1
        global y1
        x1=x
        y1=y
    if not pressed :
        return False
    CorSave(x1,y1)

# 좌표값저장
def CorSave(x,y):
    x1=x
    y1=y
    CoorList.append([x,y])
    print(CoorList)
    if(len(CoorList)==2):
        CorCal()
#좌표 계산
def CorCal():
    w=int(CoorList[0][0])
    x=int(CoorList[0][1])
    y=int(CoorList[1][0])
    z=int(CoorList[1][1])
    leng=z-x    #세로
    wid=y-w     #가로
    print(wid,leng)

    ScreenShot(wid,leng,w,x)      #좌표값 보내서 스크린샷찍

#스크린샷
def ScreenShot(wid,leng,w,x):
    img=pyautogui.screenshot('rudQN.jpg',region=(w,x,wid,leng))
# #현재 화면 해상도 인식  #좌표지정을 위한
# pyautogui.size()
    

#문자인식용 쓰레드
def Search():
    CorCal()
    tess=pytesseract.image_to_string(PIL.Image.open('rudQN.jpg'), lang='kor+eng')
    tess_1=re.split('\n',tess)
    lev=0
    for x in tess_1:

        if('뿌'or'MVP'or'경뿌'or'마빌'or'채'or'ㄱㅃ'or'ㅁㅂ' in x):
            # print('경있음')
            # beepsound()
            lev=1
            print(tess_1)

        #쓰레드시작

    t=threading.Timer(5,clicked1)
    t.daemon=True
    t.start()
    if(lev==1):
        beepsound()


def beepsound():
    fr = 300    # range : 37 ~ 32767
    du = 500     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

#main
#화면 생성
tk=Tk() 
tk.title("경뿌 알리미")   #제목
tk.geometry("640x400")  #창크기
tk.resizable(True,True) #창크기조절 true

#좌표 저장 리스트
CoorList=[]

label = Label(tk,text='경뿌 채팅창')

#fg 글자색 bg 배경색
btn1 = Button(tk, text="경뿌 찾기",bg='yellow',command=clicked1,width=20)
btn2 = Button(tk, text='채팅창 꼭짓점 좌표 4개 누르기',command=clicked2,width=40)
btn3= Button(tk,text='멈춰',command=clicked3,width=20)


btn1.grid(row=0,column=1,padx=20,pady=20)  #padx 좌우여백  pady 상하여백
btn2.grid(row=0,column=2,padx=20,pady=20)  #place 절대좌표 pack 상대위치 grid 액자형
btn3.grid(row=0,column=4,padx=20,pady=20)
#tesseract 문자인식

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'




#메인루프실행
tk.mainloop()







