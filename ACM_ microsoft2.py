asmDict = dict(zip('abcdefghijklmnopqrstuvwxyz', range(0, 26)))
acapDict = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(0, 26)))
capslist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
smlist = 'abcdefghijklmnopqrstuvwxyz'

def main():
    mainstr = input().strip()
    key = mainstr[mainstr.index('|')+1:]
    keyval = [acapDict[i] for i in key]
    mainstr = mainstr[:mainstr.index('|')]
    mainlen = len(mainstr)
    finalstr = ''
    keyval2 = []
    j = 0
    for i in range(mainlen):
        if (i%len(keyval)==0):
            j=0
        keyval2.append(keyval[j])
        j+=1
        k = 0
    for i in range(mainlen):
        if mainstr[i] in capslist:
            m = acapDict[mainstr[i]] + keyval2[k]
            finalstr+=capslist[m%26]
            k+=1
        elif mainstr[i] in smlist:
            m = asmDict[mainstr[i]] + keyval2[k]
            finalstr+=smlist[m%26]
            k+=1
        else:
            finalstr+=mainstr[i]
    return finalstr

print(main())
