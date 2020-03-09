class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        newnode = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode

    def printlist(self):
        current = self.head
        while current is not None:
            print('{}{}'.format(current.data,'->'),end = '')
            current = current.next


    def length(self):
        current = self.head
        counter = 0
        while current is not None:
            counter+=1
            current = current.next
        return counter


    def middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def returnhead(self):
        return self.head
    

# singly = LinkedList()
# singly.insert(1)
# singly.insert(2)
# singly.insert(3)
# singly.insert(4)
# singly.insert(5)
# singly.insert(6)
# singly.insert(7)
# singly.printlist()       
# print() 
# print(ll.printlist())
# print(singly.middle())