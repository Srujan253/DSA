class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class Solution:
    def traversal(self,head):
        temp=head
        while temp!=None:
            print(temp.data,"->",end="")
            temp=temp.next
        print("None")
    def reverse_list(self,head):
        prev=None
        curr=head
        while curr!=None:
            next_node=curr.next
            curr_next=prev
            prev=curr
            curr=next_node
        return prev
    

    
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
sl=Solution()
print(sl.middleNode(n1))

