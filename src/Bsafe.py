# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import winsound as ad
from tkinter import *

#비프음 함수 생성
def beepsound():
    fr = 2000
    du = 500
    ad.Beep(fr, du)

#버튼 이벤트
def click():
    print("\n[Web발신]\n119에서 긴급구조를 위해 귀하의\n휴대전화 위치를 조회하였습니다.\n")
    print("[Web발신]\n1시 01분에\n119안전센터 차량이 (상도동)으로\n출동하였습니다.\n")

#버튼
w = Tk()
w.geometry("400x400")
w.title("PhotoButton")

photo = PhotoImage(file="button.png")
btn = Button(w, image=photo, command=click)
btn.pack(expand=1, anchor=CENTER)

#사진 출력
img1=cv2.imread("danger.png", cv2.IMREAD_UNCHANGED)
img2=cv2.imread("safe.png", cv2.IMREAD_UNCHANGED) 

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(1)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    if not status:
        break

    # apply object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Bsafe", out)
    if any(str in 'person' for str in label):
        #beepsound() 
        cv2.imshow("condition", img1)
        w.mainloop()

    else:
        cv2.imshow("condition", img2)
 
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows() 