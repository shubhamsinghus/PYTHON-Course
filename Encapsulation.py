from idlelib.configdialog import changes  #in this we bind class and method togather
# class A:
#   a1=10
#   def show(self):
#       print(self.a1)
#
# class B(A):
#     def show(self):
#         print(self.a1)
#
# obj_1 = B()
# obj_2= A()
# print(obj_1.a1)
# print(obj_2.a1)
# obj_1.show()
# obj_2.show()
#
# class Television:
#     def _init_(self, brand, screen_size,current_channel,volume):
#         self.brand = brand
#         self.screen_size = screen_size
#         self.__current_channel = 1  # Private attribute
#         self.__volume = 20        # Private attribute
#
#     def get_channel(self):
#         return self.__current_channel
#
#     def set_channel(self, channel_number):
#         if 1 <= channel_number <= 999:  # Example validation
#             self.__current_channel = channel_number
#         else:
#             print("Invalid channel number.")
#
#     def get_volume(self):
#         return self.__volume
#
#     def adjust_volume(self, change):
#         new_volume = self.__volume + change
#         if 0 <= new_volume <= 100:  # Example validation
#             self.__volume = new_volume
#         else:
#             print("Volume out of range.")
#
# # Using the Television class
# my_tv = Television (" Samsung ", 55)
#
# print(f"Current channel: {my_tv.get_channel()}")
# my_tv.set_channel(5)
# print(f"Current channel: {my_tv.get_channel()}")
#
# my_tv.adjust_volume(10)
# print(f"Current volume: {my_tv.get_volume()}")
#
# # Attempting to directly access private attribute (discouraged)
# # print(my_tv.__volume) # This would result in an AttributeError



# class Laptop:
#     def __init__(self,brand,dimension):
#         self.brand = brand
#         self.dimension = dimension
#         self.__current_OS= 14#Private attribute
#         self.__price=45000
#     def get_OS(self):
#         return self.__current_OS
#
#     def set_OS(self, OS):
#          New_OS=self.OS + changes
#          if 10<New_OS  >= 16:
#              print(New_OS)
#
#          else:
#           print("Invalid OS")
#
#     def get_price(self):
#         return self.__price
#     def set_price(self, price):
#         if 15000<=price>= 100000 :
#          New_price= self.__price +changes
#          print(New_price)
#         else:
#          print("Out of range price")
#
# my_laptop = Laptop("HP","16inch")
# print(f"Current OS: {my_laptop.get_OS()}")
# print(f"Current price: {my_laptop.get_price()}")
# my_laptop.set_OS(12)
# print(f"Current OS: {my_laptop.get_OS()}")

# class Laptop:
#     def __init__(self, brand, dimension):
#         self.brand = brand
#         self.dimension = dimension
#         self.__current_OS = 14  # Private attribute
#         self.__price = 45000    # Private attribute
#
#     def get_OS(self):
#         return self.__current_OS
#
#     def set_OS(self, OS):
#         if 10 <= OS <= 13:
#             self.__current_OS = OS
#         else:
#             print("Invalid OS version. Allowed range: 10–13")
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, price):
#         if 15000 <= price <= 100000:
#             self.__price = price
#         else:
#             print("Out of range price. Allowed range: 15000–100000")


# # Test
# my_laptop = Laptop("HP", "16inch")
# print(f"Current OS: {my_laptop.get_OS()}")
# print(f"Current price: {my_laptop.get_price()}")
#
# my_laptop.set_OS(17)
# print(f"Updated OS: {my_laptop.get_OS()}")
#
# my_laptop.set_price(60000)
# print(f"Updated price: {my_laptop.get_price()}")
#

# class A():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# obj1=A("shubham",24)
# obj2=A("sahil", 20 )
# class B():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# obj3=B("sumit",28)
# obj4=B("shivam",22)
# print(obj1.name,obj1.age)
# print(obj2.name,obj2.age)
# print(obj3.name,obj3.age)
# print(obj4.name,obj4.age)
# print(obj1.age,
#       obj2.age
#       ,obj3.age,
#       obj4.age)
# class C(A,B):
#     def __init__ (self,name,age,qualification,Net_worth):
#         super().__init__(name,age)
#         self.qualification = qualification
#         self.Net_worth = Net_worth
#     def show(self):
#         print(self.name,end=" ")
#         print(self.Net_worth,end=" ")
#         print(self.age,end=" ")
#         print(self.qualification,end=" ")
# shubham's aura=C("shubham",24,"BSC","22k$")
# shubham's aura.show()



# class Universe:
#     def __init__(self,galaxy,planets):
#         self.__galaxy = galaxy
#         self.planets = planets
#     def get__galaxy(self):
#          return self.__galaxy
#     def set_galaxy(self,new_galaxy):
#         self.__galaxy =new_galaxy
#
# class Earth(Universe):
#     def __init__(self,galaxy,planets,humans,animals,plants):
#         super().__init__(galaxy,planets)
#         self.humans = humans
#         self.__animals = animals
#         self.plants = plants
#     def get__animals(self):
#         return self.__animals
#     def set__animals(self,new_animals):
#         self.__animals = new_animals
#
# my_surrounding=Universe('Andromeda',"earth")
# print(my_surrounding.get__galaxy())
# my_surrounding.set_galaxy("comet")
# print(my_surrounding.get__galaxy())
# my_surrounding.set_galaxy('Snake')
# print(my_surrounding.get__galaxy())
#
# my_environment=Earth("Tadple galaxy",'venus','shubham',"anakonda", "mango",)
# my_environment.get__animals()
# print(my_environment.get__animals())
# my_environment.set__animals('king Lion')
# print(my_environment.get__animals())
# my_environment.set__animals('Cow')
# print(my_environment.get__animals())