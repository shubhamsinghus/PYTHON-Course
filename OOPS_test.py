# class Employee:
#     def __init__(self, name,employee_id, salary):
#         self.name = name
#         self.employee_Id = employee_id
#         self.salary = salary
#     def calculate_bonus(self):
#         return self.salary*0.05
# class Manager(Employee):
#     def __init__(self, name, employee_id, salary):
#         super().__init__(name,employee_id,salary)
#     def calculate_bonus(self):
#        return self.salary*0.10
#
# class Developer(Employee):
#     def __init__ (self, name, employee_id, salary):
#         super().__init__(name,employee_id,salary)
#     def calculate_bonus(self):
#         return self.salary*0.08
#
# E1=Manager("Rohit_singh",53,350)
# E2=Developer("SHUBH",123,300)
# E3=Employee("Sahil",234,250)
# Employee=[E1,E2,E3]
# for E in Employee:
#     (print(E.name, E.employee_Id, E.salary, E.calculate_bonus(),"Total salary=",(E.salary+E.calculate_bonus())))


#bank account system
# class BankAccount:
#     def __init__(self,name,account_number,balance):
#         self.name=name
#         self.__account_number=account_number
#         self.__balance=balance
#     def credit(self,amount):
#         self.__balance+=amount
#         return self.__balance
#     def debit(self,amount):
#         self.__balance-=amount
#         return self.__balance
#
#     def get_balance(self):
#         return self.__balance
#
# class SavingAccount(BankAccount):
#     def __init__(self,name,account_number,balance,interest_rate):
#         super().__init__(name,account_number,balance)
#         self.interest_rate=interest_rate
#         interest_rate=(balance*interest_rate)/100
#
#     def add_interest(self):
#        self.interest_rate=self.balance*self.interest_rate/100

# Acc1=SavingAccount("rohit","12345678",10000,0.2)
# debit=Acc1.debit(1000)
# credit=Acc1.credit(100)
# print(debit)
# print(credit)
# interest_addition=Acc1.interest_rate
# print(interest_addition)
#

# from abc import ABC,abstractmethod


# class book:
#     def __init__(self,title,author,copies):
#         self.__title = title
#         self.__author = author
#         self.__copies = copies
#
#
#
# from abc import ABC, abstractmethod
#
# # -----------------------------
# # Encapsulation: Book class
# # -----------------------------
# class Book:
#     def __init__(self, title, author, copies):
#         self.__title = title
#         self.__author = author
#         self.__copies = copies
#
#     # Getters
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_copies(self):
#         return self.__copies
#
#     # Setters
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_copies(self, copies):
#         if copies >= 0:
#             self.__copies = copies
#
#     # Borrow book (reduce copies safely)
#     def borrow_copy(self):
#         if self.__copies > 0:
#             self.__copies -= 1
#             return True
#         else:
#             print(f" No copies of '{self.__title}' left.")
#             return False

# Return book (increase copies)
#     def return_copy(self):
#         self.__copies += 1
#
#
# # -----------------------------
# # Abstraction: Abstract User
# # -----------------------------
# class LibraryUser(ABC):
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []
#
#     @abstractmethod
#     def borrow_book(self, book: Book):
#         pass
#
#     def return_book(self, book: Book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             book.return_copy()
#             print(f" {self.name} returned '{book.get_title()}'. Copies now: {book.get_copies()}")
#         else:
#             print(f"{self.name} did not borrow '{book.get_title()}'.")
#
#
# # -----------------------------
# # Inheritance + Polymorphism
# # -----------------------------
# class Student(LibraryUser):
#     def __init__(self, name):
#         super().__init__(name)
#         self.student_limit = 0
#
#     def borrow_book(self, book: Book):
#         if self.student_limit < 2:   # Student limit
#             if book.borrow_copy():
#                 self.student_limit += 1
#                 self.borrowed_books.append(book)
#                 print(f" {self.name} borrowed '{book.get_title()}'. Copies left: {book.get_copies()}")
#         else:
#             print(f"{self.name} can't borrow more than 2 books.")
#

