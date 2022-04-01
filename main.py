import cv2
import numpy as np
import time
import playsound

Fire_Reporter = 0
Alarm_Status = False

def play():
    playsound.playsound('Alarm_Sound.mp3', True)

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = video.read()
    blur = cv2.GaussianBlur(frame, (15,15),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18,50,50]
    upper = [35,255,255]

    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv2.inRange(hsv,lower,upper)

    output = cv2.bitwise_and(frame,hsv,mask=mask)

    size = cv2.countNonZero(mask)

    if int(size) > 15000:
        Fire_Reporter = Fire_Reporter + 1
        print("Fire Detected")

        if Fire_Reporter >=1:
            if Alarm_Status == False:
                play()
                # Alarm_Status = F
                time.sleep(3)
                continue

    if ret == False:
        break

    cv2.imshow("Fire Detector", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
video.release()