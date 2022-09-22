#Have you ever wondered how notifications work? This small python project idea will throw some light on this. The desktop notifier apps run on your system and send you a piece of information after a fixed interval of time. We suggest you use libraries such as notify2, requests, etc. to build such a program.

import datetime

a= datetime.datetime(2022, 9, 22, 17, 00, 00)
b = datetime.datetime(0,0,0,3,15,3)
c = a+b
print(a)
print(b)
print(c)