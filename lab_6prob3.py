from lab_6class import *


def sumTree(root):
  sum=jog_koro(root,0)
  return sum
  #you can declare as many helper function with extra parameters as you need .
  #You can not modify the parameters of sumTree or modify any part of the given code.


def jog_koro(root,level):
  if root==None:
    return 0
  if level==0:
    dig=root.elem
  else:
    dig=root.elem % level
  return jog_koro(root.left,level+1)+jog_koro(root.right,level+1)+dig

#Driver Code
#Input 1
root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15