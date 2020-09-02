import time
import datetime
#241
now = datetime.datetime.now()
print(now)

#242
print(now, type(now))

#243
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

#244
print(now.strftime("%H:%M:%S"))

#245
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#246
'''
while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
'''

#247
'''
import 모듈
from 모듈 import 이름
del 모듈
from importlib import reload
reload(모듈)
'''

#248
import os
ret = os.getcwd()
print(ret, type(ret))

#249
#os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

#250
import numpy
for i in numpy.arange(0, 1, 0.5):
    print(i)