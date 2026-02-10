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
# #     'B': ['D', 'E'],
# #     'C': ['F'],
# #     'D': [],
# #     'E': ['F'],
# #     'F': []
# # }

# # # Output: A B C D E F
# # bfs(graph, 'C')




# # class product:
# #     def __init__(self,name, price, quantity):
# #         self.name = name
# #         self.price = price
# #         self.quantity = quantity
# #     def sell(self, amount):
# #         if amount > self.quantity:
# #             print(f"error : no\enough {self.name} in stock ! (only {self.quantity})")
# #         else:
# #             self.quantity -= amount
# #             print(f"sold {amount} {self.name}(s). remaining: {self.quantity}")
# #     def restock(self, amount):
# #         self.quantity += amount
# #         print(f"restocked{amount} {self.name}s total :{self.quantity}")
# #     def __str__(self):
# #         return f"protduct:{self.name}|  price {self.price} | stock: {self.quantity}" 
    
# # laptop  = product("gaming laptop", 1200,5)
# # print(laptop)
# # laptop.sell(2)
# # laptop.sell(10)
# # laptop.restock(5)


# # def two_sum(nums, target):
# #     lookup = {}
    
# #     for i, num in enumerate(nums):
# #         needed = target - num
# #         if needed in lookup:
# #             return [lookup[needed], i]
# #         lookup[num] = i
# #     return []

# # nums = [2, 7, 11, 15]
# # print(f"Indices: {two_sum(nums, 9)}")

# def __init__(self, title, author, isbn): # Added comma here
#     self.title = title
#     self.author = author 
#     self.isbn = isbn
#     self.is_available = True

# class library:
#     def __init__(self):
#         self.books = {}
#     def add_book(self, book):
#         self.books[book.isbn] = book
#         print(f"Added: {book.title}")

#     def find_book(self, isbn):
#         return self.books.get(isbn, "Book not found.")

#     def checkout(self, isbn):
#         book = self.books.get(isbn)
#         if book and book.is_available:
#             book.is_available = False
#             return f"You've checked out {book.title}."
#         return "Book is either unavailable or doesn't exist."

# import heapq
# from collections import Counter

# def top_k_frequent(nums, k):

#     count = Counter(nums)
    

#     return heapq.nlargest(k, count.keys(), key=count.get)

# print(top_k_frequent([1,1,1,2,2,3], 2))

# arr = [10, 20, 30, 40, 50]
# n = len(arr)

# for i in range(n // 2):
#     arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# # print("Reversed array:", arr)
# arr = [3,2,2,2,2,2,2,2,2]
# print(arr)

# rows = 5
# for i in range(1,rows +1):
#     print('#' * i)

# class Stack:
#   def __init__(self):
#     self.stack = []

#   def push(self, element):
#     self.stack.append(element)

#   def pop(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack.pop()

#   def peek(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack[-1]

#   def isEmpty(self):
#     return len(self.stack) == 0

#   def size(self):
#     return len(self.stack)

# # Create a stack
# myStack = Stack()

# myStack.push('A')
# myStack.push('B')
# myStack.push('C')

# print("Stack: ", myStack.stack)
# print("Pop: ", myStack.pop())
# print("Stack after Pop: ", myStack.stack)
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.size())








list = [1,2,2,3,4,5,5,5]
# print(list[0])
# print(list[1])
# print(list[3])
# print(list[4])
# print(list[4])


print(list[6])
print(list[1])