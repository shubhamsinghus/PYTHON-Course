# #print prime numbers
#n = int(input("Enter any number: "))


# #
# # print("the number is prime" ))
#  #factorial of a number using for loop
# n=int(input(" enter any number:"))
# fact=1
# for i in range(1,n+1):
#
#    fact*=i
# print("factorial of ", n ,"is",fact)

#reverse the number using while loop 1to10
#while n>1:

#factorial of a number using recursion
#def fact(n):n*n-i
 #  fact=n*n-1
#
# #print fabbonaci series 0 to 10
# def fabonacci(n):
#     a,b=0,1
#     count=0
#     for i in range(1,n+1):
#         a,b = b,a+b
#         print(a,end=" ")
#     count+=1
# fabonacci(n)
#
#

class Person(object):
  def __init__(self, designation, id):
    self.designation = designation
    self.id = id

  def Display(self):
    print(self.designation, self.id)

# Driver code
emp = Person("E", 102)
emp.Display()


