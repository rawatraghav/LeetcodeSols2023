# https://leetcode.com/problems/valid-parentheses/submissions/

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}":"{","]":"[",")":"("}
        deq = deque()
        
        for i in s:
            
            if i in "({[":
                deq.append(i)
            
            elif len(deq) == 0:
                return False
            else:
                par = deq.pop()
                if par != dic[i]:
                    return False
        return len(deq) == 0