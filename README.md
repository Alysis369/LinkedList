# LinkedList

A simple LinkedList implementation on Python

# Description

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

---------------------------------

# Documentation

## Constructor
- [LinkedList()](#LinkedList)

## Attributes

- **head**: _The first node of the LinkedList_

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

## Referenced Classes

- [Node](#Node)

---------------------------------

### LinkedList()

Constructor for LinkedList class.

```python
class LinkedList(node=None)
```

###### Time Complexity

O(n)

###### Parameters

- **node : Node**
    - Node representing the head of the constructed LinkedList. If existing LinkedList data structure is to be imported
      to this data structure, pass in the head of existing head of LinkedList here.

###### Returns

- **LinkedList**
    - A generated LinkedList object.

###### Examples

```
>>> existing_ll = Node(1, Node(2, Node(3)))
>>> ll = LinkedList(existing_ll)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B1210BE350>],
[2, next=<LinkedList.Node object at 0x000001B1210BC790>],
[3, next=None])
```

--------

### insertAtIndex()

Insert a value in the LinkedList in a specific index

```python
LinkedList.insertAtIndex(val, index)
```

###### Time Complexity

O(n)

###### Parameters

- **val: Any**
    - Any datastructure to be inserted into the LinkedList node
- **index: int**
    - Indicates which index in the LinkedList the node should be inserted. Index 0 refers to the beginning of linked
      list, Index 1 refers to inserting after FirstNode etc.

###### Examples

```
>>> ll = LinkedList()
>>> ll.insertAtIndex("a", 0)
>>> print(ll)
LinkedList(
[a, next=None])
```

Inserting a value in the 0 index position will insert it at the head of the LinkedList.

```
>>> ll.insertAtIndex("b", 1)
>>> print(ll)
LinkedList(
[a, next=<LinkedList.Node object at 0x000001B122140090>],
[b, next=None])

>>> ll.insertAtIndex("c", 1)
LinkedList(
[a, next=<LinkedList.Node object at 0x000001B122140090>],
[c, next=<LinkedList.Node object at 0x000001B122140550>],
[b, next=None])
```

Inserting a value will place the new node right after the specified index parameter.

------

### insertAtBegin()

Insert a value into the beginning of the LinkedList.

```python
LinkedList.insertAtBegin(val)
```

###### Time Complexity

O(1)

###### Parameters

- **val: Any**
    - Any datastructure to be inserted into the LinkedList node

###### Examples

```
>>> ll = LinkedList()
>>> ll.insertAtBegin(1)
>>> print(ll)
LinkedList(
[1, next=None])

>>> ll.insertAtBegin(2)
>>> print(ll)
LinkedList(
[2, next=<LinkedList.Node object at 0x000001B12109E210>],
[1, next=None])
```

------

### insertAtEnd()

Insert a value into the end of the LinkedList.

```python
LinkedList.insertAtEnd(val)
```

###### Time Complexity

O(n)

###### Parameters

- **val: Any**
    - Any datastructure to be inserted into the LinkedList node

###### Examples

```
>>> ll = LinkedList()
>>> ll.insertAtEnd(1)
>>> print(ll)
LinkedList(
[1, next=None])

>>> ll.insertAtEnd(2)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B12109E210>],
[2, next=None])

```

------

### removeAtIndex()

Remove a node at a specified index.

```python
LinkedList.removeAtIndex(index)
```

###### Time Complexity

O(n)

###### Parameters

- **index: int**
    - Index value of the node to be removed. ex. index=1 refers to the head, index=2 is the second node, etc.

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3)))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>> ll.removeAtIndex(2)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])
```

-------

### removeAtBegin()

Remove a node in the beginning of the LinkedList.
```python
LinkedList.removeAtBegin()
```

###### Time Complexity

O(1)

###### Parameters

NA

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3)))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> ll.removeAtBegin()
>>> print(ll) 
LinkedList(
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])
```

-------

### removeAtEnd()
Remove the node at the end of the LinkedList.
```python
LinkedList.removeAtEnd()
```

###### Time Complexity

O(n)

###### Parameters

NA

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3)))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> ll.removeAtEnd()
>>> print(ll) 
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[2, next=None])
```

-----------

### updateNode()
Change the value of a node in a specified index.
```python
LinkedList.updateNode(val, index)
```

###### Time Complexity

O(n)

###### Parameters

- **val: Any**
    - Any datastructure to be inserted into the LinkedList node
- **index: int**
    - Index value of the node to be removed. ex. index=1 refers to the head, index=2 is the second node, etc.

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3)))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> ll.updateNode(4, 2)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[4, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])
```

