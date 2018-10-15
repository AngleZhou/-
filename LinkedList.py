class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




class LinkedList:
    def __init__(self):
        self.head = None
        self.guard = Node(None)
        self.current = self.guard

    def printlist(self, node):
        # node = self.guard.next
        while node is not None:
            print(node.val)
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
        node = Node(self.head.val)
        list.current = node
        node1 = self.head.next
        while node1 is not None:
            node = Node(node1.val)
            node.next = list.current
            list.current = node
            node1 = node1.next
        list.head = list.current
        list.guard.next = list.head
        return list

    @classmethod
    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node1 = l1
        node2 = l2
        node = Node(0)
        head = node
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        if node1 is not None:
            node.next = node1
        elif node2 is not None:
            node.next = node2
        return head.next

    @classmethod
    def mergeRecursive(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeRecursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeRecursive(l1, l2.next)
            return l2


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

    def removeNthFromEnd(self, head, n):
        if head is None or head.next is None:
            return None

        node = head
        count = 0

        while node is not None:
            count += 1
            node = node.next
        if n > count:
            return head
        node = head
        index = 0
        while index < count-1-n:
            node = node.next
            index += 1
        node.next = node.next.next
        return head

    def removeNthFromEndArray(self, head, n):
        if head is None:
            return head
        node = head
        nodeArr = []

        while node is not None:
            nodeArr.append(node)
            node = node.next
        node = nodeArr[len(nodeArr) - n - 1]
        node.next = node.next.next
        return head

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
    l1 = LinkedList()
    l1.add(1)
    l1.add(2)
    l1.add(4)
    l1.head = l1.guard.next
    l1.printlist(l1.head)
    print('-----------')
    l2 = LinkedList()
    l2.add(1)
    l2.add(3)
    l2.add(4)
    l2.head = l2.guard.next
    l2.printlist(l2.head)
    print('-----------')
    # head = LinkedList.merge(l1.guard.next, l2.guard.next)
    head = LinkedList.mergeRecursive(l1.guard.next, l2.guard.next)
    list = LinkedList()
    list.guard.next = head
    list.printlist(head)
    print('-----------')
    list.removeNthFromEndArray(list.guard.next, 2)
    list.printlist(head)
    # node = list.mid()
    # print(node.val)
    # list2 = list.reverseList()
    # list2.printlist()
    # print('-----------')
    # node = list.deleteReverseN(6)
    # print(node.val)
    # print('-----------')
    # list.gettail()
    # list.tail.next = list.head
    # print(list.circleDetect())



