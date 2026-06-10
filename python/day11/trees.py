#non linear data Structure
#structural and other root and leef node 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)
def preOrder(root):
    if root is not None:
       print(root.data,end=" ")
       preOrder(root.left)
       preOrder(root.right)
def PostOrder(root):
    if root is not None:
        
       PostOrder(root.left)
       PostOrder(root.right)
       print(root.data,end=" ")
def level_order(root):
    if root is None:
        return root
    que=[]
    
    que.append(root)
    while que:
        curr=que.pop(0)
        print(curr.data,end=" ")
        if curr.left:
            que.append(curr.left)
        if curr.right:
            que.append(curr.right)
def sum_of_nodes(root):
    if root is None:
        return 0
    sum=root.data+sum_of_nodes(root.left)+sum_of_nodes(root.right)
    return sum
    
def height_of_tree(root):
    if root is None:
        return 0
    d={}
    que=[]
    que.append(root)
    d[root]=1
    

    

    
    
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(30)
# print("INORDERRRRRR")
# inOrder(root)
# print()
# print("PREORDERRRRRR")
# preOrder(root)
# print()
# print("POSTORDERRRRRR")
# PostOrder(root)

# print("Level Order")
# level_order(root)

print("Sum of nodes are :",sum_of_nodes(root))
