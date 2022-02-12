#Height of Binary Tree using recursion

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 

def height(root):
    if root == None:
        return 0 
    left_height = height(root.left)
    right_height = height(root.right)
    
    return 1+ max(left_height,right_height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)
print(height(root))
