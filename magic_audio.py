# Functions needed for Team 15's Magic 8 ball

import subprocess
import asyncio
import random

# We chose to use asyncio in order to play lights simultainiously while playing audio.
# We thought this was probably the easest method of coordinating both functions
# asynchronously while maintaining a synchronous application flow. In the end we
# started and stoped the event loop twice and with each iteration we instantiate
# a new event loop.

# Audio answers
sounds = {0:'./audio/Uhhhmmm.mp3',1:'./audio/absativly.mp3',
    2:'./audio/afermitutly.mp3',3:'./audio/ask_your_mother.mp3',
    4:'./audio/bannans_on_moon.mp3',5:'./audio/can_you_ask.mp3',
    6:'./audio/certain.mp3',7:'./audio/concentrate_harder.mp3',
    8:'./audio/cookie_monster.mp3',9:'./audio/do_you_really_need.mp3',
    10:'./audio/dont_worry.mp3',11:'./audio/doubtful.mp3',
    12:'./audio/elmer_fud.mp3',13:'./audio/hazzy.mp3',
    14:'./audio/hehehe.mp3',15:'./audio/signs.mp3',
    16:'./audio/sure.mp3',17:'./audio/sure_I_mean.mp3',
    18:'./audio/the_stars.mp3',19:'./audio/washing_machine.mp3',
    20:'./audio/well.mp3',21:'./audio/without.mp3',
    22:'./audio/yuppers.mp3'}

# Play the opening audio
async def open_question():
    # Start a process to play the audio file
    p = subprocess.Popen("mpg123 ./audio/Opening.mp3".split())

    # Checks to see if the process has finished
    while p.poll() == None:
        # hands processing back, if the audio hasn't finished playing
        await asyncio.sleep(0.5)

    # terminates the process
    p.terminate()


#This function will run through each audio file in order to test and make sure
# it runs
async def test_audio():
    for i in sounds:
        # Start process that runs audio file
        p = subprocess.Popen(["mpg123", sounds[i]])

        # Checks to see if the process has finished
        while p.poll() == None:
            # hands processing back, if the audio hasn't finished playing
            await asyncio.sleep(0.5)

        # terminates the process
        p.terminate()
        

#This function plays a randomly selected audio answer
async def answer():
    # chose a random integer
    i=random.randint(0,22)

    # Start process that runs audio file
    p=subprocess.Popen(["mpg123", sounds[i]])

    # Checks to see if the process has finished
    while p.poll() == None:
        # hands processing back, if the process hasn't finished
        await asyncio.sleep(0.5)

    # terminates the process
    p.terminate()

