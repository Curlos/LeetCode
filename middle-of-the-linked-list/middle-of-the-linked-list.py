# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        listLen = 0
        node = head
        
        while node:
            listLen += 1
            node = node.next
        
        node = head
        midIndex = listLen // 2
        currIndex = 0
        
        while currIndex < midIndex:
            node = node.next
            currIndex += 1
        
        return node