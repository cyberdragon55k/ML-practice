# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] >arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# arr = [1,3,6,8,0,2,5]
# a = bubble_sort(arr)
# print(a)

# def linear_search(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return -1

# data = [10,50,30,70,80,20]
# target = 30
# result = linear_search(data,target)
# if result != -1:
#     print(f"element found at index: {result}")
# else:
#     print("element not found")



# list = [10,50,30]
# if 30 in list:
#     print('found it ')

# try:
#     idx = list.index(30)
#     print(f"index is {idx}")
# except ValueError:
#     print('not found ')

# def binary_search(arr, target):
#     low = 0 
#     high = len(arr) -1

#     while low <= high:
#         mid = (low+high) //2
#         guess = arr[mid]
#         if guess == target:
#             return mid
#         elif guess >target:
#             high = mid -1
#         else:
#             low = mid +1
#     return -1
# list = [1,2,3,5,7,9,11,55]

# print(binary_search(list,7))

# print(binary_search(list,55))

# Breadth-First Search (BFS)
# from collections import deque
# def bfs(graph, start_node):
#     visited = set()
#     queue = deque([start_node])
#     visited.add(start_node)

#     while queue:
#         current_node = queue.popleft()
#         print(current_node, end=' ')

#         for neighbor in graph[current_node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# # Output: A B C D E F
# bfs(graph, 'C')



#x = 20 
#y = 40

x,y = 20,40
x,y = y,x+20
print(f"the value of x :{x}, the value of y = {y}")