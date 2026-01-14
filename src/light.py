import tapo
import asyncio
from tapo import ApiClient

class Smart_light:
    
    

    def __init__(self,username,password,ip):
        
        self.device = None
        self.cooldown_flag = False

    async def connect_plug(self,username,password,ip):
        client = ApiClient(username,password)
        device = await client.p110(ip)
        print("connceted to plug")
        return device
    
        

    async def light_on(self):
        ##device = await self.connect_plug()
       

        
        
        await self.device.on()
        self.cooldown_flag =True
        await asyncio.sleep(3)
        self.cooldown_flag =False

    async def light_off(self):
        
        ##device = await self.connect_plug()
        
        
        await self.device.off()
        self.cooldown_flag =True
        await asyncio.sleep(3)
        self.cooldown_flag =False
    




####light = Smart_light("lucasbubuoppenheimer@gmail.com","Respawnables2006!","192.168.1.103")
##asyncio.run(light.light_on())
