# leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swap(self, prev: ListNode, current: ListNode, nextNode: ListNode):
        if(current == None or nextNode == None):
            return
        if(prev != None):
            prev.next = nextNode
            
        #swap logic
        current.next = nextNode.next
        nextNode.next = current
        current, nextNode = nextNode, current
        
        return (prev, current, nextNode)

            
    def swapPairs_(self, prev: ListNode, head: ListNode):
        if(head != None and head.next != None):
            prev, current, nextNode = self.swap(prev, head, head.next)
            self.swapPairs_(nextNode, nextNode.next)
        
    def swapPairs(self, head: ListNode) -> ListNode:
        #edge cases
        if(head == None):
            return 
        if(head.next == None):
            return head
            
        temp = head.next
        self.swapPairs_(None, head)
        return temp
        
