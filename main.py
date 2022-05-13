import tkinter
from turtle import bgcolor, left, right
from PIL import Image   #이미지 불러오기
from tkinter import*    #GUI
import pytesseract      #문자인식
import cv2
import numpy as np


#화면 생성
tk=Tk() 
tk.title("경뿌 알리미")   #제목
tk.geometry("640x400")  #창크기
tk.resizable(True,True) #창크기조절 true

#클릭했을시
def clicked():
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

label = Label(tk,text='경뿌 채팅창')

#fg 글자색 bg 배경색
btn1 = Button(tk, text="경뿌 찾기",bg='yellow',command=clicked,width=20)
# btn2 = Button(tk, text='끄기,초기화')

btn1.pack(side= BOTTOM,padx=20,pady=20)  #padx 좌우여백  pady 상하여백
# btn2.pack(side= RIGHT,padx=20,pady=20)



# #텍스트 표시
# label = Label()

#레이블 배치 실행 (label자동정렬)
# label.pack()

#메인루프실행
tk.mainloop()



# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# f=open('rud.txt','w')

# f.write(pytesseract.image_to_string(Image.open('rudQN.jpg'), lang='kor+eng'))