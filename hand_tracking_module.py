import cv2
import mediapipe as mp
import time

class hand_detector:

    def __init__(self,mode=False,max_hands=2,model_complexity=1,detection_confidence=0.5,track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.model_complexity=model_complexity
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,self.max_hands,self.model_complexity,self.detection_confidence,self.track_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def hand_tracker(self,img,draw=True):
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)

        if self.results.multi_hand_landmarks:
            for landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self,img,hand_number=0,draw=True):

        landmark_list=[]
        if self.results.multi_hand_landmarks:

            using_hand=self.results.multi_hand_landmarks[hand_number]
            for index, landmark in enumerate(using_hand.landmark):
                height, width, channel = img.shape
                x_axis = int(landmark.x * width) + 10
                y_axis = int(landmark.y * height) + 10
                landmark_list.append([index,x_axis,y_axis])
        return landmark_list

def main():
    current_time = 0
    previous_time = 0

    detector=hand_detector()
    cap = cv2.VideoCapture(0)

    i=0
    fps_list=[]
    while True:
        success,img=cap.read()

        img=detector.hand_tracker(img)
        landmark_list=detector.find_position(img)
        if len(landmark_list)!=0:
            print(landmark_list[12])

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(round(fps)), (30, 80), cv2.FLOODFILL_MASK_ONLY, 1, (0, 255, 0), 2)

        if i>=30:
            idx=i%30
            fps_list[idx]=fps
        else:
            fps_list.append(fps)

        avg_fps=sum(fps_list)/len(fps_list)

        cv2.putText(img, (str(round(avg_fps))+"  AVG FPS"), (30, 130), cv2.FLOODFILL_MASK_ONLY, 1, (0, 255, 0), 2)

        cv2.imshow("Image Recognizing", img)
        cv2.waitKey(1)
        i+=1

if __name__=="__main__":
    main()