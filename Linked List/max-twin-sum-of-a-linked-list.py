
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        ptr = head
        res = []
        n = 0

        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
            n += 1
        
        pair = float('-inf')

        for i in range(n//2):
            pair = max(pair, res[i]+res[-1-i])

        return pair