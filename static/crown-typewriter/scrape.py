import re
import string
import urllib

import json

SOURCE_URL = 'https://www.gutenberg.org/files/1342/1342-0.txt'
SOURCE_TEXT = urllib.urlopen(SOURCE_URL).read()
SOURCE_TEXT = filter(lambda x: x in string.uppercase, string.upper(SOURCE_TEXT))

digraphs = {}

for a in string.uppercase:
    for b in string.uppercase:
        digraphs[a+b] = SOURCE_TEXT.count(a+b)

f = open('digraphs.json', 'w')
json.dump(digraphs, f, indent=2)
f.close()
