from arduino import Arduino
import time

b = Arduino('/dev/ttyUSB0')
pin = 1

b.output([])

while (True):
    val = b.analogRead(pin)
    print val
    time.sleep(0.5)