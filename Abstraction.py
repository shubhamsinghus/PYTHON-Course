# from abc import ABC,  abstractmethod
# class Secrets(ABC):
#     def __init__(self, Hydrogen_bomb):
#         self.Hydrogen_bomb = Hydrogen_bomb
#         print("formula =Deuterium + Tritium → Helium + Neutron + Energy")
#     @abstractmethod
#     def __init__(self,atomic_bomb_formula):
#              pass
# class Mass_destruction(Secrets):
#
#     def __init__(self,mass_destruction):
#         super().__init__(3)
#         self.mass=mass_destruction
#         print("Wepons= Corona virus,  Nuclear exploison ")
#     def atomic_bomb_formula(self):
#         print("A formula =¹⁰n + ²³⁵U → ¹⁴¹Ba + ⁹²Kr + 3¹⁰n + Energy")
#     def Hydrogen_bomb(self):
#         print(" H formula =Deuterium + Tritium → Helium + Neutron + Energy")
# obj=Mass_destruction("Destroy world")
# obj.atomic_bomb_formula()
# obj.Hydrogen_bomb()
#
#

from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name,skills):
        self.name = name
        self.skills = skills
    @abstractmethod
    def qualification(self):
        pass

class profesionals (Person):
    def __init__(self, name, skills,salary):
        super().__init__(name,skills)
        self.salary = salary
        print("Enter the salary, salary")
    def qualification(self):
        print("Enter the qualification, qualification")
obj=profesionals("shubham",["A.I expert"],"12K $")
obj.qualification()







