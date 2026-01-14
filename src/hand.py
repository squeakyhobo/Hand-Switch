import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time 



class HandTracker:

    
    


    def __init__(self):
        self.dectector = self.make_model()
        self.result = None
        self.CONNECTIONS = [
    # Thumb
    (0, 1), (1, 2), (2, 3), (3, 4),(2,5),
    # Index
    (5, 6), (6, 7), (7, 8),
    # Middle
    (9, 10), (10, 11), (11, 12),
    # Ring
    (13, 14), (14, 15), (15, 16),
    # Pinky
    (0, 17), (17, 18), (18, 19), (19, 20),
    # (Palm)
    (5, 9), (9, 13), (13, 17)
]
       
        


    
    def result_call(self,result, output_image, timestamp_ms):
        if result:
            self.result =result
       

                    
            

    
                     
        





    def make_model(self):

        
        base_options = python.BaseOptions(model_asset_path='resources /hand_landmarker.task')
        live_feed_option = vision.RunningMode.LIVE_STREAM
        options = vision.HandLandmarkerOptions(
            base_options = base_options,
            running_mode = live_feed_option,
            result_callback= self.result_call,
            num_hands =2
        )

        dectector = vision.HandLandmarker.create_from_options(options)

        return dectector
        
        
        
        
            
        
            
            
        
            
    def detect(self,frame):
        mp_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        timestamp = int(time.time()*1000)
        result = self.dectector.detect_async(mp_frame,timestamp)  
        

    def visualise_lm(self,frame):
        coords =[]
        h, w, _ = frame.shape
        if self.result:
            for hand in self.result.hand_landmarks:
                for point in hand:
                    coords.append((int(point.x * w), int(point.y * h)))
                    
                    
                for pt in coords:
                    cv2.circle(frame, pt, 5, (0, 255, 0), -1)
                for edge in self.CONNECTIONS:
                    cv2.line(frame,coords[edge[0]],coords[edge[1]],(0, 255, 0),2)

    def count_fingers(self,frame):
        total_fingers =0
        
        if self.result:
            
            if self.result.hand_landmarks:
                

                for i in range(len(self.result.hand_landmarks)):
                
                    lm = self.result.hand_landmarks[0]
                    
                    
                    
                    # coords start from top left of the screen , so the biiger y in the real world will be smaller in this 
                    
                    #index
                    y8 = lm[8].y
                    y6 = lm[6].y
                    if(y8<=y6):
                        total_fingers+=1
                    
                    #middle 
                    y12 = lm[12].y
                    y10 = lm[10].y
                    if(y12<=y10):
                        total_fingers+=1
                    
                    # ring
                    y16 = lm[16].y
                    y14 =lm[14].y

                    if(y16<=y14):
                        total_fingers+=1

                    #pinky

                    y20 =lm[20].y
                    y18 =lm[18].y

                    if(y20<=y18):
                        total_fingers+=1

                    
                        
        
        cv2.putText(frame,f'fingers up: {total_fingers}',(20,70),cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 2)
        return total_fingers



               
                
                   
                

                
        
    
    




        


