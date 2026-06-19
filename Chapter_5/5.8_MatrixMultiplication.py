# Matrix Multiplicaiton

A = [[1, 3, 4],[5, 1, 0]]
B = [[3 ,1 ,5],[7, 0, 2],[2, -1, 3]]
Ans = []
row = len(A)
col = len(B[0])
for i in range(row):
    oneRow = col * [0]
    for j in range(col):
        s = 0.0
        for k in range(len(B)):
            s += A[i][k] * B[k][j]
        oneRow[j] = s
    Ans.append(oneRow)
print(Ans)
