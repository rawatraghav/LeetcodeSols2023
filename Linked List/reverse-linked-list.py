

# https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        prev = None
        curr = head

        while curr:
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        