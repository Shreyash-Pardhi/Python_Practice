#structure of node
class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next=next

#structure of linked list
class LinkedList:
    def __init__(self):
        self.head=None
    
    def add_at_begining(self, data):
        node = Node(data,self.head)
        self.head =node
    
    def add_at_end(self, data):
        if self.head == None:
            self.head=Node(data, None)
            return
        
        loop = self.head
        while(loop.next):
            loop = loop.next
        
        loop.next = Node(data, None)
    
    def length(self):
        loop = self.head
        c=0
        while(loop):
            c+=1
            loop=loop.next
        return c
    
    def delete_at(self, index):
        if self.head == None:
            print('No elements to delete')
            return
        
        if index == 0:
            self.head=self.head.next
            return
        
        if index<0 or index>(self.length())-1:
            print("Index not found")
            return
        
        loop = self.head
        c=0
        while loop:
            if c == index -1:
                loop.next = loop.next.next
                break
            c+=1
            loop = loop.next
        
        
    def traverse(self):
        if self.head == None:
            print('Linked List is Empty')
            return
        
        loop = self.head
        link_list=''
        while(loop):
            link_list += str(loop.data) + ' -> '
            loop=loop.next
        print(link_list)
        
if __name__ == '__main__':
    ll=LinkedList()
    ll.add_at_begining(20)
    ll.add_at_begining(245)
    ll.add_at_end(12)
    ll.add_at_end(15)
    ll.traverse()
    print('length: ',ll.length())
    ll.delete_at(3)
    ll.traverse()
