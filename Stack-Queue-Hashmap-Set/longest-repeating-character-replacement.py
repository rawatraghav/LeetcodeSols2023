
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

import collections

# My solution , also the most optimized (O(n))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        Sliding window and hashmap at its best. 
        """
        
        counter = collections.defaultdict(int)
        maxlen = 0
        maxcount = 0
        left = 0

        for right in range(len(s)):
            
            counter[s[right]] += 1
            maxcount = max(counter.values())
            
            if right-left+1 - maxcount > k:  # This condition checks the number of other characters 
                                             # ,than the max occuring, are under 'k'           
                counter[s[left]] -= 1
                left += 1
            
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
                
                
            