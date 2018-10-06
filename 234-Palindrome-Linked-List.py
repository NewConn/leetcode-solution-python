# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        pCount = self.head
        count = 0
        while(pCount != None):
            count = count + 1
            pCount = pCount.next
        
        pHead1 = head
        pHead2 = head
        pNew = None
        for i in range(count // 2):
            pHead2 = pHead1.next
            pHead1.next = pNew
            pNew = pHead1
            pHead1 = pHead2
        
        if count % 2 == 1:
            pHead2 = pHead2.next

        while(pHead2 != None and pNew != None):
            if pHead2.val != pNew.val:
                return False
            pHead2 = pHead2.next
            pNew = pNew.next
        return True