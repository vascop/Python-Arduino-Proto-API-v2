from arduino import Arduino
import time

b = Arduino('/dev/ttyUSB0')
pin = 9

#declare output pins as a list/tuple
b.output([pin])

brightness = 0
fadeAmount = 3

b.output([pin])

while (True):
    b.analogWrite(pin, brightness)
    time.sleep(0.05)
    print b.analogRead(pin)
    brightness = brightness + fadeAmount

    if (brightness == 0 or brightness == 255):
        fadeAmount = -fadeAmount