# https://leetcode.com/problems/is-subsequence/description/

# https://leetcode.com/problems/is-subsequence/submissions/

# Best Solution
# https://leetcode.com/problems/is-subsequence/solutions/4074367/93-76-two-pointers-dp/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for char in s:
            if char in t:
                t = t[t.index(char)+1:]
            else:
                return False
            
        return True