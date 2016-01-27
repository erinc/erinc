from pocket import Pocket
import datetime
import pytz
import os
from firebase import Firebase
f = Firebase('https://erinc.firebaseio.com/blog/', auth_token="novxUZ6B97vTwyPrOWtYGxVFKMgUqQ14cIbR3c3H")

consumer_key = "50565-f102f306ba3067de6dc3825b"
access_token = '8e80403e-a37d-b45a-ae4e-7b7526'

pocket_instance = Pocket(consumer_key, access_token)

# unread_posts = pocket_instance.get()
# print 'unread', len(unread_posts[0]['list'])

# archived_posts = pocket_instance.get(state='archive')
# print 'read', len(archived_posts[0]['list'])

today = datetime.datetime.now(pytz.timezone('US/Pacific'))
yesterday = today - datetime.timedelta(hours=24)
unix_time = yesterday.strftime("%s")

today_read_articles = pocket_instance.get(state='archive', since=unix_time)
today_read_count = len(today_read_articles[0]['list'])
print 'read today', today_read_count

unread_count = len(pocket_instance.get()[0]['list'])

f.patch({'pocket_read':today_read_count})
f.patch({'pocket_unread':unread_count})