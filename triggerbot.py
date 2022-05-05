import torch
import pyautogui
import time
import keyboard
from playsound import playsound

from torch._C import TensorType

model = torch.hub.load('ultralytics/yolov5', 'yolov5s6')
model.classes = [0]

while True:

    # quit
    if keyboard.is_pressed('q'):
        break
    
    # triggerbot key is pressed
    while keyboard.is_pressed('shift'):
        pyautogui.screenshot('screenshot.jpg')
        img = pyautogui.screenshot(region=(860, 445 , 200, 200))
        results = model(img)

        df = results.pandas().xyxy[0]
        
        # loop through each detection
        for i in range(len(df.index)):
            if df.iloc[i]['xmin'] <= 100 and df.iloc[i]['xmax'] >= 100 and df.iloc[i]['ymin'] <= 100 and df.iloc[i]['ymax'] >= 100:
                pyautogui.click()
                print("BANG!\n")
                #playsound('hitsound.wav')
