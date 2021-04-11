class LinkedListNode:
    def __init__ (self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__ (self, head=None):
        self.head = head

    def insert_beginning (self, value):
        newNode = LinkedListNode(value, self.head)
        self.head = newNode

    def insert_end(self,value):
        newNode = LinkedListNode(value)
        
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = newNode
                break
            currentNode = currentNode.next
        
    def insert_values(self, values):
        self.head = None
        for v in values:
            self.insert_end(v)

    def delete_value (self, value):
        if self.head is None:
            print('Linked List is empty')
            return
        
        currentNode = self.head
        if currentNode.value == value:
            self.head = currentNode.next
            return

        while currentNode is not None:
            if currentNode.next.value == value:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next
        print('The value to delete is not an avenger')
        
    def delete_index(self, index):
        currentIndex = 0
        currentNode = self.head

        if self.head is None:
            print('There are not nodes on the linked list')
            return
        
        if index < 0 or index > self.get_length():
            print('Index is out of range')
            return

        if index == 0:
            self.head = currentNode.next

        currentIndex = 0
        currentNode = self.head

        while currentNode is not None:
            if index == currentIndex + 1:
                currentNode.next = currentNode.next.next
                break
            currentNode = currentNode.next
            currentIndex += 1

    def get_length(self):
        if self.head is None:
            print('Linked List is empty')
            return
        currentNode = self.head
        number_nodes = 0
        while currentNode is not None:
            number_nodes += 1
            currentNode = currentNode.next
        return number_nodes
    
    def printLinkedList (self):
        if self.head is None:
            print('There are not avengers')
            return

        currentNode = self.head
        while currentNode is not None:
            print (currentNode.value, "->", end=' ')
            currentNode = currentNode.next
        print('None')

    def reverse (self):
        currentNode = self.head
        previousNode = None
        
        while currentNode is not None:
            restNodes = currentNode.next
            # 5 | 7 | 9 | None
            currentNode.next = previousNode
            # 3 -> None | 5 -> 3 | 7 -> 5 | 9 -> 7
            previousNode = currentNode
            # 3 | 5 | 7 | 9
            currentNode = restNodes
            # 5 | 7 | 9 | None
        self.head = previousNode




avengers = LinkedList()
avengers.insert_values([3,5,7,9])
avengers.printLinkedList()
avengers.reverse()
avengers.printLinkedList()


# 3 -> 5 -> 7 -> 9 -> None
# 9 -> 7 -> 5 -> 3 -> None




