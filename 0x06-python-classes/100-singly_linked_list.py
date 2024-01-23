#!/usr/bin/python3


"""Defines a class Node."""


class Node:
    """Represents a Node."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head is None:
            self.__head = node
        elif node.data < self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            node.next_node = tmp.next_node
            tmp.next_node = node

    def __str__(self):
        data = []
        temp = self.__head
        while temp is not None:
            data.append(temp.data)
            temp = temp.next_node
        return '\n'.join(map(str, data))


'''
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
'''
