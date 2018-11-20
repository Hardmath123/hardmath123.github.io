import re
import string
import urllib

import json

SOURCE_URLS = []
SOURCE_URLS.append('https://www.gutenberg.org/files/1342/1342-0.txt') # pride and prejudice (1813)
SOURCE_URLS.append('http://www.gutenberg.org/files/35/35-0.txt') # the time machine (1895)
SOURCE_URLS.append('http://www.gutenberg.org/cache/epub/1661/pg1661.txt') # sherlock holmes (1892)

digraphs = {}

for URL in SOURCE_URLS:
    print "Scraping", URL, "..."
    SOURCE_TEXT = urllib.urlopen(URL).read()
    SOURCE_TEXT = filter(lambda x: x in string.uppercase, string.upper(SOURCE_TEXT))

    for a in string.uppercase:
        for b in string.uppercase:
            digraphs[a+b] = SOURCE_TEXT.count(a+b) + digraphs.get(a+b, 0)

print "Done scraping."

f = open('digraphs.h', 'w')
f.write('const int digraphs[26][26] = {\n')
for x in string.uppercase:
    f.write('  {')
    for y in string.uppercase:
        f.write(str(digraphs[x+y]))
        if y != 'Z':
            f.write(', ')
    f.write('}')
    if x != 'Z':
        f.write(',')
    f.write('\n')
f.write('};\n')
f.close()
