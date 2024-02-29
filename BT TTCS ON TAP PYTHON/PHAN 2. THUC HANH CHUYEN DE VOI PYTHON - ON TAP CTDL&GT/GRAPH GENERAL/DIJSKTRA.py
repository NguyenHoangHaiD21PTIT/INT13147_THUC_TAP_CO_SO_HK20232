n = int(input())

#Nhập ma trận
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
s, t = map(int, input().split())    
#Nhập danh sách kề
ke = [[] for _ in range(100)]
for i in range(n):
    for j in range(n):
        if a[i][j]: ke[i].append([j, a[i][j]])

#Tạo mảng d[x] là khoảng cách ngắn nhất từ nguồn tới x
d = [10**9] * 100; visited = [0] * 100; par = [-1] * 100

#Khởi tạo thuật toán
d[s] = 0 
#Hàng đợi ưu tiên để mỗi lần lôi (d[x], x): x là đỉnh chưa xét có d[x] min
import heapq
#Dùng minheap để đỉnh hàng đợi là bé nhất
pq = [(0, s)]

#Lặp
while pq:
    #Mỗi bước lấy ra đỉnh có d nhỏ nhất mà chưa xét
    dist, cur = heapq.heappop(pq)
    if visited[cur] == 1: continue #Lấy ra đỉnh đã xét thì bỏ qua
    visited[cur] = 1 #Chưa xét thì xét rồi đánh dấu
    for i in ke[cur]: #Xét tập các đỉnh kề với đỉnh được chọn
        v, w = i[0], i[1] #v: Đỉnh kề với cur, w: trọng số cạnh (v, cur)
        if d[v] > d[cur] + w:
            d[v] = d[cur] + w
            heapq.heappush(pq, (d[v], v))
            par[v] = cur
            
#Xây dựng đường đi
path = []  
t1 = t
while t1!=s:
    path.append(t1)
    t1 = par[t1]
path.append(s)
print("Dijkstra's shortest path algorithm:")
print("The shortest distance from vertex {} to {} is {}".format(s, t, d[t]))  
print("The shotest path is ", end = "")
for i in range(len(path) - 1, 0, -1): print(path[i], end = " -> ") 
print(path[0])   
