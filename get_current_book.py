import requests
from xml.etree import ElementTree
import os
from firebase import Firebase
f = Firebase('https://erinc.firebaseio.com/blog/', auth_token="novxUZ6B97vTwyPrOWtYGxVFKMgUqQ14cIbR3c3H")

goodreads_url = "https://www.goodreads.com/review/list/15767078?format=xml&key=EakwJ1KkkfReddLlPeGMig&v=2&shelf=currently-reading"
response = requests.get(goodreads_url)
tree = ElementTree.fromstring(response.content)

title = tree.find('reviews').find('review').find('book').find('title').text
link = tree.find('reviews').find('review').find('book').find('link').text
out = '<a target="_blank" href="'+link+'">'+title+'</a>'

f.patch({'book':out})
