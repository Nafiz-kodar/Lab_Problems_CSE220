from lab_7class import * 

def sum_of_leaves(root, sum):
  pass
def helper(root,sum):
    if root ==None:
        return sum
    if root.left==None:
        sum+=root.elem
        return
  
    return sum_of_leaves(root.left, sum)


#DRIVER CODE
#Write by yourself from the given tree
# Creating the tree structure
root = BTNode(10)
root.left = BTNode(5)
root.right = BTNode(15)
root.left.left = BTNode(3)
root.left.right = BTNode(7)
root.right.left = BTNode(12)
root.right.right = BTNode(18)

# Printing the sum of leaf nodes
print(sum_of_leaves(root, 0))