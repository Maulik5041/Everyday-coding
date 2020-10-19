import csv
import requests
from collections import OrderedDict
import urllib.request


url = "https://raw.githubusercontent.com/Maulik5041/challenges/community/13/movie_metadata.csv"
reader = urllib.request.urlretrieve(url)
print(reader.read(100).decode('utf-8'))
