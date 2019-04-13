# Functions needed for Team 15's Magic 8 ball


import subprocess
import asyncio
import random



# Play the opeing audio
async def open_question():
    # Start a process to play the audio file
    p = subprocess.Popen("mpg123 ./audio/Opening.mp3".split())

    # Checks to see if the process has finished
    while p.poll() == None:
        # hands processing back, if the process hasn't finished
        await asyncio.sleep(0.5)

    # terminates the process
    p.terminate()


def answer():
    print("My answer is yes")
