import heapq
min_heap = []
heapq.heappush(min_heap, (5))
heapq.heappush(min_heap, (2))
heapq.heappush(min_heap, (10))

# Lấy phần tử nhỏ nhất từ min heap
min_element = heapq.heappop(min_heap)
print(min_element)