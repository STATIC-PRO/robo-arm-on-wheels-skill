import RPi.GPIO as GPIO
import time
from mycroft import MycroftSkill, intent_file_handler
# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(26,GPIO.OUT)
servo1 = GPIO.PWM(26,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)


class RoboArmOnWheels(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wheels.on.arm.robo.intent')
    def handle_wheels_on_arm_robo(self, message):
        action = message.data.get('action')

        if action.casefold() == "dance":
        self.log.info("Blinking!")
        self.speak_dialog('wheels.on.arm.robo', data={
            'action': action
        })
        servo1.ChangeDutyCycle(2+(180/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        servo1.ChangeDutyCycle(2+(180/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

def create_skill():
    return RoboArmOnWheels()

