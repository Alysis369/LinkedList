## Test class for LinkedList
import unittest
from LinkedList import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def testInsertAtIndex(self):
        ll = LinkedList()
        ll.insertAtIndex(1, 0)
        ll.insertAtIndex(2, 1)

        with self.assertRaises(IndexError):
            ll.insertAtIndex(4, 4)

        expected = [1, 2]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))

    def testRemoveAtIndex(self):
        ll = LinkedList(Node(1, Node(2, Node(3))), 3)
        ll.removeAtIndex(2)

        with self.assertRaises(IndexError):
            ll.removeAtIndex(0)

        expected = [1, 3]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))

    def testInsertAtBegin(self):
        ll = LinkedList()
        ll.insertAtBegin(1)

        expected = [1]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))

    def testInsertAtEnd(self):
        ll = LinkedList(Node(1, Node(2)), 2)
        ll.insertAtEnd(3)

        expected = [1, 2, 3]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))

    def testUpdateNode(self):
        ll = LinkedList(Node(1, Node(2, Node(3))), 3)
        ll.updateNode(4, 2)

        expected = [1, 4, 3]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))

    def testRemoveVal(self):
        ll = LinkedList(Node(1, Node(2, Node(3))), 3)
        ll.removeNode(2)

        expected = [1, 3]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))

    def testReverse(self):
        ll = LinkedList(Node(1, Node(2, Node(3))), 3)
        ll.reverse()

        expected = [3, 2, 1]

        cur = ll.head
        for val in expected:
            self.assertEqual(cur.val, val)
            cur = cur.next

        self.assertEqual(ll.size, len(expected))


if __name__ == "__main__":
    unittest.main()
