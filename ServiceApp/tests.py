import datetime

from django.test import TestCase

# Create your tests here.

import time, sched
import datetime

s = sched.scheduler(time.time, time.sleep)

def print_time(a='default'):
    print('Now Time:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),a)

def print_some_times():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    s.enter(10,1,print_time)
    s.enter(5,2,print_time,argument=('positional',))
    s.run()

print_some_times()