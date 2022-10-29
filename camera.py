from enum import Flag
import cv2
import random
import pygame
import mediapipe as mp
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
from sys import exit

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        self.counter = 0 
        self.stage = None
        self.guide = None
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame = self.video.read()
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

   
         
    def get_frame(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        def calculate_angle(a,b,c):
            a = np.array(a) # First
            b = np.array(b) # Mid
            c = np.array(c) # End
            
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
            
            if angle >180.0:
                angle = 360-angle
                
            return angle 



        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self.video.isOpened():
                ret, frame = self.video.read()
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
            
                # Make detection
                results = pose.process(image)
            
                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    
                    # Get coordinates
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                            
                    # Calculate angle
                    angle = calculate_angle(shoulder, elbow, wrist)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle), 
                                tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Curl counter logic+
                  
                    if angle > 160:
                        self.stage = "down"
                        self.guide = "Upward"
                    if angle < 30 and self.stage =='down':
                        self.stage="up"
                        self.guide = "Downward"
                        self.counter +=1
                        #print(counter)

                except:
                    pass

                        # Setup status box
                cv2.rectangle(image, (0,0), (225,73), (0,0,0), -1)
                
                # Rep data
                cv2.putText(image, 'REPS', (15,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                cv2.putText(image, str(self.counter), 
                            (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Stage data
                cv2.putText(image, 'STAGE', (80,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                cv2.putText(image, self.stage, 
                            (80,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)



                cv2.rectangle(image, (640,0), (415,73), (0,255,0), -1)

                # guide data
                cv2.putText(image, 'Next', (430,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, self.guide, 
                            (430,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                        )
                ret,jpg=cv2.imencode('.jpg',image)
                return jpg.tobytes()


            
class Shoulder(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        self.counter = 0 
        self.stage = None
        self.guide = None
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame = self.video.read()
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

    def get_frame(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        def calculate_angle(a,b,c):
            a = np.array(a) # First
            b = np.array(b) # Mid
            c = np.array(c) # End
            
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
            
            if angle >180.0:
                angle = 360-angle
                
            return angle 



        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self.video.isOpened():
                ret, frame = self.video.read()
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
            
                # Make detection
                results = pose.process(image)
            
                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    
                    # Get coordinates
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                                    
                    # Calculate angle
                    angle = calculate_angle(hip, shoulder, elbow)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle), 
                                tuple(np.multiply(shoulder, [640, 480]).astype(int)), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Curl counter logic+
                  
                    if angle > 150:
                        self.stage = "down"
                        self.guide = "Upward"
                    if angle < 70 and self.stage =='down':
                        self.stage="up"
                        self.guide = "Downward"
                        self.counter +=1
                        #print(counter)

                except:
                    pass

                        # Setup status box
                cv2.rectangle(image, (0,0), (225,73), (0,0,0), -1)
                
                # Rep data
                cv2.putText(image, 'REPS', (15,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                cv2.putText(image, str(self.counter), 
                            (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

               
                
                # Stage data
                cv2.putText(image, 'STAGE', (80,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                cv2.putText(image, self.stage, 
                            (80,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)



                cv2.rectangle(image, (640,0), (415,73), (0,255,0), -1)

                # guide data
                cv2.putText(image, 'Next', (430,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, self.guide, 
                            (430,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                        )
                ret,jpg=cv2.imencode('.jpg',image)
                return jpg.tobytes()


class Leg(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        self.counter = 0 
        self.stage = None
        self.guide = None
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame = self.video.read()
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

    def get_frame(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        def calculate_angle(a,b,c):
            a = np.array(a) # First
            b = np.array(b) # Mid
            c = np.array(c) # End
            
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
            
            if angle >180.0:
                angle = 360-angle
                
            return angle 



        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self.video.isOpened():
                ret, frame = self.video.read()
                
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
            
                # Make detection
                results = pose.process(image)
            
                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    
                    # Get coordinates
                    hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                    ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                                            
                    # Calculate angle
                    angle = calculate_angle(hip, knee, ankle)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle), 
                                tuple(np.multiply(knee, [640, 480]).astype(int)), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Curl counter logic+
                  
                    if angle > 150:
                        self.stage = "up"
                        self.guide = "Downward"
                    if angle < 70 and self.stage =='up':
                        self.stage="down"
                        self.guide = "Upward"
                        self.counter +=1
                        #print(counter)

                except:
                    pass

                        # Setup status box
                cv2.rectangle(image, (0,0), (225,73), (0,0,0), -1)
                
                # Rep data
                cv2.putText(image, 'REPS', (15,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                cv2.putText(image, str(self.counter), 
                            (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Stage data
                cv2.putText(image, 'STAGE', (80,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                cv2.putText(image, self.stage, 
                            (80,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)



                cv2.rectangle(image, (640,0), (415,73), (0,255,0), -1)

                # guide data
                cv2.putText(image, 'Next', (430,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, self.guide, 
                            (430,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                        )
                ret,jpg=cv2.imencode('.jpg',image)
                return jpg.tobytes()



class Game(object):
    # def __init__(self):
    #     Flag = True
       
    # def __del__(self):
    #     self.cap.release()

    # def get_frame(self):
    #     #ret,frame = self.cap.read()
    #     ret,jpg=cv2.imencode('.jpg',frame)
    #     return jpg.tobytes()

    def get_frame(self):
        # Images
        pygame.init()
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.cap=cv2.VideoCapture(0)
        self.cap.set(3, 1280)  # width
        self.cap.set(4, 720)  # height
        self.width, self.height = 1280, 720
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Punch Reaction")
        imgBalloon = pygame.image.load('Resources/punching_bag.png').convert_alpha()
        rectBalloon = imgBalloon.get_rect()
        rectBalloon.x, rectBalloon.y = 200, 100
        
        # Variables
        speed = 15
        score = 0
        startTime = time.time()
        totalTime = 30
        
        # Detector
        detector = HandDetector(detectionCon=0.8, maxHands=2)
        
        
        def resetBalloon():
            rectBalloon.x = random.randint(100, img.shape[1] - 100)
            rectBalloon.y = img.shape[0] + 50
        
        
        # Main loop
        start = True
        while start:
            # Get Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
        
            # Apply Logic
            timeRemain = int(totalTime -(time.time()-startTime))
            if timeRemain <0:
                self.window.fill((255,255,255))
        
                font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 50)
                textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
                textTime = font.render(f'Time UP', True, (50, 50, 255))
                self.window.blit(textScore, (450, 350))
                self.window.blit(textTime, (530, 275))
        
            else:
                # OpenCV
                success, img = self.cap.read()
                img = cv2.flip(img, 1)
                hands, img = detector.findHands(img, flipType=False)
        
                rectBalloon.y -= speed  # Move the balloon up
                # check if balloon has reached the top without pop
                if rectBalloon.y < 0:
                    resetBalloon()
                    speed += 1
        
                if hands:
                    hand = hands[0]
                    x, y = hand['lmList'][8][0:2]
                    if rectBalloon.collidepoint(x, y):
                        resetBalloon()
                        score += 10
                        speed += 1
        
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                imgRGB = np.rot90(imgRGB)
                frame = pygame.surfarray.make_surface(imgRGB).convert()
                frame = pygame.transform.flip(frame, True, False)
                self.window.blit(frame, (0, 0))
                self.window.blit(imgBalloon, rectBalloon)
        
                font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 50)
                textScore = font.render(f'Score: {score}', True, (50, 50, 255))
                textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
                self.window.blit(textScore, (35, 35))
                self.window.blit(textTime, (1000, 35))
        
            # Update Display
            pygame.display.update()
            # Set FPS
            self.clock.tick(self.fps)
         	
        pygame.quit()
        self.cap.release()
            # ret,jpg=cv2.imencode('.jpg',frame)
            # return jpg.tobytes()