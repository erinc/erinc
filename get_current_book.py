import requests
from xml.etree import ElementTree
import os

script_dir = os.path.dirname(__file__)
rel_path = "templates/data.txt"
book_file_path = os.path.join(script_dir, 'templates/_book.txt')

goodreads_url = "https://www.goodreads.com/review/list/15767078?format=xml&key=EakwJ1KkkfReddLlPeGMig&v=2&shelf=currently-reading"
response = requests.get(goodreads_url)
tree = ElementTree.fromstring(response.content)

title = tree.find('reviews').find('review').find('book').find('title').text
link = tree.find('reviews').find('review').find('book').find('link').text
out = '<a target="_blank" href="'+link+'">'+title+'</a>'

with open(book_file_path, 'w') as the_file:
    the_file.write(out)   