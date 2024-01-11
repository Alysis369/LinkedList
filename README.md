# LinkedList
A simple LinkedList implementation on Python

# Intuition
Initial simple implementation of linkedlist. 

Written with an implementation time limit <30 mins in mind including limited TestCases.

### Added extra methods:
- reverseFirstN()
- getNode()
- insertNodeToEnd()
- containsLoop()
- getLoopNode()


### Notes:
- Included dummy head, to increase code cleanliness on empty/begin insertion and deletion
- Implemented insert/remove at begin/end through Index to save on implementation time


# Implementation
## Setup
```python
import LinkedList

ll = LinkedList()
```
## Methods
- [insertAtIndex()](#insertAtIndex)
- [insertAtBegin()](#insertAtBegin)
- [insertAtEnd()](#insertAtEnd)
- [removeAtIndex()](#removeAtIndex)
- [removeAtBegin()](#removeAtBegin)
- [removeAtEnd()](#removeAtEnd)
- [updateNode()](#updateNode)
- [removeNode()](#removeNode)
- [reverse()](#reverse)
- [reverseFirstN()](#reversefirstn)
- [getNode()](#getnode)
- [insertNodeToEnd()](#insertnodetoend)
- [containsLoop()](#containsloop)
- [getLoopNode()](#getloopnode)

---------------------------------
### insertAtIndex
_Time Complexity_: O(n) | 
_params_: val, index: int
_Notes_: Index 0 refers to the beginning of linked list, Index 1 refers to inserting after FirstNode etc.
```python
ll = LinkedList()
ll.insertAtIndex(val=1, index=0)
```

### insertAtBegin
_Time Complexity_: O(1) | 
_params_: val
```python
ll = LinkedList()
ll.insertAtBegin(val=1)
```

### insertAtEnd
_Time Complexity_: O(n) | 
_params_: val
```python
ll = LinkedList()
ll.insertAtEnd(val=1)
```

### removeAtIndex
_Time Complexity_: O(n) | 
_params_: index: int
_Notes_: Index 1 refer to the first node, 2 to the second etc.
```python
ll = LinkedList()
ll.removeAtIndex(1)
```

### removeAtBegin
_Time Complexity_: O(1) | 
_params_: 
```python
ll = LinkedList()
ll.removeAtBegin()
```

### removeAtEnd
_Time Complexity_: O(n) | 
_params_: 
```python
ll = LinkedList()
ll.removeAtEnd()
```

### updateNode
_Time Complexity_: O(n) | 
_params_: val, index: int
```python
ll = LinkedList()
ll.insertAtBegin(1) # ll should be [1]
ll.insertAtBegin(2) # ll should be [1,2]
ll.updateNode(val=2, index=1) # ll should be [2,2]
```

### removeNode
_Time Complexity_: O(n) | 
_params_: val
```python
ll = LinkedList()
ll.insertAtBegin(1) # ll should be [1]
ll.insertAtBegin(2) # ll should be [1,2]
ll.removeNode(val=1) # ll should be [2]
```

### reverse
Reverses the LinkedList
_Time Complexity_: O(n) | 
_params_: 
```python
ll = LinkedList()
ll.reverse()
```

### reverseFirstN
Reverses only the first _n_ of the LinkedList
_Time Complexity_: O(n) | 
_params_: n: int
```python
# ll is LinkedList of [1,2,3,4]
ll.reverseFirstN(2) # ll is now [2,1,3,4]
```

### getNode
Get the node from an index
_Time Complexity_: O(n) | 
_params_: index: int
_return_: node: Node
```python
# ll is LinkedList of [1,2,3,4]
node = ll.getNode(2) # node is node with val 2
```

### insertNodeToEnd
Inserts node to end of LinkedList
_Time Complexity_: O(n) | 
_params_: node: Node
```python
# ll is LinkedList of [1,2,3,4]
node = Node(5)
ll.insertNodeToEnd(node) # ll is [1,2,3,4,5]
```

### containsLoop
Checks if LinkedList contains a loop
_Time Complexity_: O(n) | 
_params_: 
_return_: bool
```python
# ll is LinkedList of [1->2->3->4->5->2]
ll.containsLoop() # returns True
```

### getLoopNode
Gets the starting loop node if contains loop
_Time Complexity_: O(n) | 
_params_: 
_return_: Node
```python
# ll is LinkedList of [1->2->3->4->5->2]
ll.getLoopNode() # returns node with val 2
```