class employee:
    company_name= "tech sol"
    def __init__(self,name,base_salary):
        self.name= name
        self.__base_salary = base_salary

    def get_salary(self):
        return self.__base_salary
    def give_raise(self,amount):
        if amount > 0:
            self.__base_salary+= amount
            print(f"paise of ${amount} approved for {self.name}.")

        else:
            print("invalid raise amount.")

    def work(self):
        return f"{self.name} is performing general corporate duties"

class Developer(Employee):
    def __init__(self, name, base_salary, programming_language):
        # super() calls the constructor of the parent class (Employee)
        super().__init__(name, base_salary) 
        self.programming_language = programming_language

    # Method Overriding (Polymorphism)
    def work(self):
        return f"{self.name} is writing brilliant code in {self.programming_language}."