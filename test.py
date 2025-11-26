#  program to find factorial of number
# n=int(input("enter any number:"))
# #factorial => n!=n*(n-1)*(n-2).....*1
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
#
# print("Factorial of", n, "is", fact)
# #program to find no. is prime or not?

# n = int(input("enter any number:"))
# if n=1:
#     print("no. is not prime")
# elif n==2:
#     print("no.is prime)
# else:for i in range(2, n):
#         if n % i == 0:
#             print("Not prime")
#             break
n = int(input("Enter any number: "))

if n <= 1:
    print("Not prime")
elif n == 2:
    print("Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#program to find prime factors of a number.

# n = int(input("Enter any number: "))
# for i in range(2, n + 1):
#     if n % i == 0:
#         is_prime = True
#         for j in range(2,int(i**0.5)+1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#            print(i)

# #factors of a number
# n = int(input("Enter any number: "))
# for i in range(1,n//2):
#     if n%i==0:
#         print(i)
