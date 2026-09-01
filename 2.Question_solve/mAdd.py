A = [[2,4],[3,6]]
B = [[3,4],[2,5]]
row = len(A)
col= len(A[0])
relsult = [for i in range(row)][for j in range(col)]
# print(col)
for i in range(row):
    for j in range(col):
        relsult[i][j] = A[i][j] +B[i][j]
        
        
print(relsult)                
        