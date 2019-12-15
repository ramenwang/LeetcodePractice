# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def listNodeToInt(node):
            '''
            function to read NodeList as int
            '''
            result = ""
            while node:
                result = str(node.val) + result # read from back to front
                node = node.next

            return int(result)

        def intListToListNode(x: int):
            '''
            function to convert int to NodeList
            '''
            xList = list(str(x))
            xList = map(int, xList[::-1]) # change the order from back to front
            dummyRoot = ListNode(0)
            ptr = dummyRoot
            for i in xList:
                ptr.next = ListNode(i)
                ptr = ptr.next
            ptr = dummyRoot.next
            return ptr

        x = listNodeToInt(l1) + listNodeToInt(l2)

        return intListToListNode(x)
