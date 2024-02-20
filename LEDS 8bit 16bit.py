import machine
import utime

led0 = machine.Pin(0,machine.Pin.OUT)
led1 = machine.Pin(1,machine.Pin.OUT)
led2 = machine.Pin(2,machine.Pin.OUT)
led3 = machine.Pin(3,machine.Pin.OUT)
led4 = machine.Pin(4,machine.Pin.OUT)
led5 = machine.Pin(5,machine.Pin.OUT)
led6 = machine.Pin(6,machine.Pin.OUT)
led7 = machine.Pin(7,machine.Pin.OUT)
led8 = machine.Pin(8,machine.Pin.OUT)
led9 = machine.Pin(9,machine.Pin.OUT)
led10 = machine.Pin(10,machine.Pin.OUT)
led11 = machine.Pin(11,machine.Pin.OUT)
led12 = machine.Pin(12,machine.Pin.OUT)
led13 = machine.Pin(13,machine.Pin.OUT)
led14 = machine.Pin(14,machine.Pin.OUT)
led15 = machine.Pin(15,machine.Pin.OUT)

led16 = machine.Pin(16,machine.Pin.OUT)
led17 = machine.Pin(17,machine.Pin.OUT)
led18 = machine.Pin(18,machine.Pin.OUT)

def LED16(display_data):
    led0.value((display_data & 0b0000000000000001) >>0)
    led1.value((display_data & 0b0000000000000010) >>1)
    led2.value((display_data & 0b0000000000000100) >>2)
    led3.value((display_data & 0b0000000000001000) >>3)
    led4.value((display_data & 0b0000000000010000) >>4)
    led5.value((display_data & 0b0000000000100000) >>5)
    led6.value((display_data & 0b0000000001000000) >>6)
    led7.value((display_data & 0b0000000010000000) >>7)   
    led8.value((display_data & 0b0000000100000000) >>8)
    led9.value((display_data & 0b0000001000000000) >>9)
    led10.value((display_data & 0b0000010000000000) >>10)
    led11.value((display_data & 0b0000100000000000) >>11)
    led12.value((display_data & 0b0001000000000000) >>12)
    led13.value((display_data & 0b0010000000000000) >>13)
    led14.value((display_data & 0b0100000000000000) >>14)
    led15.value((display_data & 0b1000000000000000) >>15)     

def LED8(display_data):
    led0.value((display_data & 0b00000001) >>0)
    led1.value((display_data & 0b00000010) >>1)
    led2.value((display_data & 0b00000100) >>2)
    led3.value((display_data & 0b00001000) >>3)
    led4.value((display_data & 0b00010000) >>4)
    led5.value((display_data & 0b00100000) >>5)
    led6.value((display_data & 0b01000000) >>6)
    led7.value((display_data & 0b10000000) >>7) 

led16.value(1)
led17.value(1)
led18.value(1)

while True:
    
    for x in range (0,255):
        LED8(~x)
        utime.sleep(0.01)
        
    for y in range (0,65535):
        LED16(~y)
        utime.sleep(0.01)
        
