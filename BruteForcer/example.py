from Helpers import *
from Brute import *

FLAG="navy{:pepe-cry:}"

def checkChar(i,ch):
    if FLAG[i]==ch:
        return True
    
    return False

def compareChar(i,ch):
    if ord(FLAG[i])>ord(ch):
        return 1

    elif ord(FLAG[i])<ord(ch):
        return -1

    else:
        return 0

def checkLen(l):
    if len(FLAG)==l:
        return True
    
    return False

def compareLen(l):
    if len(FLAG)>l:
        return 1
    elif len(FLAG)<l:
        return -1
    else:
        return 0

def Main():
    options=Helpers.getOptions()
    options['checkChar']=checkChar
    options['len']=10
    options['flag']='navy'
    brute = Brute(**options)
    flag=brute.run(5)

    print(flag)
    options=Helpers.getOptions()
    options['checkChar']=checkChar
    options['checkLen']=checkLen
    brute = Brute(**options)
    flag=brute.run(5)
    print(flag)

    options=Helpers.getOptions()
    options['compareChar']=compareChar
    options['compareLen']=compareLen
    brute = Brute(**options)
    flag=brute.run(5)
    print(flag)

    options=Helpers.getOptions()
    options['compareChar']=compareChar
    options['compareLen']=compareLen
    options['maxLen']=5
    brute = Brute(**options)
    flag=brute.run(5)
    print(flag)

Main()
