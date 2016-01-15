#!/usr/local/bin/python2.7

import json
import requests
import os
script_dir = os.path.dirname(__file__)
rel_path = "templates/data.txt"
posts_file_path = os.path.join(script_dir, 'templates/_posts.txt')

url = 'https://medium.com/@erinc/latest'

params = dict(
    count=10
)

headers = {
    "Accept": "application/json",
}

resp = requests.get(url=url, params=params,  headers=headers)
data = json.loads(resp.text.replace('])}while(1);</x>', ''))

# from pprint import pprint
# pprint(data)
out = ''
url_base = 'https://medium.com/@erinc/'

for post in data['payload']['posts']:
    if not post['inResponseToPostId']:
        # print '------------------'
        # pprint(post)
        out += '<li><a target="_blank" href="%s">%s</a></li>\n' %(url_base + post['id'] ,post['title'])
        # print post['title']
        # print post['virtuals']['emailSnippet']

print out
with open(posts_file_path, 'w') as the_file:
    the_file.write(out)   