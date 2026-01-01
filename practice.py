# robot class

class Robot:
    def __init__(self,name, color):
        self.name = name #attribute 
        self.color = color # attribute
        self.battery =100
    

    def introduce(self):
        print(f"hello! I am {self.name}, a {self.color} robot.")

    def move(self, steps):
        self.battery-= steps
        print(f"{self.name} moved {steps} steps. Battery is now {self.battery}%")
    


my_bot = Robot("griffen","orange")

my_bot.introduce()
my_bot.move(150)

# student class 
class Student:
    def __init__(self, name , grade):
        self.name = name
        self.grade = grade
    

    def study(self):
        print(f"{self.name} is studying")

    def Get_grade(self):
        print(f"{self.name} is in grade {self.grade}")


aditya = Student("Aditya Namdev","12")

aditya.study()
aditya.Get_grade()


# bankaccount class

class BankAccount:
    def __init__(self,account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount
        print(f"The amount {amount} you entered is deposited to you account. your new balance is {self.balance}")




    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance=self.balance-amount
            print(f"The amount {amount} is been withdrawed. remaining balance is {self.balance}")
        else:
            print("Insufficient funds")


a = BankAccount("Aditya",0)
a.deposit(100)
a.withdraw(5)



