

# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head):
            return head

        odd = head
        even = head.next
        main = head.next

        while odd.next and odd.next.next:

            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = main

        return head

