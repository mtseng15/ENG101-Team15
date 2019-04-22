
# Because LED's don't require user interaction, we are importing them here
from gpiozero import LED
import time
import asyncio
import random



# Instantiate the LEDs
led1 = LED(4) # Yellow
led2 = LED(17) # Yellow
led3 = LED(27) # Yellow
led4 = LED(22) # Yellow
led5 = LED(5) # Red
led6 = LED(6) # Red
led7 = LED(13) # Green
led8 = LED(19) # Green
led9 = LED(26) # Blue
leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9]

yellow_leds = [led1, led2, led3, led4]
red_leds = [led5, led6]
green_leds = [led7, led8]
blue_leds = [led9]

#Flash blue and green leds
async def opening_lights():
    for j in range(6):
        for i in blue_leds:
            i.on()

        await asyncio.sleep(0.5)

        for i in blue_leds:
            i.off()
            
        for i in green_leds:
            i.on()

        await asyncio.sleep(0.5)

        for i in green_leds:
            i.off()


#End of function Opening_lights

#Quickly scroll through all leds
async def crazy_LED():

    for j in range(5):
        #Turn LEDs on
        for i in leds:
            i.on()
            await asyncio.sleep(0.1)

        #Short pause
        await asyncio.sleep(0.2)

        #Turn LEDs Off
        for i in leds:
            i.off()
            await asyncio.sleep(0.1)
            
#End of crazy_LED() Function        

#Slowly toggle every led on and off
async def thoughtful_LED():
    for i in leds:
        i.on()
        await asyncio.sleep(0.5)
        i.off()

#End of toughtful_LED() Function

#Toggle stop light colors on and off
async def stop_lights():
    for i in yellow_leds:
        i.on()

        
    await asyncio.sleep(0.3)
    for i in yellow_leds:
        i.off()

    for i in red_leds:
        i.on()

        
    await asyncio.sleep(0.3)
    for i in red_leds:
        i.off()

    for i in green_leds:
        i.on()

        
    await asyncio.sleep(0.3)
    for i in green_leds:
        i.off()

#End of stop_lights() function

#Flash only red LEDs
async def red_flashing():
    for i in range(10):
        for j in red_leds:
            j.on()
            await asyncio.sleep(0.07)
            j.off()

#End of red_flashing() Function

#Flash only yellow LEDs
async def yellow_flashing():
    for i in range(10):
        for j in yellow_leds:
            j.on()
            await asyncio.sleep(0.07)
            j.off()

#End of yellow_flashing() Function

#Flash only green LEDs
async def green_flashing():
    for i in range(10):
        for j in green_leds:
            j.on()
            await asyncio.sleep(0.07)
            j.off()

#End of green_flashing() Function

#Turn on and off totally random leds
async def total_random():
    for i in range (10):
        rand_num=random.randint(0,8)

        if rand_num == 0:
            led1.on()
            await asyncio.sleep(0.07)
            led1.off()

        elif rand_num == 1:
            led2.on()
            await asyncio.sleep(0.07)
            led2.off()

        elif rand_num == 2:
            led3.on()
            await asyncio.sleep(0.07)
            led3.off()

        elif rand_num == 3:
            led4.on()
            await asyncio.sleep(0.07)
            led4.off()

        elif rand_num == 4:
            led5.on()
            await asyncio.sleep(0.07)
            led5.off()

        elif rand_num == 5:
            led6.on()
            await asyncio.sleep(0.07)
            led6.off()

        elif rand_num == 6:
            led7.on()
            await asyncio.sleep(0.07)
            led7.off()

        elif rand_num == 7:
            led8.on()
            await asyncio.sleep(0.07)
            led8.off()

        elif rand_num == 8:
            led9.on()
            await asyncio.sleep(0.07)
            led9.off()
    #End of for loop

#End of total_random() function

#Turn all leds on and then turn one off at a time
async def subtractive_LED():
    for j in range(5):
        for i in leds:
            i.on()
    
        for i in leds:
            i.off()
            await asyncio.sleep(.1)
            i.on()

#End of subtractive_LED() Function


#Function to turn on and off leds by color
async def on_off_LED():
    for i in range(10):
        for j in blue_leds:
            j.on()

        await asyncio.sleep(.2)
        for j in green_leds:
            j.on()

        await asyncio.sleep(.2)
        for j in red_leds:
            j.on()

        await asyncio.sleep(.2)
        for j in yellow_leds:
            j.on()

        await asyncio.sleep(.2)
        for j in blue_leds:
            j.off()

        await asyncio.sleep(.2)
        for j in green_leds:
            j.off()

        await asyncio.sleep(.2)
        for j in red_leds:
            j.off()

        await asyncio.sleep(.2)
        for j in yellow_leds:
            j.off()

        await asyncio.sleep(.2)

        #End of j for loop

    #End of i for loop


#All off function
def all_LEDs_off():
    for i in leds:
        i.off()

#End of all_off function




####Random Function Picker
#initalize list of all functions
func_list=[crazy_LED, thoughtful_LED, stop_lights, red_flashing, yellow_flashing, green_flashing, total_random, subtractive_LED, on_off_LED]

async def rand_light_function():
    # await a random function to be excecuted in the event loop
    await random.choice(func_list)()
    
