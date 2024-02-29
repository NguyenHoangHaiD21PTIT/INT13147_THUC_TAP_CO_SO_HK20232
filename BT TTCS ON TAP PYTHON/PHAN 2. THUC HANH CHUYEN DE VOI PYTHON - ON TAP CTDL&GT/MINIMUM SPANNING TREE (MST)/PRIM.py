used = [0] * 100 #Đã dùng
n, x = int(input()), int(input()) #Số đỉnh, đỉnh bắt đầu dựng cây
edge = [] #Lưu danh sách cạnh

#Nhập ma trận kề
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
    
#Duyệt và tạo danh sách cạnh
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j]: edge.append([i + 1, j + 1, a[i][j]])
print(edge)        
#Khởi tạo cây khung
d = 0 #Tổng chiều dài = 0 
MST = [] #Tập cạnh cây khung
used[x] = 1 

#Lặp
while len(MST) < n - 1:
    #Mỗi lần chọn ra 1 cạnh ngắn nhất với 1 đỉnh đã dùng và đỉnh kia chưa dùng
    t, x, y = 10**9, 0, 0 #t: trọng số cạnh min tại lúc đó, x y là 2 đầu cạnh nhỏ nhất
    for i in edge:
        if ((used[i[0]]==0 and used[i[1]]) or (used[i[1]]==0 and used[i[0]])) and i[2] <t:
            t = i[2]
            x, y = i[0], i[1]
            print(t)
    MST.append([x, y])
    d+=t 
    if used[x]==0: used[x] = 1
    else: used[y] = 1 

print("dH = {}".format(d))