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
    while curr is not None:
        nextcurr = curr.next
        curr.next = prev
        prev = curr
        curr = nextcurr
    return prev


def insertinsorted(head,data):
        current = head
        newnode = SinglyLL.Node(data)
        while current.data < data:
            prev = current 
            current = current.next
        prev.next = newnode
        newnode.next = current



ll = SinglyLL.LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(9)
ll.insert(11)
print(ll.printlist())
insertinsorted(ll.returnhead(),7)
print(ll.printlist())


# ll = reverse(ll)
    