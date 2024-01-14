## Implementation of Linked List in Python
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head: Node = None):
        self.__head = Node(0)
        self.__size = 0
        # self.__set_custom_head(head)
        self.head = head

    @property
    def head(self) -> Node:
        return self.__head.next

    @head.setter
    def head(self, head: Node):
        self.__size = 0

        cur = head
        while cur:
            self.__size += 1
            cur = cur.next

        self.__head.next = head

    def insertAtIndex(self, val, index: int):
        if index > self.__size:
            raise IndexError

        cur = self.__head
        for _ in range(index):
            cur = cur.next

        cur.next = Node(val, next=cur.next)

        self.__size += 1

    def insertAtBegin(self, val):
        self.insertAtIndex(val, 0)

    def insertAtEnd(self, val):
        self.insertAtIndex(val, self.__size)

    def removeAtIndex(self, index: int):
        if index == 0 or index > self.__size:
            raise IndexError

        cur = self.__head
        for _ in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next

        self.__size -= 1

    def removeAtBegin(self):
        self.removeAtIndex(0)

    def removeAtEnd(self):
        self.removeAtIndex(self.__size)

    def updateNode(self, val, index: int):
        if index == 0 or index > self.__size:
            raise IndexError

        cur = self.__head
        for _ in range(index):
            cur = cur.next

        cur.val = val

    def removeNode(self, val):
        cur = self.__head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self.__size -= 1
                return

            cur = cur.next

        raise Exception("Val not found")

    def reverse(self):
        prev, cur = None, self.head

        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        self.head = prev

    def getNode(self, index: int) -> Node:
        if index == 0 or index > self.__size:
            raise IndexError

        cur = self.__head
        for _ in range(index):
            cur = cur.next

        return cur

    def insertNodeToEnd(self, node: Node):
        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = node

        self.__size += 1

    def containsLoop(self) -> bool:
        slow, fast = self.head, self.head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True

        return False

    def getLoopNode(self) -> Node:
        if not self.containsLoop():
            raise Exception("No loop is detected on LinkedList")

        slow = fast = node = self.__head

        while True:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                break

        while node is not slow:
            node, slow = node.next, slow.next

        return node

    def reverseFirstN(self, n: int):
        if n == 0 or n > self.__size:
            raise IndexError

        right = self.head
        for _ in range(n):
            right = right.next

        prev, left = right, self.head

        while left is not right:
            left.next, left, prev = prev, left.next, left

        self.head = prev

    def __len__(self):
        return self.__size

    def __iter__(self):
        # cur = self.head
        # while cur:
        #     yield cur
        #     cur = cur.next

        cur = self.__head
        for _ in range(len(self)):
            cur = cur.next
            yield cur

    def __str__(self):
        node_str = ''
        for node in self:
            node_str += f"\n[{node.val}, next={node.next}],"
        node_str = node_str[0:len(node_str) - 1]

        return f"LinkedList({node_str})"
