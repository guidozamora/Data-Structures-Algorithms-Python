class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                break
            current_node = current_node.next_node

    def print_list(self):
        if self.head is None:
            print('Linked list is empty')
            return
        current_node = self.head
        while True:
            print(current_node.value, '->', end=" ")

            if current_node.next_node is None:
                print('None')
                break
            current_node = current_node.next_node


if __name__=='__main__':

    ll = LinkedList()                
    ll.print_list()
    ll.insert_node('Iron Man')
    ll.print_list()
    ll.insert_node('Hulk')
    ll.print_list()
    ll.insert_node('SpiderMan')
    ll.print_list()


