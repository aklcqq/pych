import urllib.request, urllib.parse, urllib.error
import re, string
counts = dict()
fhand = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') # grab html source
b = ' '
for line in fhand:
    words = line.decode().strip()
    for word in words:
        if word not in string.ascii_letters: continue # clear punctuation
        b += word
#    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(b) # the password is in the last line / the last word
#print(counts)

t = list(counts.items())
l = list()
for a, b in t:
    l.append((b,a))
l.sort()
#print(l)
