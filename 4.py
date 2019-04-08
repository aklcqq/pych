# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re, string
words = ''
base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
fhand = urllib.request.urlopen(base + '63579')
for line in fhand:
    nwords = line.decode().strip()
nwords.split(' ')
a = nwords[24:]
print(a)

while int(a) != None:
    fhand = urllib.request.urlopen(base + a)
    for line in fhand:
        nwords = line.decode().strip()
    nwords.split(' ')
    a = nwords[24:]
    print(a)
print(nwords)
