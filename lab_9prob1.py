ver=7
edg=16
lbl=['a','x','r','3','9','i','q']

edg_list=[
    (0,1),(0,2),(0,3),(0,4),(1,2) ,(1,5),(2,6),( 2,4),(3, 4),(3,6),(4, 5), (5, 6),(1,3),( 2 , 3),(0 ,6),(4,6)]
edg_wght=[3, 2, 4, 1, 5, 2, 7, 6, 2, 3, 1, 5, 2, 3, 4, 6]

adj_mat=[]
for i in range(ver):
    row=[]
    for j in range(ver):
        row+=[0]
    adj_mat.append(row)


neightbor_n=[]
for i in range(ver):
    neightbor_n+=[0]

adj_list=[]
for i in range(ver):
    row=[]
    for j in range(ver):
        row+=[0]
    adj_list.append(row)

for i in range(edg):
    m=edg_list[i][0]
    n=edg_list[i][1]
    weight=edg_wght[i]
    adj_mat[m][n]=weight
    adj_mat[n][m]=weight
    adj_list[m][neightbor_n[m]]=n
    adj_list[n][neightbor_n[n]]=m
    neightbor_n[m]+=1
    neightbor_n[n]+=1


"""TASK-01"""

def max_deg_matrix(graph):
    maxver=0
    maxdeg=0
    for i in   range(ver):
        deg=0
        for j in range(ver):
            if graph[i][j]>0:
                deg=deg+1
            if  deg>maxdeg:
                maxdeg=deg
                maxver=i

    return lbl[maxver],maxdeg

def max_deg_list(graph):
    maxver=0
    maxdeg=0
    for i in range(ver):
        degree=0
        for j in range(ver):
            if graph[i][j]>0:
                degree=degree+1
            if degree>maxdeg:
                maxdeg=degree
                maxver=i
    return lbl[maxver],maxdeg


"""TASK-02"""
def max_weight_mat(graph):
    maxver=0
    maxwght=0
    for i in range(ver):
        wght=0
        for j in range(ver):
            if graph[i][j]>0:
                wght=wght+graph[i][j]
            if wght>maxwght:
                maxwght=wght
                maxver=i

    return lbl[maxver],maxwght
def max_weight_list(graph):
    maxver=0
    maxwght=0
    for i in range(ver):
        wght=0
        for j in range(neightbor_n[i]):
            wght=wght+graph[i][j]
        if wght>maxwght:
            maxwght=wght
            maxver=i
    return lbl[maxver],maxwght
"""TASK-03"""

def max_deg_matrix(graph):
    maxver=0
    maxdeg=0
    for i  in range(ver):
        deg=0
        for  j in range(ver):
            if graph[i][j] >0:  # Outgoing edge
                deg+=1
        if deg>maxdeg:
            maxdeg=deg
            maxver= i
    return lbl[maxver], maxdeg

def max_deg_list(graph, neighbor_n):
    maxver = 0
    maxdeg = 0

    for i in range(ver):

        deg = neighbor_n[i]  
        if deg > maxdeg:

            maxdeg = deg
            maxver = i

    return lbl[maxver], maxdeg

def max_weight_mat(graph):
    maxver =0
    maxwght = 0

    for i in range(ver):
        wght = 0

        for j in range(ver):
            if graph[i][j]>0:
                wght+=graph[i][j]

        if wght>maxwght:
            maxwght= wght
            maxver=i

    return lbl[maxver],maxwght

def max_weight_list(graph, neighbor_n, edge_weights):
    maxver=0
    maxwght=0
    
    for i in range(ver):
        wght = 0
        for j in  range(neighbor_n[i]):
            wght+=edge_weights[i][j]
        if wght>maxwght:
            maxwght  =wght
            maxver=  i
     
    return lbl[maxver],maxwght



######                 DRIVER_CODE              ######

print("Using Matrix:", max_deg_matrix(adj_mat))
print("Using List  :", max_deg_list(adj_list))

print("Using Matrix:", max_weight_mat(adj_mat))
print("Using List  :", max_weight_list(adj_list))


print("Max Out-Degree (Matrix):", max_deg_matrix(adj_mat))
print("Max Out-Degree (List):", max_deg_list(adj_list, neightbor_n))
print("Max Out-Weight (Matrix):", max_weight_mat(adj_mat))
print("Max Out-Weight (List):", max_weight_list(adj_list, neightbor_n, adj_mat))

