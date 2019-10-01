# Spy on your friends while they are using your phone with Python and OpenCV

# IP Camera tutorial - http://www.skipser.com/p/2/p/android-as-webcam.html
# OpenCV-Python docs - https://opencv-python-tutroals.readthedocs.io/
# https://github.com/paakways/spycam - October 2019

import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()  
stream_url = simpledialog.askstring(title="IP Camera URL", prompt="Enter stream URL:")
count = 0


stream = cv2.VideoCapture(stream_url)  

while True:
    ret, frame = stream.read()

    #cv2.rectangle(frame,(0,0),(478,60),(0,255,0),1)
    text = 'sPycam'
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    if count % 20 == 0: cv2.circle(frame,(30,35),10,(0,0,255), -1)
    cv2.putText(frame, text, (45,40),font,1,(255,255,255),2)
    count += 1
    
    try:
        cv2.imshow('sPycam', frame)
    except:
        messagebox.showwarning(title="IP Camera URL", message="Could not open stream URL")
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
