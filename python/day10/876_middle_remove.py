class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class Solution:
    def middleNode(self,head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        return slow.value
    
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
sl=Solution()
print(sl.middleNode(n1))
    