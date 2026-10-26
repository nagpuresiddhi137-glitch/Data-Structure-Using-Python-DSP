class Node:
    def __init__(self,data):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert (self,data):
        new_node= Node (data)
        new_node.next=self.head
        self.head = new_node

    def display (self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

c11=LinkedList()
c11.insert(10)
c11.insert(20)
c11.insert(30)

c11.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    

    

    