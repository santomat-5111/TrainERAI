import cv2
import mediapipe as mp
import numpy as np

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
                cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
                
                # Rep data
                cv2.putText(image, 'REPS', (15,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, str(self.counter), 
                            (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Stage data
                cv2.putText(image, 'STAGE', (80,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, self.stage, 
                            (80,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)



                cv2.rectangle(image, (640,0), (415,73), (0,255,0), -1)

                # guide data
                cv2.putText(image, 'Now', (430,24), 
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
                cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
                
                # Rep data
                cv2.putText(image, 'REPS', (15,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, str(self.counter), 
                            (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Stage data
                cv2.putText(image, 'STAGE', (80,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, self.stage, 
                            (80,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)



                cv2.rectangle(image, (640,0), (415,73), (0,255,0), -1)

                # guide data
                cv2.putText(image, 'Now', (430,24), 
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
                cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
                
                # Rep data
                cv2.putText(image, 'REPS', (15,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, str(self.counter), 
                            (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                # Stage data
                cv2.putText(image, 'STAGE', (80,24), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, self.stage, 
                            (80,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)



                cv2.rectangle(image, (640,0), (415,73), (0,255,0), -1)

                # guide data
                cv2.putText(image, 'Now', (430,24), 
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