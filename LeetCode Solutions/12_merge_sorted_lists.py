class ListNode():
    def __init__ (self, val, next = None):
        self.val = val
        self.next = next
def mergeTwoLists(l1, l2):
    head = tail = ListNode(-1)
    
    while l1 and l2:
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next

    if l1: tail.next = l1
    if l2: tail.next = l2

    return head.next

if __name__ == '__main__':

    l1n1 = ListNode(1)
    l1n2 = ListNode(2)
    l1n3 = ListNode(4)

    l1n1.next = l1n2
    l1n2.next = l1n3

    l2n1 = ListNode(1)
    l2n2 = ListNode(3)
    l2n3 = ListNode(4)

    l2n1.next = l2n2
    l2n2.next = l2n3

    resultado = mergeTwoLists(l1n1, l2n1)
    
    while resultado:
        print(resultado.val)
        resultado = resultado.next