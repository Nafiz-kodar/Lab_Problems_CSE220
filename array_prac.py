import numpy as np


# a2=np.zeros((5,6))            #making a 5x6 matrix and types of matrix
# print(a2)
# print(a2.shape)
# print(a2.ndim)
# print(a2.size)
# print(a2.dtype)
# print(type(a2))

# r=5                         #making a 5x5 matrix and primary diagonal sum
# c=5
# n=0
# sum=0
# a3=np.ones((r,c))
# for j in range(c):
#     for i in range(r):
#         a3[i][j]=n
#         n+=1
#         if i==j:
#             sum+=a3[i][j]
# print(a3)
# print(sum)
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr2=np.zeros(len(arr1),)
print(arr2)
for i in range(len(arr1)):
    arr2[i]=arr1[i] 

print(arr2)

arr1=arr1[::-1]
print(f"print reverse array{arr1}")