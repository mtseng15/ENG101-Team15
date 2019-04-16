# Team 15
# ENG101
# Due 4/21/19

from magic_audio import *
import asyncio

async def haha():
    for i in range(100):
        print("haha")
        await asyncio.sleep(0.5)


async def laughing():
    for i in range(100):
        print("hehe")
        await asyncio.sleep(0.5)

        if i == 10:
            loop.close()


def main():
    loop = asyncio.get_event_loop()

    # Wait for button to be pressed
    m = input("Press any key to start")

    # Ask user qustion with flashing lights
    loop.run_until_complete(asyncio.wait([
        open_question(),
        haha()
    ], return_when=asyncio.FIRST_COMPLETED))


    # Play Jeopardy theme with lights while waitin for user to press Button
    m = input("Press a key to continue")
    # Things are far from done here. It may simply be byond the scope of This
    # class to try to get both lights and the Jeopardy theme to play simultaneously
    # AND wait for the button to be pressed. It's rather tricky and beyond my leage
    music = Jeopardy()


    # Play answer with more flashing lights
    loop.run_until_complete(asyncio.wait([
        answer(),
        haha()
    ], return_when=asyncio.FIRST_COMPLETED))







main()
