a = [1,2,3,4,5]
# b = 2 *a

b = map(lambda x:x*2 ,a)
print(list(b))

from functools import reduce
a = [1,2,3,4,5,6]

product_a = reduce(lambda x,y: x*y,a)

print(product_a)

#error and exceptions

x = -5 
if x < 0: 
    raise Exception('x should be positive')