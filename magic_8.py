# Team 15
# ENG101
# Due 4/21/19

from magic_fun import *
# Becuase Buttons are user interactions we are importing them here
from gpiozero import Button

button1 = Button(21)

while True:
    # Wait until the user presses the button to start the game
    # this will have to be rewriten aysnychronously because I am 98% sure
    # that wait_for_press is blocking and we can't use blocking funcitons
    button(21).wait_for_press()

    # Aske the opening question
    open_question()

    # Wait for the user to finish asking the qustion
    button(21).wait_for_press()

    # Answer the user
    answer()





# Prompt User to ask question
# Ask a question then press the button for my answer?

# Wait for button to be pressed

# Delay with "hmm...."

# Answer the user
