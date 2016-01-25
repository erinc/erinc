#!/usr/local/bin/python2.7

import fitbit
import os
import pytz
from datetime import datetime, timedelta
from pprint import pprint

script_dir = os.path.dirname(__file__)
steps_file_path = os.path.join(script_dir, 'templates/_steps.txt')
sleep_file_path = os.path.join(script_dir, 'templates/_sleep.txt')

authd_client = fitbit.Fitbit('6430a603bf3d0cc53629a3ace47037d3', '71eea5d0316ab1b0636953d6bf24a5ac', resource_owner_key='43e4e8c4beb60bd54ac7f71fc73219fb', resource_owner_secret='d2fb687e641a13b337f236a21ffea650')

print '--------------------------------'
# pprint(authd_client.activities(date=datetime.today()))

today = datetime.now(pytz.timezone('US/Pacific'))

try:
    steps = authd_client.activities(date=today)['summary']['steps']
except:
    steps = 0

try:
    sleep = authd_client.sleep(date=today)['summary']['totalMinutesAsleep']
except:
    sleep = 0

if sleep:
    print sleep
    hours = str(sleep / 60) + ' hours, '
    minutes = str( int(sleep) % 60 ) + ' minutes'
    sleep = hours + minutes
else:
    sleep = "0 hours"

# print 'Steps: ', authd_client.activities(date=datetime.today())['summary']['steps']
# print 'Slept: ', authd_client.sleep(date=datetime.today())['summary']['totalMinutesAsleep']/60.0

with open(steps_file_path, 'w') as the_file:
    the_file.write(str(steps))

with open(sleep_file_path, 'w') as the_file:
    the_file.write(sleep)    

authd_client.sleep()
