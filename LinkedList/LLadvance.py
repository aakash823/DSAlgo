import SinglyLL


def findmid(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data


def reverse(head):
    prev = None
    curr = head
    nextcurr = None
    while curr is not None:
        nextcurr = curr.next
        curr.next = prev
        prev = curr
        curr = nextcurr
    head = prev

def insertinsorted(head,data):
        current = head
        newnode = SinglyLL.Node(data)
        while current.data < data:
            prev = current 
            current = current.next
        prev.next = newnode
        newnode.next = current

def sortlinkedlist(head):
        current = head
        nextnode = head.next
        while current is not None:
            nextnode = head
            while nextnode.next is not None:
                if nextnode.data > nextnode.next.data:
                    nextnode.data , nextnode.next.data = nextnode.next.data, nextnode.data
                nextnode = nextnode.next
            current = current.next


ll = SinglyLL.LinkedList()
ll.insert(4)
ll.insert(5)
ll.insert(2)
ll.insert(2)
ll.insert(7)
ll.insert(6)
print(ll.printlist())
sortlinkedlist(ll.returnhead())
insertinsorted(ll.returnhead(),3)
print(ll.printlist())


    