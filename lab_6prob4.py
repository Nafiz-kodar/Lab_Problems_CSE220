from lab_6class import *


def swap_child(root, level, M):
  ghurao(root,level,M)
  return root

def ghurao(root,level,M):
  if root==None:
    return

  if level<=M:
    root.right,root.left=root.left,root.right
    ghurao(root.left,level+1,M)
    ghurao(root.right,level+1,M)


#Driver Code
root=BTNode('A')
node1 = BTNode("B")
node2 = BTNode("C")
node3 = BTNode("D")
node4 = BTNode("E")
node5 = BTNode("F")
node6 = BTNode("G")
node7 = BTNode("H")
node8 = BTNode("I")
node9 = BTNode("J")

root.left = node1
root.right = node2

node1.left=node3
node1.right=node4

node3.left=node6
node3.right=node7

node4.left=node8

node2.right=node5

node5.left=node9

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H