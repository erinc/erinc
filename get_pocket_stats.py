from pocket import Pocket
import datetime
import pytz
import os

script_dir = os.path.dirname(__file__)
pocket_read_file_path = os.path.join(script_dir, 'templates/_pocket_read.txt')
pocket_unread_file_path = os.path.join(script_dir, 'templates/_pocket_unread.txt')


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


with open(pocket_read_file_path, 'w') as the_file:
    the_file.write(str(today_read_count))

with open(pocket_unread_file_path, 'w') as the_file:
    the_file.write(str(unread_count))
