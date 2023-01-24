import board 
import digitalio 
import time
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = board.I2C()
i2c_bus = board.STEMMA_I2C()
ss = Seesaw(i2c_bus, addr=0x36)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    print("Temp: " + str((9/5)*temp + 32) + " Moisture: " + str(touch))
    time.sleep()



#     .          _            
#   ,'/ _   /7 ,' \ _    () __
# ,'o/ /o| / \/ 0 // \/7/7,','
#(___7/_,'/n_/\_,'/_n_/// \_\ 
#    // 