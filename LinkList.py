class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.guard = Node(None)
        self.head = self.guard.next
        self.current = self.guard

    def printlist(self):
        node = self.guard.next
        while node is not None:
            print(node.value)
            node = node.next

    def add(self, data):
        newNode = Node(data)
        self.current.next = newNode
        self.current = newNode

    def gettail(self):
        self.head = self.guard.next
        node = self.head
        while node.next is not None:
            node = node.next
        self.tail = node

    def reverse(self):
        node1 = self.guard
        self.current = node1.next
        self.guard.next = None
        self.tail = self.current
        while self.current is not None:
            node2 = self.current
            self.current = node2.next
            node2.next = node1
            node1 = node2
        self.guard.next = node1
        self.head = node1
        self.tail.next = None

    def reverseList(self):
        list = LinkedList()
        self.head = self.guard.next
        if self.head is None:
            return list
        node = Node(self.head.value)
        list.current = node
        node1 = self.head.next
        while node1 is not None:
            node = Node(node1.value)
            node.next = list.current
            list.current = node
            node1 = node1.next
        list.head = list.current
        list.guard.next = list.head
        return list

    @classmethod
    def merge(self, list1, list2):
        list1.head = list1.guard.next
        list2.head = list2.guard.next
        node1 = list1.head
        node2 = list2.head
        list = LinkedList()
        list.current = list.guard
        while node1 is not None and node2 is not None:
            if node1.value < node2.value:
                list.current.next = node1
                node1 = node1.next
            else:
                list.current.next = node2
                node2 = node2.next
            list.current = list.current.next
        if node1 is not None:
            list.current.next = node1
        elif node2 is not None:
            list.current.next = node2
        return list

    def mid(self):
        self.head = self.guard.next
        if self.head is None:
            return Node(0)
        fast = self.head
        slow = self.head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def deleteReverseN(self, n):
        node = self.guard
        count = 0
        while node.next is not None:
            count += 1
            node = node.next
        if n > count:
            return Node(0)
        node = self.guard
        index = 0
        while index < count-1-n:
            node = node.next
            index += 1
        delete = node.next
        node.next = node.next.next
        return delete

    def circleDetect(self):
        self.head = self.guard.next
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False


if __name__ == '__main__':
    list1 = LinkedList()
    list1.add(1)
    list1.add(3)
    list1.add(5)
    list1.printlist()
    print('-----------')
    list2 = LinkedList()
    list2.add(2)
    list2.add(4)
    list2.add(7)
    list2.printlist()
    print('-----------')
    list = LinkedList.merge(list1, list2)
    list.printlist()
    print('-----------')
    # node = list.mid()
    # print(node.value)
    # list2 = list.reverseList()
    # list2.printlist()
    # print('-----------')
    # node = list.deleteReverseN(6)
    # print(node.value)
    print('-----------')
    list.gettail()
    list.tail.next = list.head
    print(list.circleDetect())



