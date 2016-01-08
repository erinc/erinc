import fitbit
authd_client = fitbit.Fitbit('6430a603bf3d0cc53629a3ace47037d3', '71eea5d0316ab1b0636953d6bf24a5ac', resource_owner_key='43e4e8c4beb60bd54ac7f71fc73219fb', resource_owner_secret='d2fb687e641a13b337f236a21ffea650')

print '--------------------------------'
from pprint import pprint
from datetime import datetime
# pprint(authd_client.activities(date=datetime.today()))
print 'Steps: ', authd_client.activities(date=datetime.today())['summary']['steps']
print 'Slept: ', authd_client.sleep(date=datetime.today())['summary']['totalMinutesAsleep']/60.0
authd_client.sleep()