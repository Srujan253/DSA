class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def shortes_num(root,p,q):
    
    while root:
        if root.val>p.val and root.val>q.val:
            root=root.left
        elif root.val<p.val and root.val<q.val:
            root=root.right
        else:             
            return root.val
        
    
    

    

root=Node(10)
root.left=Node(2)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(6)
root.right.left=Node(15)
root.right.right=Node(30)
print(shortes_num(root,2,8))
#nothing done