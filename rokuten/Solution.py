# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List

def solution(S):
    # write your code in Python 3.6
    vowel_set={'A','E','I','O','U'}
    pre=[]
    for s in S:
        pre.append(s)
    tmp=formAllAnagram(pre)
    res=[]
    prev=""
    print(tmp)
    for lists in tmp:
        flag=0
        prev=""
        if lists[0] in vowel_set:
            continue
        for s in lists:
            if s in vowel_set and prev!="" and prev in vowel_set or prev!="" and s not in vowel_set and prev not in vowel_set:
                flag=1
                continue
            else:
                prev=s
        if flag==0:
            res.append(lists)
    return len(res)


def formAllAnagram(chars: List[str]) -> List[List[str]]:
    res=[]

    if (len(chars)==1):
         return [chars.copy()]
    
    for i in range(len(chars)):
        c = chars.pop(0)
        anagram = formAllAnagram(chars)
        for a in anagram:
            a.append(c)
        res.extend(anagram)
        chars.append(c)
    return res

print(solution('BAAB'))