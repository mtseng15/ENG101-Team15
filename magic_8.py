# Team 15
# ENG101
# Due 4/21/19

from gpiozero import Button
from magic_audio import *
from magic_lights import *
import asyncio

# instantiate button
button1=Button(18)

# main function
def main():
    # Instantiate a new event loop
    loop = asyncio.new_event_loop()

    # Wait for button to be pressed
    button1.wait_for_press()

    # Ask user qustion with flashing lights
    loop.run_until_complete(asyncio.wait([
        open_question(), # ask the opening question
        opening_lights() # display the opening lights  
    ], return_when=asyncio.ALL_COMPLETED))


    # Wait for the user to ask the question
    button1.wait_for_press()


    # Play answer with more flashing lights
    loop.run_until_complete(asyncio.wait([
        answer(), # play the answer
        rand_light_function() # display a random light function
    ], return_when=asyncio.FIRST_COMPLETED))

    #Call function to turn off all LEDs
    all_LEDs_off()

    # Close the current event loop
    loop.close()


# safety against accedently starting an infinate loop
if __name__ == "__main__":
    # Print names and team
    print("Team #15\nJacob Dumbacher\nZach Helton\nJason Riebe\nMicah Tseng")

    # Run Magic 8 ball
    while True:
        main()
