# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        count = 0
        for char in strs[0]:
            for string in strs[1:]:
                if len(string) < count+1:
                    return strs[0][:count]
                elif string[count] != char:
                    return strs[0][:count]
            count += 1
            
        return strs[0][:count]
                    