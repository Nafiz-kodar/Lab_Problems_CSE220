from lab_6class import *


def subtract_summation(root):
  subtraction=left_side_jog(root.left)-right_side_jog(root.right)
  return subtraction

def right_side_jog(root):
  if root == None:
    return 0
  else:
    return right_side_jog(root.left)+right_side_jog(root.right)+root.elem
def left_side_jog(root):
  if root == None:
    return 0
  else:
    return left_side_jog(root.right)+right_side_jog(root.left)+root.elem



#Driver Code
root=BTNode(71)
#Write other nodes by yourself from the given tree of Doc File

# Level 1
root.left = BTNode(27)
root.right = BTNode(62)

# Level 2
root.left.left = BTNode(80)
root.left.right = BTNode(75)
root.right.left = BTNode(41)
root.right.right = BTNode(3)

# Level 3
root.left.left.left = BTNode(87)
root.left.left.right = BTNode(56)
root.right.right.left = BTNode(19)
root.right.right.right = BTNode(89)

print(subtract_summation(root)) #This should print 111