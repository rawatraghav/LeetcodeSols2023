
# https://leetcode.com/problems/longest-repeating-character-replacement/description/


# My solution , also the most optimized (O(n))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = collections.defaultdict(int)
        maxlen = 0
        maxcount = 0
        left = 0

        for right in range(len(s)):
            
            counter[s[right]] += 1
            maxcount = max(counter.values())
            
            if right-left+1 - maxcount > k:
                counter[s[left]] -= 1
                left += 1
            
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
                
                
            