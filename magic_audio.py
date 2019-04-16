# Functions needed for Team 15's Magic 8 ball


import subprocess
import asyncio
import random

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
        # hands processing back, if the process hasn't finished
        await asyncio.sleep(0.5)

    # terminates the process
    p.terminate()


#This function will run through each audio file in order
async def test_audio():
    for i in sounds:
        p = subprocess.Popen(["mpg123", sounds[i]])


        # Checks to see if the process has finished
        while p.poll() == None:
            # hands processing back, if the process hasn't finished
            await asyncio.sleep(0.5)

        # terminates the process
        p.terminate()

#This function returns a randomly selected audio answer
async def answer():
    i=random.randint(0,22)
    p=subprocess.Popen(["mpg123", sounds[i]])

    # Checks to see if the process has finished
    while p.poll() == None:
        # hands processing back, if the process hasn't finished
        await asyncio.sleep(0.5)

    # terminates the process
    p.terminate()


class Jeopardy(object):
    async def start(self):
        self.p = subprocess.Popen(["mpg123","./audio/Jeopardy-theme-song.mp3"])

        while self.p.poll() == None:
            # hands processing back, if the process hasn't finished
            await asyncio.sleep(0.5)

        self.p.terminate()

    async def stop(self):
        self.p.terminate()
