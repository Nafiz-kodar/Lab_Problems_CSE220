from lab_7class import * 

def sum_of_leaves(root, sum):
  ans = helper_jog(root, sum)
  return ans

def helper_jog(root,sum):
    if root==None:
        return sum
    if root.right ==None and root.left==None:
        sum+=root.elem
        return sum
  
    return sum+helper_jog(root.left, sum)+helper_jog(root.right, sum)


#DRIVER CODE
#Write by yourself from the given tree
# Creating the tree structure
root = BTNode(30)
root.left = BTNode(10)
root.right = BTNode(40)
root.left.left = BTNode(3)
root.left.right = BTNode(15)
root.right.left = BTNode(35)
root.right.right = BTNode(55)
root.left.left.left = BTNode(2)
root.right.left.right=BTNode(36)

# Printing the sum of leaf nodes
print(sum_of_leaves(root, 0))