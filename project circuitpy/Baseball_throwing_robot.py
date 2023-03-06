import time
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor

DEBUG = True  # mode of operation; False = normal, True = debug
OP_DURATION = 1  # operation duration in seconds

drv6612_ain1 = PWMOut(board.D5, frequency=50)
drv6612_ain2 = PWMOut(board.D4, frequency=50)
drv6612_sleep = DigitalInOut(board.D0)

button_a = DigitalInOut(board.D8)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

motor_a = Motor.DCMotor(drv6612_ain1, drv6612_ain2)


def print_motor_status(motor):
    if motor == motor_a:
        motor_name = "A"
    else:
        motor_name = "Unknown"
    print(f"Motor {motor_name} throttle is set to {motor.throttle}.")
# Main
drv6612_sleep.direction = Direction.OUTPUT
drv6612_sleep.value = True  # enable (turn on) the motor driver

while True:
    if button_a.value:
        print((1,))
        def basic_operations():
            # Drive forward at full throttle
            motor_a.throttle = 1.0
            time.sleep(0.5)

    else:
        print((0,))
    time.sleep(0.1)
    def basic_operations():
        # Brake to a stop
        motor_a.throttle = None