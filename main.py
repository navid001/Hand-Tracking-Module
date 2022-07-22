import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_draw=mp.solutions.drawing_utils

current_time=0
previous_time=0

while True:
    success,img=cap.read()
    image_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for index,landmark in enumerate(landmarks.landmark):
                height,width,channel=img.shape
                x_axis=int(landmark.x*width)+10
                y_axis=int(landmark.y*height)+10
                cv2.putText(img, str(index), (int(x_axis), int(y_axis)), cv2.FLOODFILL_MASK_ONLY, 0.5, (0, 255, 0),2)
                if index==12:
                    cv2.circle(img,(int(x_axis-10), int(y_axis-10)),10,(255,255,255),cv2.FILLED)
            mp_draw.draw_landmarks(img,landmarks,mp_hands.HAND_CONNECTIONS)

    current_time=time.time()
    fps=1/(current_time-previous_time)
    previous_time=current_time

    cv2.putText(img,str(round(fps)),(30,80),cv2.FLOODFILL_MASK_ONLY,1,(0,255,0),2)

    cv2.imshow("Image Recognizing",img)
    cv2.waitKey(1)
