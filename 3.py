import re, string
fh = open('tt.txt') # the source code of html
pw = ''
for line in fh:
    y = re.findall('[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}',line)
    if len(y) > 0:
#        print(y)
        for a in y:
            pw += a
print(pw) # print password
