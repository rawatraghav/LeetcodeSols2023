
# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counter = {}

        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        return len(counter.values()) == len(set(counter.values()))