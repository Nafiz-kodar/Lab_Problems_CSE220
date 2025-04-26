from lab_7class import BTNode

def find_path(root, key):
    way=[]
    if short_way(root,key,way):
        return way
    else:
        return "No Path Found"    

def short_way(root,key,way):
    if root is None:
        return False
    way.append(root.elem)
    if root.elem==key:
        return True
    else:
        left_way = short_way(root.left, key, way)
        right_way = short_way(root.right, key, way)
        if left_way or right_way:
            return True
    way.pop()
    return False
        
        
    



#DRIVER CODE
#Write by yourself from the given tree
# print(find_Path(root,15))
# #This should print [30,10,15]

# print(find_Path(root,50))
# Creating the tree structure
root = BTNode(30)
root.left = BTNode(10)
root.right = BTNode(40)
root.left.left = BTNode(3)
root.left.right = BTNode(15)
root.right.left = BTNode(35)
root.right.right = BTNode(55)

# Testing the function
print(find_path(root, 15))  # This should print [30, 10, 15]
print(find_path(root, 50))  # This should print no path found
#This should print No Path Found