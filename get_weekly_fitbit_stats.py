#!/usr/local/bin/python2.7

import fitbit
import os
from datetime import datetime, timedelta
import pytz
from firebase import Firebase
f = Firebase('https://erinc.firebaseio.com/blog/', auth_token="novxUZ6B97vTwyPrOWtYGxVFKMgUqQ14cIbR3c3H")

authd_client = fitbit.Fitbit('6430a603bf3d0cc53629a3ace47037d3', '71eea5d0316ab1b0636953d6bf24a5ac', resource_owner_key='43e4e8c4beb60bd54ac7f71fc73219fb', resource_owner_secret='d2fb687e641a13b337f236a21ffea650')

today = datetime.now(pytz.timezone('US/Pacific'))

week_steps = 0
for i in range(1,8):
    d = today - timedelta(days=i)
    s = authd_client.activities(date=d)['summary']['steps']
    week_steps = week_steps + s

week_avg = week_steps / 7
f.patch({'steps_avg':str(week_avg)})

authd_client.sleep()