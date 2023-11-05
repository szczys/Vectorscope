import _thread
import vectoros
from time import sleep
import ostentus_i2c

ostentus_i2c.init()

import machine
user_button = machine.Pin(19, machine.Pin.IN)
if user_button.value():
    vectoros.run()
else:
    import vectorscope
    v = vectorscope.Vectorscope()





