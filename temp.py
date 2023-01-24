import board 
import digitalio 
import time 
import adafruit_sht4x

sht = adafruit_sht4x.SHT4x(board.I2C())
print(sht.temperature)
print(sht.relative_humidity)

i2c = board.I2C()
sht = adafruit_sht4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION 
print("Current mode is:" , adafruit_sht4x.Mode.string[sht.mode])
i2c_bus = board.I2C()

while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f F" % ((9/5)*temperature + 32))
    print("Humidity is: %0.1f %%" % relative_humidity)
    print("")
    time.sleep()

#     .          _            
#   ,'/ _   /7 ,' \ _    () __
# ,'o/ /o| / \/ 0 // \/7/7,','
#(___7/_,'/n_/\_,'/_n_/// \_\ 
#    // 
