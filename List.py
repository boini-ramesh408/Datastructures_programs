class Node:
    def __init__(self, data):
        # It creates the node with data and address fields
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # It adds the node with given data at the end of the list
    def addElement(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
        return

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    # It inserts data with given node at particular location
    def insert(self, previous_node, data):
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    # Delete node with given data
    def remove(self, data):  #
        temp = self.head
        prev = temp
        if temp.data == data:
            self.head = temp.next
            temp = None
        # return

        prev = None
        while temp.data != data:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
        return

    # Count number nodes in linked list
    def size(self):
        x = 0
        temp = self.head
        while temp:
            x = x + 1
            temp = temp.next
        print("size of list is:", x)
        # return x

    # STACK UTILITY
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def pop(self):
        data = None
        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        data = temp.data
        return data
