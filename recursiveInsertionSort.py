class Node:
    def __init__(self, e, n=None):
        self.element = e
        self.next = n

class MyList:

    def __init__(self, a):
        self.head = None
        tail = None
        for i in a:
            n = Node(i)
            if self.head is None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n

    def bubble_sort(self):
        finish = None
        while finish != self.head.next:
            x = self.head
            while x.next != finish:
                y = x.next
                if x.element > y.element:
                    x.element, y.element = y.element, x.element
                x = x.next
            finish = x

        n = self.head
        while n is not None:
            print(n.element, end=" ")
            n = n.next


list1 = MyList([1,2,5,3,8])
list1.bubble_sort()
print("\n")
list2 = MyList([30,20,15,23,-2,56,-5])
list2.bubble_sort()

