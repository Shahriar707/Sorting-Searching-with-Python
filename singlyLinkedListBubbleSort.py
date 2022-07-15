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

    def selection_sort(self):
        n = self.head
        while n is not None:
            minimum = n
            x = n.next
            while x is not None:
                if minimum.element > x.element:
                    minimum = x
                x = x.next

            y = n.element
            n.element = minimum.element
            minimum.element = y
            n = n.next

        n = self.head
        while n is not None:
            print(n.element, end=" ")
            n = n.next

a = MyList([30,20,15,23,-2,56,-5])
a.selection_sort()