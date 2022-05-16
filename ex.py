import pytesseract              #문자인식
import pyautogui                #스크린샷
import PIL.Image           #이미지 불러오기
import schedule                 #일정한주기마다 실행
import time                     #시간


def Search():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    tess=pytesseract.image_to_string(PIL.Image.open('rudQN.jpg'), lang='kor+eng')
    print(tess)

schedule.every(5).seconds.do(Search)
while True:
    schedule.run_pending()
    time.sleep(1)