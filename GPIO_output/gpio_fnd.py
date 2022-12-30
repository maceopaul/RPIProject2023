import Rpi.GPIO as GPIO
import time


# GPIO output raspberry pi pinnum 
#        A   B   C   D   E   F   G   DP
seg = [8, 10, 12, 13, 19, 21, 23, 24]

num = 0

#       A B C D E F G DP
fnd = [(1,1,1,1,1,1,0,0),#0
       (                ),#1
       (                ),#2
       (                ),#3
       (                ),#4
       (                ),#5
       (                ),#6
       (                ),#7
       (                ),#8
       (                )]#9

def FND_setup():
    setmode(BOARD)
    setwarnings(False)
    GPIO.setup(seg,GPIO.OUT,initial=GPIO.LOW)

def main():
    i=0
    FND_setup()
    
    while True:        
        # GPIO.output(GPIO pin, GPIO out)
        time.sleep(1)
        

if __name__ == '__main__':
    main()

