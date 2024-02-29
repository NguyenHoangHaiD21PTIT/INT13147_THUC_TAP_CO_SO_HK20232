n = int(input())
a = []
for i in range(n): 
    b = list(map(int, input().split()))
    a.append(b)
u, v = map(int, input().split())

next = [[-1] * 100 for _ in range (100)] 
#next[i][j] là điểm tiếp theo của điểm i trên đường đi từ i đến j
d = [[10**9] * 100 for _ in range(100)]
#d[i][j] là khoảng cách ngắn nhất từ i đến j 

#Bước 1a: Khởi tạo khoảng cách mặc đỉnh
for i in range(n): 
    for j in range(n): d[i][j] = 10**9
    d[i][i] = 0

#Bước 1b: Khởi tạo khoảng cách mặc định dựa trên trọng số
for i in range(n):
    for j in range(n):
        if a[i][j]: #Có trọng số -> Có đường đi
            next[i][j] = j
            d[i][j] = a[i][j]
        else: 
            next[i][j] = -1

#Bước 2: Cập nhật khoảng cách dựa trên đỉnh trung gian
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j] and d[i][k]!=10**9 and d[k][j]!=10**9:
                d[i][j] = d[i][k] + d[k][j]
                next[i][j] = next[i][k]

#Bước 3: Truy vết đường đi
path = [u]
u1 = u
while u!=v:
    u = next[u][v]
    path.append(u)

print("Floyd's shortest path algorithm:") 
print("The shortest distance from vertex {} to {} is {}".format(u1, v, d[u1][v]))  
print("The shotest path is ", end = "")
for i in range(len(path) - 1): print(path[i], end = " -> ")
print(path[-1])
