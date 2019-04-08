atoz = 'abcdefghijklmnopqrstuvwxyz'
ctob = 'cdefghijklmnopqrstuvwxyzab'
def castpasswd(c):
    return ctob[int(atoz.find(c))]
print(castpasswd('k'))


hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
b = ''
for a in hint:
    if a in atoz:
        b = b + castpasswd(a)
    else:
        b = b + a
print(b)
