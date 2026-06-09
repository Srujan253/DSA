#__int__ acts like an constructor 
#object name is equal to class name
#data is data and next if next node 
#self keyword used to pass object and classs 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def traversal(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"->",end="")
            temp=temp.next
        print("None")
    def add_at_start(self,data):
        new_data=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        new_data.next=temp.data
        self.head=new_data
    def add_at_end(self,data):
        new_data=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_data
    def delete_at_end(self):
        prev=self.head
        temp=self.head
        while temp.next!=None:
            prev=temp
            temp=temp.next
        print(prev.next.data)
        prev.next=None
    def delete_at_start(self):
        
        temp=self.head.next
        self.head.next=None
        print(self.head.data)
        self.head=temp
        
    def sum_of_nodes(self):
        sum=0
        temp=self.head
        while temp!=None:
            sum+=temp.data
            temp=temp.next
        print("sum of nodess:",sum)
    
    
n1=Node(10)
sll=SLL()
sll.head=n1
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
sll.traversal()

sll.sum_of_nodes()

sll.delete_at_end()
sll.traversal()

sll.delete_at_start()
sll.traversal()


