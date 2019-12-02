

class Node:
    def __init__(self, data):
        # It creates the node with data and address fields
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def addFront(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            print("node inserted")
            return
            node = Node(data)
            node.nref = self.start_node
        self.head.pref = new_node
        self.start_node = new_node
    # def addFront(self,data):
    #     #print(data)
    #     node=Node(data)
    #     if self.head is None:
    #         head=node
    #     else:
    #         temp=self.head
    #         while temp.next is not None:
    #             temp=temp.next
    #         temp.next=node
    def addRear(self,data):
        global dec
        temp=self.head
        if self.head==None:
            dec=Node(data)
        self.head=dec

        while temp.next is not None:
                temp=temp.next
                deque=Node(data)
                temp.next=deque
    def removeFront(self,rempve):
        prev= self.head
        head= self.head.next
        return prev.data
    def renoveRear(self):
        xx=None
        temp=self.head
        prev=temp
        while temp.next is not None:
            prev=temp
            temp=temp.next
        xx=temp.next
        prev.next=None
        return xx
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp =temp.next