# class Teacher(LibraryUser):
#     def __init__(self, name):
#         super().__init__(name)
#         self.teacher_limit = 0
#
#     def borrow_book(self, book: Book):
#         if self.teacher_limit < 5:   # Teacher limit
#             if book.borrow_copy():
#                 self.teacher_limit += 1
#                 self.borrowed_books.append(book)
#                 print(f" {self.name} borrowed '{book.get_title()}'. Copies left: {book.get_copies()}")
#         else:
#             print(f"⚠ {self.name} can't borrow more than 5 books.")
#

# # -----------------------------
# # Demonstration
# # -----------------------------
# if __name__ == "__main__":
#     # Create some books
#     book1 = Book("Data Science", "R.K Sharma", 3)
#     book2 = Book("Python Basics", "Guido van Rossum", 2)
#
#     # Create users
#     users = [Student("Amit"), Teacher("Gupta Sir")]
#
#     # Polymorphism in action
#     for user in users:
#         user.borrow_book(book1)
#         user.borrow_book(book2)
#
#     # Trying to exceed limits
#     users[0].borrow_book(book1)   # Student exceeds limit
#     for _ in range(6):
#         users[1].borrow_book(book1)  # Teacher exceeds limit
#
#     # Return demo
#     users[0].return_book(book1)
#     users[1].return_book(book2)


# class Employee:
#     def __init__(self,id,salary):
#         self.id=id
#         self.salary=salary
# class Manager(Employee):
#     def __init__(self,id,salary,bonus):
#         super().__init__(id,salary)
#         self.bonus=bonus
# employee1=Employee(123,123425364,876)
# print(employee1.id)


# class Vehicle:
#     def __init__(self, brand, model, rental_price_per_day):
#         self.brand = brand
#         self.model = model
#         self.rental_price_per_day = rental_price_per_day
#
#     def vehicle_info(Vehicle):
#         pass
#
#
# Vehicle1 = Vehicle(brand="honda",model="City",rental_price_per_day=1500)
# Vehicle2=Vehicle(brand="Hyundai",model="i10",rental_price_per_day=1000)
# Vehicle1.vehicle_info()
# print(Vehicle2.brand)
# print(Vehicle1.model)
# print(Vehicle1.rental_price_per_day)

class Vehicle:
    def __init__(self, brand, model, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.__rental_price_per_day = rental_price_per_day

    def vehicle_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Rental Price per Day: {self.__rental_price_per_day}')

     def __get_price(self):
        return self.__rental_price_per_day
     def __set_price(self, new_price):
        new_price =rental_price_per_day

        if new_price >=0:
          print("invalid_price")
        else:
            print(new_price)
class Car(Vehicle):
    def __init__(self, brand, model, rental_price_per_day,seating_capacity):
        super().__init__(self,brand,model,rental_price_per_day)
        self.rental_price_per_day = rental_price_per_day
        self.seating_capacity = seating_capacity
    def vehicle_info(self):
        print(self.brand,self.model,self.rental_price,self.seating_capacity)
        return
class Bike(Vehicle):
    def __init__(self, brand, model, rental_price_per_day,helmet_included):
        super().__init__(self,brand,model,rental_price_per_day)
        self.helmet_included=True
    def vehicle_info(Bike):
        print("Brand: " + Bike.brand)
        print("Model: " + Bike.model)
car1=Car("honda","civic","2000","4")
car2=Car("honda","Elevate","2000","4")
car3=Car("hyundai","Exter","1500","4")
Bike1=Bike("honda","shine","600","true")
Bike2=Bike("honda","dream_yuva","600","false")
Bike3=Bike("hero","splendor","600","true")

CAR=[car1,car2,car3]
for Car in CAR:
    print(Car.brand,Car.model,Car.rental_price_per_day,Car.seating_capacity)
BIKE=[Bike1,Bike2,Bike3]
for Bike in BIKE:
    print(Bike.brand,Bike.model,Bike.rental_price_per_day,Bike.helmet_included)

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
    def cash_payment(self):
        print("{payment.make_payment} cash payment}")