
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

# My best solution 
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        counter1 = collections.Counter(word1)
        counter2 = collections.Counter(word2)

        chars_check = len(counter1.keys() - counter2.keys()) == 0
        values_check = sorted(counter1.values()) == sorted(counter2.values())

        return chars_check and values_check