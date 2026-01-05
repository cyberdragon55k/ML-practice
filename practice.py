# #1 jan 2026
# # robot class

# class Robot:
#     def __init__(self,name, color):
#         self.name = name #attribute 
#         self.color = color # attribute
#         self.battery =100
    

#     def introduce(self):
#         print(f"hello! I am {self.name}, a {self.color} robot.")

#     def move(self, steps):
#         self.battery-= steps
#         print(f"{self.name} moved {steps} steps. Battery is now {self.battery}%")
    


# my_bot = Robot("griffen","orange")

# # my_bot.introduce()
# # my_bot.move(150)

# # student class 
# class Student:
#     def __init__(self, name , grade):
#         self.name = name
#         self.grade = grade
    

#     def study(self):
#         print(f"{self.name} is studying")

#     def Get_grade(self):
#         print(f"{self.name} is in grade {self.grade}")


# aditya = Student("Aditya Namdev","12")

# # aditya.study()
# # aditya.Get_grade()


# # bankaccount class

# class BankAccount:
#     def __init__(self,account_holder , balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance = self.balance+amount
#         print(f"The amount {amount} you entered is deposited to you account. your new balance is {self.balance}")




#     def withdraw(self, amount):
#         if (self.balance >= amount):
#             self.balance=self.balance-amount
#             print(f"The amount {amount} is been withdrawed. remaining balance is {self.balance}")
#         else:
#             print("Insufficient funds")


# a = BankAccount("Aditya",0)
# # a.deposit(100)
# # a.withdraw(5)



# #2 jan 2026

# #Avenger's
# class Avenger:
#     def __init__(self, name, health=100, power=10):
#         self.name = name
#         self.health = health
#         self.power = power

#     def take_damage(self,damage):
#         self.health -= damage
#         print(f"{self.name} took {damage} damage. Health is now {self.health}")
#         if self.health <= 0:
#             print(f"{self.name} has fallen!")
        
#     def heal(self):
#         self.health += 20 
#         if self.health >100:
#             self.health = 100
#             print(f"New health is {self.health}")


# ironman = Avenger("Ironman",100,100)

# ironman.take_damage(50)
# ironman.heal()
# ironman.take_damage(60)


# 3 jan 26

def count_frequency(nums):
    counts={}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

# print(count_frequency([1,2,3,1,1,2,1]))


def two_sum(nums, target):
    seen = {}
    for i , num in enumerate(nums):
        needed = target - num 

        if needed in seen:
            return [seen[needed],i]
        
        seen[num] = i

# print(two_sum([5, 5, 2], 10))



##
# 4 jan 26

squares = []
for x in range(10):
    squares.append(x*x)

# print(squares)

squares = [x *x for x in range(15)]

# print(squares)



# the initials generator 
names = ["Iron man", "Thor", "Hulk", "Spiderman"]
for name in names:
    print(name[0])




# 5 jan 26
def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart
# print(add_to_cart("Apple"))
# print(add_to_cart("banana"))


users = [
    {'name': 'Admin_01', 'active': True},
    {'name': 'Guest_User', 'active': False},
    {'name': 'Super_Dave', 'active': True},
    {'name': 'Lurker_99', 'active': False}
]

if (users.active) == True:
    print(users)