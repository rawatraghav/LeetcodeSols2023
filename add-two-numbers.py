# https://leetcode.com/problems/add-two-numbers/solution/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode(0)
        result_ptr = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            out = (val1 + val2 + carry)%10
            carry = (val1 + val2 + carry)//10
            
            result_ptr.next = ListNode(out)
            result_ptr = result_ptr.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next