# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

import collections



def findLUSlength(S) -> int:
    # C = collections.Counter(S)
    # S = sorted(C.keys(), key = len, reverse = True)      # S = ['aba', 'cdc', 'eae']
    maxlen = -1
    flag = False
    for i in range(len(S)):
        currlen = len(S[i])
        for j in range(len(S)):
            if(i!=j and isSubstring(S[i],S[j])):
                flag = True
                break
        if(not flag):
            maxlen = max(maxlen, currlen)

    return maxlen

def isSubstring(mainstr, sub):
    if mainstr == sub: return True
    j = 0
    i = 0
    while i < len(sub) and j<len(mainstr):
        if sub[i] == mainstr[j]:
            i += 1
        j+=1
    
    return i == len(sub)



if __name__ == "__main__":
    strs = list(input().split())       # strs = aba cdc eae
    print("Result:",findLUSlength(strs))