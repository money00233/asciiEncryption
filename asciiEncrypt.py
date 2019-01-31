# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 04:36:38 2019

@author: Mani
"""

import re
import collections
def groupSplit(h):
    split = []
    split = re.findall('....',h)
    return split
def getASCII(n):
    n = list(n)
    asciiList = []
    for i in range(len(n)):
        asciiList.append(ord(n[i]))
    return asciiList
#function to get modvalue
def modASCII(n):
    modList = []
    minK = min(n)
    for i in range(len(n)):     
        modList.append(n[i]%minK)
    return modList
#function to get decimal to binary list
def getBin(n):
    binList = []
    for i in range(len(n)):
        binList.append((bin(n[i])[2:].zfill(4)))
    return binList
#funtion to rotate binary numbers
def rotBin(n,p):
    n = "".join(n)
    d = collections.deque(n)
    d.rotate(p)
    t = "".join(d)
    return t
#function to convert binary to decimal
def toDecimal(n): 
    number = n; 
    dvalue = 0;
    base = 1; 
    len1 = len(number); 
    for i in range(len1 - 1,-1,-1): 
        if (number[i] == '1'):      
            dvalue += base; 
        base = base * 2;
    return dvalue
#function to add minimum value to rotated binary numbers
def addMinKey(n,minKL,p):
    addedKey = []
    for i in range(p):
        addedKey.append(int(n[i]) + int(minKL))
    return addedKey
#function to get the final cipher text
def cipherText(n):
    check = []
    for i in range(len(n)):
        check.append(str(chr(n[i])))
    cipher = "".join(check)
    return cipher
#function to perform the encryption
def getCipher(string,key):
    shiftKey = []
    finalnumKey = []
    p = len(string)
    stringASCII = getASCII(string)
    keyASCII = getASCII(key)
    modContent = modASCII(stringASCII)
    modKey = modASCII(keyASCII)
    binKey = getBin(modKey)
    rotKey = rotBin(binKey,p)
    rotKey = groupSplit(rotKey)
    for i in range(len(rotKey)):
        shiftKey.append(toDecimal(rotKey[i]))
    minK = min(stringASCII)    
    AKey = addMinKey(shiftKey,minK,p)
    for i in range(len(AKey)):
        finalnumKey.append(int(AKey[i]) + int(modContent[i]))
    ciphertext = cipherText(finalnumKey)
    print(ciphertext)