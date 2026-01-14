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

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

data = [10,50,30,70,80,20]
target = 30
result = linear_search(data,target)
if result != -1:
    print(f"element found at index: {result}")
else:
    print("element not found")