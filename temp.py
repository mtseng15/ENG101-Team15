from magic_audio import *


# Instantiates the event loop
loop = asyncio.get_event_loop()

# a symple function to test asynchronousness
async def haha(x):

    for i in range(0,x):
        # print hahaha
        print("haha")
        # then hand processing back
        await asyncio.sleep(0.1)


# This is the main function where all things will go
async def main():

    music = Jeopardy()

    music.start()
    time.sleep(10)
    music.stop()
    # This creates a waiting loop for all the functions we want to be asyncronus to run




# Calls the event loop to run until complete
# On our actual python script we shoudl probably use loop.run_forever(main())
loop.run_until_complete(main())
loop.close()
