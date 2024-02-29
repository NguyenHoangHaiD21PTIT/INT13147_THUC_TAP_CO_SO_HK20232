from collections import deque
import sys

#Chuyển số thành chữ
def changeNumtoChar(x):
    return chr(x + 64) 

#Thuật toán DFS
def DFS(x, visited, ke):
    visited[x] = 1 
    print(changeNumtoChar(x), end = " ")
    for i in ke[x]:
        if visited[i] ==0: DFS(i, visited, ke)

#Thuật toán BFS   
def BFS(x, visited, ke):
    #Bước 1: Khởi tạo
    q = deque()
    q.append(x)
    visited[x] = 1
    #Bước 2: Lặp
    while q:
        x = q.popleft() #Lấy đỉnh hàng đợi rồi xóa đi
        print(changeNumtoChar(x), end = " ")
        for i in ke[x]: #Duyệt  các đỉnh kề với đỉnh bị xóa
            if visited[i] ==0:
                q.append(i)
                visited[i] = 1
    
#Nhập ma trận  
input()  
n = int(input())
a = []
for i in range (n):
    b = list(map(int, input().split()))
    a.append(b)

#Tạo danh sách kề
ke = [[] for _ in range (500)]
for i in range(n):
    for j in range(n): 
        if a[i][j]==1: ke[i + 1].append(j + 1) 

visited = [0] * 1005

#Loại truy vấn
x = int(input())
if x == 1:
    print("1. Test breadth-first traversal: ")
    for i in range (1, n + 1):
        if visited[i] ==0: BFS(i, visited, ke)
else: 
    print("2. Test depth-first traversal: ")
    for i in range (1, n + 1):
        if visited[i] ==0: DFS(i, visited, ke)

