# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow now points to the middle of the linked list

        # Now we should create another linkedlist that reverses the second half of the linked list

        curr = slow.next
        prev = slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # curr1 = 0, 1, 2
        # curr = None, 6, 5, 4, 3
        curr1 = head
        second = prev
        while second:
            tmp1, tmp2 = curr1.next, second.next
            curr1.next = second
            second.next = tmp1
            curr1, second = tmp1, tmp2
        
            

