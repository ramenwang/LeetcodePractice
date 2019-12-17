# convert-binary-number-in-a-linked-list-to-integer
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        base2string = ''
        while head:
            base2string = base2string + str(head.val)
            head = head.next
        print(base2string)
        return int(base2string, 2)
