#Thực hiện Cấu trúc dữ liệu DSU (Make_set sẽ thực hiện trong main)
def find(x, par):
    if x == par[x]: return x
    par[x] = find(par[x], par)
    return par[x]

#Gom 2 đỉnh ở 2 tập vào cùng 1 tập
def union(a, b, par, sze):
    a = find(a, par)
    b = find(b, par)
    #Nếu ở chung 1 tập thì không gộp nữa
    if a == b: return False
    if sze[a] < sze[b]: a, b = b, a
    par[b] = a
    sze[a] += sze[b]
    return True

#Đọc ma trận
n = int(input())
a = []
for i in range (n):
    b = list(map(int, input().split()))
    a.append(b)
    
edges = []
#Tạo danh sách cạnh   
for i in range(n):
    for j in range(n):
        if a[i][j] and i < j: edges.append([i + 1, j + 1, a[i][j]])
#Sắp xếp theo trọng số tăng dần
edges.sort(key=lambda x: x[2])


#Thực hiện thuật toán Kruskal
d = 0 #Tổng chiều dài cây khung
mst = [] #Tập cạnh của cây khung
#Thao tác make_set
par = [i for i in range(15)]
sze = [1] * 15

#Duyệt từng cạnh
for edge in edges:
    #Đủ cạnh cuả cây khung thì dừng
    if len(mst) == n - 1: break
    #Kiểm tra xem khi thêm cạnh có ra chu trình không
    if union(edge[0], edge[1], par, sze):
        mst.append((edge[0], edge[1]))
        d += edge[2]

print("dH =", d)
for edge in mst: print(edge[0], edge[1])
