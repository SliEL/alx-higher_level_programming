#!/usr/bin/python3

class Node:
    """Represent a Node in the linked list class"""

    def __init__(self, data, next_node=None):
        """Initialize the node.

        Args:
            data (int): value of the node
            next_node (Node): next node in the linked list
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        "Set and Get the value of the node"
        return (self.__data)
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """get and set next node"""
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None
    
    def sorted_insert(self, value):
        """Inserts a new Node to the Singly L_list.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new
        
    def __str__(self):
        """Defines the print representation of the Singly L_List."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))



