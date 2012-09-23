# Python Arduino Prototyping API v2

This is a project based on the original [Python Arduino Prototyping API](https://github.com/HashNuke/Python-Arduino-Prototyping-API).
I started a fork and after a while the whole thing was getting too different to make a pull request so I just put it here.
The old project had wierd things going on to handle the communication, where I rely on parseInt() to do the work for me.
There were also problems with analogWrite(), which is working in this version. 

Major changes:
- .pde is completely redone
- Small changes in the arduino.py file
- Added examples

Here follows the original README (with updated example):

> &copy; 2009-2010 Akash Manohar J <akash@akash.im>
> under the MIT License

The Python Arduino Prototyping API helps you to quickly prototype Arduino programs,
without having to repeatedly load the program to the Arduino board.

#### Setup:

1. Load prototype.pde onto your Arduino dev board.
2. Import the arduino lib in your python script.


## Methods

*Arduino.output(list_of_output_pins)* - set the output pins

**Digital I/O**

1. *Arduino.setHigh(pin_number)*
2. *Arduino.setLow(pin_number)*
3. *Arduino.getState(pin_number)*
4. *Arduino.getState()* - returns true if pin state is high, else it returns false.

**Analog I/O**

1. *Arduino.analogRead(pin_number)* - returns the analog value
2. *Arduino.analogWrite(pin_number, value)* - sets the analog value

**Misc**

1.) *Arduino.turnOff()* - sets all the pins to low state

2.) *Arduino.close()* - closes serial connection. Using this makes sure that you won't have to disconnect & reconnect the Arduino again to recover the serial port.

## Usage example

    from arduino import Arduino
    import time

    b = Arduino('/dev/ttyUSB0')
    pin = 9

    #declare output pins as a list/tuple
    b.output([pin])

    for xrange(10):
        b.setHigh(pin)
        time.sleep(1)
        print b.getState(pin)
        b.setLow(pin)
        print b.getState(pin)
        time.sleep(1)

    b.close()
