import fitbit
import os
import pytz
from datetime import datetime, timedelta
from pprint import pprint
from firebase import Firebase
f = Firebase('https://erinc.firebaseio.com/blog/', auth_token="novxUZ6B97vTwyPrOWtYGxVFKMgUqQ14cIbR3c3H")

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


f.patch({'steps':steps})
f.patch({'sleep':sleep})

authd_client.sleep()
