epicDict = {'jack':5,'bill':14,'kat':3,'jess':33,'Alex':4}
def sortBykey():
    sortedBykeyDict = sorted(epicDict.items(), key = lambda t: t[0])
    print sortedBykeyDict

def sortByvalue():
    sortedByvalue = sorted(epicDict.items(),key = lambda t:t[1])
    print sortedByvalue
sortedByvalue()