import cv2
import asyncio
import os
from hand import HandTracker
from light import Smart_light
from dotenv import load_dotenv


async def main():

    
    load_dotenv()
    username = os.getenv("TAPO_USERNAME")
    password =os.getenv("TAPO_PASSWORD")
    ip = os.getenv("TAPO_IP")

    hand = HandTracker()
    camera = cv2.VideoCapture(0)
    lamp = Smart_light(username,password,ip)

    lamp.device = await lamp.connect_plug(username,password,ip)




    while True:
        captured,frame = camera.read()
        

       
        hand.detect(frame)
        hand.visualise_lm(frame)
        total_fingers = hand.count_fingers(frame)
        if (total_fingers == 1 and not lamp.cooldown_flag):
            asyncio.create_task(lamp.light_on())
        
        elif (total_fingers == 2 and not lamp.cooldown_flag):
            asyncio.create_task(lamp.light_off())
        
        await asyncio.sleep(0.001)
            


        
        
    # frame =cv2.circle(frame, (50, 50), 5, (255, 0, 255), cv2.FILLED)
        cv2.imshow("hand tracker",frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()


asyncio.run(main())