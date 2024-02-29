def Hamilton(k, n, x, ke, visited): #Xây dựng chu trình Hamilton từ đỉnh thứ k
    for i in ke[x[k - 1]]:
        if k == n + 1 and i == x[1]:
            for i in range(1, n + 1): print(x[i], end = " ")
            print(x[1]) 
        elif visited[i] == 0:
            x[k] = i 
            visited[i] = 1 
            Hamilton(k + 1, n, x, ke, visited)
            visited[i] = 0

n, v = int(input()), int(input())
#Nhập ma trận kề
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

#Tạo danh sách kề    
ke = [[] for _ in range(100)]
for i in range(n):
    for j in range(n):
        if a[i][j]: ke[i + 1].append(j + 1)

#Liệt kê chu trình Hamiltion
x = [0] * (n + 5) #x: Vector lưu chu trình Hamilton
x[1] = v
visited = [0] * 100
visited[v] = 1
Hamilton(2, n, x, ke, visited)