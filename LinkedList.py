class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def isempty(self):
        if self.tail == None and self.head == None:
            return True
        else:
            return False
            
    def __str__(self):
        count = 0
        temp = ""
        start_node = self.head
        while start_node != None:
            temp += f"{count,start_node.data}-->"  
            start_node = start_node.next
            count +=1
        return temp

    def append(self,node):
        if self.isempty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def prepend(self,node):
        if self.isempty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        
    def insert(self,index,value):
        node = Node(value)
        if self.isempty():
            self.head = node
            self.tail = node
        elif index >= len(self):
            self.tail.next = node
            self.tail = node
        else:
            count = 0
            temp = self.head
            while count != index-1:
                temp = temp.next
                count += 1
            node.next = temp.next
            temp.next = node

    def __len__(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count




mylist = LinkedList()
mylist.prepend(Node(1))
mylist.prepend(Node(0))
mylist.prepend(Node(-1))
mylist.append(Node(2))
mylist.append(Node(3))
mylist.insert(2,45)
mylist.insert(0,45)
print(len(mylist))
print(mylist)