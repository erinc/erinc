import json, requests

url = 'https://medium.com/@erinc/latest'

params = dict(
    count=1
)

headers = {
    "Accept": "application/json",
}

resp = requests.get(url=url, params=params,  headers=headers)
data = json.loads(resp.text.replace('])}while(1);</x>', ''))

from pprint import pprint
pprint(data)

# for post in data['payload']['posts']:
#     if not post['inResponseToPostId']:
#         print '------------------'
#         print post['title']
#         print post['virtuals']['emailSnippet']