--------

### removeNode()
Remove the node with a specified value.
```python
LinkedList.removeNode(val)
```

###### Time Complexity

O(n)

###### Parameters

- **val: Any**
    - Value of the node to be deleted

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3)))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> ll.removeNode(2)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122143B90>],
[3, next=None])
```

--------

### reverse()
Reverse the LinkedList.
```python
LinkedList.reverse()
```

###### Time Complexity

O(n)

###### Parameters

NA

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3))))
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> ll.reverse()
>>> print(ll)
LinkedList(
[3, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122143B10>],
[1, next=None])
```

------

### reverseFirstN
Reverse only the first _n_ node in the LinkedList.
```python
LinkedList.reverseFirstN(n)
```

###### Time Complexity

O(n)

###### Parameters

- **n: int**
    - The number of nodes from the start to reverse.

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3, Node(4))))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=<LinkedList.Node object at 0x000001B122149290>],
[4, next=None])

>>> ll.reverseFirstN(2)
>>> print(ll)
LinkedList(
[2, next=<LinkedList.Node object at 0x000001B122143B10>],
[1, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=<LinkedList.Node object at 0x000001B122149290>],
[4, next=None])
```

-----

### getNode()
Get the node in a specified index from the LinkedList.
```python
LinkedList.getNode(index)
```

###### Time Complexity

O(n)

###### Parameters

- **index: int**
    - Index value of the node to be removed. ex. index=1 refers to the head, index=2 is the second node, etc.

###### Returns
- **node: Node**
  - The node that is in the specified index from the LinkedList.
###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3))))
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> ll.getNode(2)
<LinkedList.Node at 0x1b122148850>
```

-------

### insertNodeToEnd()
Insert a node to the end of the LinkedList.
```python
LinkedList.insertNodeToEnd(node)
```

###### Time Complexity

O(n)

###### Parameters

- **node: Node**
    - Node datastructure to be inserted in the tail

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3, Node(4)))))
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> new_node = Node(4)
>>> ll.insertNodeToEnd(new_node)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=<LinkedList.Node object at 0x000001B122149290>],
[4, next=None])
```

Inserting an empty Node to the end of the LinkedList

```
>>> ll = LinkedList(Node(1, Node(2, Node(3)))) 
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=None])

>>> second_node = ll.getNode(2)
>>> second_node
<LinkedList.Node at 0x1b122148850>

>>> new_node = Node(4, next=second_node)
>>> ll.insertNodeToEnd(new_node)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=<LinkedList.Node object at 0x000001B122149290>],
[4, next=<LinkedList.Node object at 0x000001B122148850>])
```

Creating a cyclic LinkedList using getNode() and insertNodeToEnd()

-------

### containsLoop()
Checks if the LinkedList contains a loop (cyclic).
```python
LinkedList.containsLoop()
```

###### Time Complexity

O(n)

###### Parameters

NA

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3))))
>>> second_node = ll.getNode(2)
>>> new_node = Node(4, next=second_node)
>>> ll.insertNodeToEnd(new_node)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x000001B122148850>],
[2, next=<LinkedList.Node object at 0x000001B122142F50>],
[3, next=<LinkedList.Node object at 0x000001B122149290>],
[4, next=<LinkedList.Node object at 0x000001B122148850>])

>>> ll.containsLoop()
True
```

-----

### getLoopNode()
Returns the node in which the loop occurs if the LinkedList is cyclic.
```python
LinkedList.getLoopNode()
```

###### Time Complexity

O(n)

###### Parameters

NA

###### Returns
- **node: Node**
  - The node in which the loop occurs

###### Examples

```
>>> ll = LinkedList(Node(1, Node(2, Node(3))))
>>> second_node = ll.getNode(2)
>>> new_node = Node(4, next=second_node)
>>> ll.insertNodeToEnd(new_node)
>>> print(ll)
LinkedList(
[1, next=<LinkedList.Node object at 0x00000219434F15D0>],
[2, next=<LinkedList.Node object at 0x00000219434F1510>],
[3, next=<LinkedList.Node object at 0x00000219434F1E10>],
[4, next=<LinkedList.Node object at 0x00000219434F15D0>])

>>> ll.getLoopNode()
<LinkedList.Node at 0x219434f15d0>
```
------

### Node
Node datastructure.
```python
Node(val=None, next=None)
```


###### Parameters

- **val: Any**
  - Any value to be inserted to the node
- **next: Node**
  - Pointer to the next node from the current node

###### Returns
- **node: Node**
  - A node data structure
