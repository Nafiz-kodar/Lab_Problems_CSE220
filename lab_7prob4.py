from lab_7class import *

def mirror_sum(root):
  ans=helperOFsum(root.left,root.right,0)
  return ans

def helperOFsum(l, r, sum):

    if l is not None and r is not None:
        
        local_sum = l.elem + r.elem
        local_sum += helperOFsum(l.left, r.right, sum)
        local_sum += helperOFsum(l.right, r.left, sum)
        return local_sum

    return sum




#DRIVER CODE

print("---------------------Test#1---------------------")
#Example Tree 1
root = BTNode(10)
n1 = BTNode(6)
n2 = BTNode(15)
n3 = BTNode(3)
n4 = BTNode(8)
n5 = BTNode(12)
n6 = BTNode(20)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n2.left = n5
n2.right = n6
print("Expected Output: 64")
print("You output     :",mirror_sum(root))

print("---------------------Test#2---------------------")

#Example Tree 1
root = BTNode(20)
n1 = BTNode(15)
n2 = BTNode(25)
n3 = BTNode(10)
n4 = BTNode(18)
n5 = BTNode(5)
n6 = BTNode(30)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n3.left = n5
n2.right = n6
print("Expected Output: 80")
print("You output     :",mirror_sum(root))