#Have you ever wondered how notifications work? This small python project idea will throw some light on this. The desktop notifier apps run on your system and send you a piece of information after a fixed interval of time. We suggest you use libraries such as notify2, requests, etc. to build such a program.

import datetime
from datetime import timedelta
import os


path = os.uname()
os.mkdir('/home/a/Desktop/Compressed_Python_Projects/new-directory1')
path = os.getcwd()

print(path)
print(path)

#Have you ever wondered how notifications work? This small python project idea will throw some light on this. The desktop notifier apps run on your system and send you a piece of information after a fixed interval of time. We suggest you use libraries such as notify2, requests, etc. to build such a program.

import datetime
from datetime import timedelta
import os
import notify2

now = datetime.datetime.now().replace(microsecond=0)
then = datetime.datetime(2022, 9, 24, 10, 59, 0)



minutes = (diff.seconds - hours * 3600) / 60

seconds = (diff.seconds - (hours * 3600 + minutes * 60))

def sendmessage(title, message):
    notify2.init("inage")
    notice = notify2.Notification(title, message, "/Downloads/anne-nicole-AfOT-zVezTM-unsplash.jpg").show()
    return notice

sendmessage("Time Remaining", "%s days, %s hours, %s minutes and % seconds." % (diff.days,hours,minutes,seconds))


