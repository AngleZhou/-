class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None




class LinkedList:
    def __init__(self):
        self.head = None
        self.guard = ListNode(None)
        self.current = self.guard

    def printlist(self, node):
        # node = self.guard.next
        while node is not None:
            print(node.val)
            node = node.next

    def add(self, data):
        newNode = ListNode(data)
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

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        node1 = ListNode(head.val)
        while head.next:
            node2 = ListNode(head.next.val)
            node2.next = node1
            node1 = node2
            head = head.next
        return node1

    def reverseList2(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return cur

    def reverseR(self, head):
        (newHead, pre) = self.reverseListRecursive(head)
        return newHead

    def reverseListRecursive(self, head):
        if head is None or head.next is None:
            return head, head
        newHead, node = self.reverseListRecursive(head.next)
        head.next = None
        node.next = head
        return newHead, head

    @classmethod
    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node1 = l1
        node2 = l2
        node = ListNode(0)
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


    def mid(self, head):
        if head is None:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if not fast.next:
            return slow
        return slow.next

    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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

    def has_cycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
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
    print('------ merge -----')
    head = LinkedList.mergeRecursive(l1.head, l2.head)
    list = LinkedList()
    list.guard.next = head
    list.printlist(head)
    print('-----------')
    print('----- has_cycle ------')
    # list.gettail()
    # list.tail.next = head
    print(list.has_cycle(head))
    print('-----------')
    print('----- removeNthFromEnd ------')
    # l1.removeNthFromEnd(None, 0)
    # l1.printlist(l1)
    print('-----------')
    print('------ mid -----')
    node = list.mid(head)
    print(node.val)
    print('-----------')
    print('------ reverse -----')
    l4 = LinkedList()
    l4.add(1)
    l4.add(2)
    l4.add(4)
    l4.head = l4.guard.next
    l4.printlist(l4.head)
    print('--')
    # ret = l4.reverseR(l4.head)
    ret = l4.reverseList(l4.head)
    l4.printlist(ret)

    # node = list.deleteReverseN(6)
    # print(node.val)
    # print('-----------')
    # list.gettail()
    # list.tail.next = list.head
    # print(list.circleDetect())



