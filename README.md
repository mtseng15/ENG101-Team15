# ENG101-Team15
Team15's Raspberry Pi Magic 8 Ball

Please look at https://guides.github.com/activities/hello-world/ for a tutorial on how to use GitHub

magic_8.py - main python file

magic_fun.py - functions dealing with everything

There is also a great video series by The Coding Train about Git and Github on youtube.
	https://www.youtube.com/watch?v=yXT1ElMEkW8&list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV&index=6

After doing testing, we need use asynchronous coding for this to both play audio and lights simultaneously. I have started to implement it in the temp.py and the magic_audio.py. The big thing, is that we can't use blocking functions such as time.sleep() or subprocess.run() or Button.wait_for_press(). Instead we must use (or write) asynchronous versions such as asyncio.sleep() or subprocess.Popen().

Here are some youtube videos and documentation to help understand asynchronous coding. It's kinda wacky at first, if you haven't seen it before.

https://www.youtube.com/watch?v=tSLDcRkgTsY
https://docs.python.org/3/library/asyncio.html
https://www.youtube.com/watch?v=iG6fr81xHKA
