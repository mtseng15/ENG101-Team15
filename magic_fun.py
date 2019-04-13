# Functions needed for Team 15's Magic 8 ball

# Because LED's don't require user interaction, we are importing them here
# from gpiozero import LED
import subprocess
import time
import random

# Instantiate the LEDs
# led1 = LED(4) # Yellow
# led2 = LED(17) # Yellow
# led3 = LED(27) # Yellow
# led4 = LED(22) # Yellow
# led5 = LED(5) # Red
# led6 = LED(6) # Red
# led7 = LED(13) # Green
# led8 = LED(19) # Green
# led9 = LED(26) # Blue
# leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9]


def open_question():
    print("What is the question you would like answered? Then press the button for my answer.")


def answer():
    print("My answer is yes")

# def crazy_LED():
#     for i in leds:
#         i.on()

#     time.sleep(1)
#     for i in leds:
#         i.off()


# def thoughtful_LED():
#     for i in leds:
#         i.on()
#         time.sleep(1)
#         i.off()
