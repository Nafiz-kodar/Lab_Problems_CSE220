from lab_6class import *

# Task-Code


def level_sum(root):
  sum=jog(root,0)
  return sum

def jog(root,level):
  if root==None:
    return 0
  if level%2==0:
    dig=-1*root.elem
  else:
    dig=root.elem
  return dig+jog(root.left,level+1)+jog(root.right,level+1)



#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4