import RPi.GPIO as GPIO
import time
import threading
class StepperMotor(object):
    def __init__(self, pin0=5, pin1=6, pin2=13, pin3=19):
        self.pin0 = pin0
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3

        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(pin0, GPIO.OUT)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(pin3, GPIO.OUT)

        self._reset_pins()

        #setup a current step var
        #going to use a 8 step sequence
        self.current_step = 0

    def step(self, dir):
       
        if self.current_step == 0:#pin 0 is high
            GPIO.output(self.pin3, GPIO.LOW)
            GPIO.output(self.pin0, GPIO.HIGH)
            
            
        elif self.current_step == 1:#pin 0 and pin 1 are high
             GPIO.output(self.pin1, GPIO.HIGH)
             
            
        elif self.current_step == 2:#pin 1 is high
             GPIO.output(self.pin0, GPIO.LOW)
             
            
        elif self.current_step == 3:#pion 1 and pin 2 are high
            GPIO.output(self.pin2, GPIO.HIGH)
            
            
        elif self.current_step ==4:#pin 2 is high
            GPIO.output(self.pin1, GPIO.LOW)
            

        elif self.current_step == 5:#pin 2 and pin 3 are high
            GPIO.output(self.pin3, GPIO.HIGH)
            
            
        elif self.current_step == 6:#pin 3 is high
            GPIO.output(self.pin2, GPIO.LOW)
            
            
        elif self.current_step == 7:#pin 3 and pin 0 are high
            GPIO.output(self.pin0, GPIO.HIGH)
            
        else:
            raise Exception('Invalid step', 'There was an error')

        if dir == 'cw':
            self.current_step += 1

            if self.current_step > 7:
                self.current_step = 0
        elif dir == 'ccw':
            self.current_step -= 1

            if self.current_step < 0:
                self.current_step = 7
        else:
                raise Exception('Invalid input dir', 'Opitons are cw or ccw')
        return

    def turn_degrees(self, deg, dir, speed): #speed is degrees per second
        steps = deg*11#this leaves .377777 steps per degree since I rounded 11 down
        degrees_turned = 0
        counter = 0
        delay = 1/(speed*11)
        while(counter < steps):
            counter += 1
            self.step(dir)
            time.sleep(delay)
            if counter%11 == 0:
                degrees_turned += 1
            if degrees_turned % 3 == 0 and degrees_turned != 0:
                counter -= 1
        
        return



                
    def _reset_pins(self):
        GPIO.output(self.pin0, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin3, GPIO.LOW)
    def __del__(self):
        self._reset_pins()
        
    def cleanup(self):
        #wait for thread to become inactive
        while threading.active_count() > 1:
            time.sleep(1)
            
        GPIO.cleanup()

    def turn_degreesThreaded(self, deg, dir, speed):
        thread = threading.Thread(target=self.turn_degrees, args=(deg, dir, speed,))
        thread.start()
        return thread
        

def raise_lower(self, motor0, motor1, deg, dir, speed): #1, 2
    thread0 = motor1.turn_degreesThreaded(deg, dir, speed)
    thread1 = motor2.turn_degreesThreaded(deg, dir, speed)
    thread0.join()
    thread1.join()
    GPIO.cleanup()
        
if __name__ == "__main__":
    motor0 = StepperMotor(26,21,20,16)#left motor
    motor1 = StepperMotor(5,6,13,19)#right motor
    steps = 0
    raise_lower(motor0, motor1, 30, 'cw', 50)
    
   
