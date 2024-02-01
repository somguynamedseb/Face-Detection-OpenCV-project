import serial

from time import sleep

serial1 = serial.Serial('COM11', 9600)
# import required module
import os
from ultralytics import YOLO
from PIL import Image
import cv2 as cv
import time

deadzone = 10


model = YOLO("train3/weights/last.pt")

print("model loaded")
filename = 'example unknowns/104712738-Accounting_101.jpg'
vid = cv.VideoCapture(1)
print("cam loaded") 
ret, frame = vid.read() 
wid = frame.shape[1] 
hgt = frame.shape[0] 

center_x = wid/2
center_y = hgt/2
while(True): 
    # Capture the video frame 
    # by frame
    ret, frame = vid.read() 
    results = model.predict(source=frame)  # save plotted images
    result = results[0]
    UD = ""
    LR = ""
    UDpercent = 0
    LRpercent = 0
    output = "{}{}{}{}"
    try:
        box = result.boxes[0]
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
    #     print("Object type:", class_id)
    #     print("Coordinates:", cords)
    #     print("Probability:", conf)
    #     print("---")
        cv.rectangle(frame, (cords[0], cords[1]), (cords[2], cords[3]), (0, 255, 0), 2)
        x_head = (cords[0] + cords[2]) / 2
        y_head = (cords[1] + cords[3]) / 2
        
        if center_y > y_head:
            UD = "u"
            UDpercent = int(((abs(center_y - y_head) / center_y)*100)-1)
            if UDpercent<5:
                UDpercent = "00"
        elif center_y < y_head:
            UD = "d"
            UDpercent = int(((abs(center_y - y_head) / center_y)*100)-1)
            if UDpercent<5:
                UDpercent = "00"
        else:
            UD = "N"
            UDpercent = "00"
        if center_x > x_head:
            LR = "l"
            LRpercent = int(((abs(center_x - x_head) / center_x)*100)-1)
            if LRpercent<deadzone:
                LRpercent = "00"
        elif center_x < x_head:
            LR = "r"
            LRpercent = int(((abs(center_x - x_head) / center_x)*100)-1)
            if LRpercent<deadzone:
                LRpercent = "00"
        else:
            LR = "N"
            LRpercent = "00"
                
    except:
        UD = "N"
        LR = "N"
        UDpercent = "00"
        LRpercent = "00"
    
    # print(output.format(UD, UDpercent, LR, LRpercent))
    encoded_output = (output.format(UD, UDpercent, LR, LRpercent)).encode()
    serial1.write(encoded_output)
    # print(encoded_output)
    # data = serial1.readline()
    # print(data)
    # print(UD+str(UDpercent)+LR+str(LRpercent))
    sleep(0.5)