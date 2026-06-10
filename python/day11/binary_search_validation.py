class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def is_binary(root):
    

root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(30)