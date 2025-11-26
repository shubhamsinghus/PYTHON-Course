li=[5,6,7,0,-1-2,-3]
                                    #Q=1
# sum=0
# count=1
# for i in li:
#     count+=1
#     sum+=i
#
#
# print(count)
# print("sum= ",sum)
#
# avg=sum/count  #mean=average
# print(avg)

#median=
# for even terms n= even =>(((n/2)th terms+(n/2)+1)th term)/2
#for odd term=>n=odd = (n/2)th term
# count=1
# for i in li:
#     count+=1
# print(count)
# #n=7 which is odd ((n+1)/2)term
# li.sort()
# print(count=4)


# li = [-9,-8,-6,0,8,11,20,22,23]
# li.sort()
# print(li)
# count=0
# for i in li:
#     count+=1
#
# print(count)


# if (count%2==1):
#
#     n = (count+1)/2
#     n = int(n)
#     print(li[n])
# else :
#     n1 = int((count)/2)
#     n2 = int(n1+1)
#
#     median = (li[n1]+li[n2])/2
#     print("median is ",median)
    ##2
# li = [-9,-8,-6,0,8,11,20,22,23]
# count=0
#
# for i in li:
#      if i%2 ==0:
#        print( i,end=" ")
#        count +=1
# print("\nTotal even numbers:",count)
#3
# li = [-9,-8,-6,0,8,11,20,22,23]
# count=0
# for i in li:
#     if i%2==1:
#       print( i,end=" ")
#       count +=1
# print("\nTotal odd numbers:",count)

#4
# li = [-9,-8,-6,0,8,11,20,22,23]
# neg_count = 0
# pos_count = 0
#
# for i in li:
#     if i < 0:
#         print(i, end=" ")
#         neg_count += 1
#     elif i > 0:
#         print(i, end=" ")
#         pos_count += 1
#
# print("\nThe total no. of negative integers:", neg_count)
# print("The total no. of positive integers:", pos_count)
# print("zero is neither +ve or -ve")
#
#
#  ##5
# li=["hello","world","how","are","you","?"]
# count=0
# for s in li:
#     char_count=0
#     for ch in s:
#         char_count+=1
#
#     if char_count>=5:
#         count+=1
# print("the number of string with length>=5:",count)

#6 product of positive numbers
# li = [-9,-8,-6,0,8,11,20,22,23]
# count=0
# product=1
# for i in li:
#     if i > 0:
#         print(i,end=" ")
#         product*=i
#         count+=1
# print("Product of positives is",product )

##7 replace negative with zero
# li = [-9,-8,-6,0,8,11,20,22,23]
# # for i in li:
# #     if i <0:
# #         li=0
# # i for i in li
# li = [-9, -8, -6, 0, 8, 11, 20, 22, 23]
# #li = [0 if i < 0 else i for i in li]
# #print(li)
# li = [-9, -8, -6, 0, 8, 11, 20, 22, 23]
# for i in range (len(li)-1,-1,-1):
#     print(li[i], end=" ")
#
#
#
#
# # #
# # # li = [-9, -8, -6, 0, 8, 11, 20, 22, 23]
# # #
# # # largest = li[0]  # assume first element is largest
# # # for i in li:
# # #     if i > largest:
# # #         largest = i
# # #
# # # print("Largest number is:", largest)
# #
# # #
# # #
# # # li = [-9, -8, -6, 0, 8, 11, 20, 22, 23]
# # # smallest=li[0]
# # # for i  in li:
# # #     if i<smallest:
# # #         smallest=i
# # # print("The smallest number is ", smallest)
# # #find second largest number
# #
# # li = [-9, -8, -6, 0, 8, 11, 20, 22, 23]
# # li =[0 if i>0 else i for i in li]
# # print(li)
# # li=[5,0,1,2,3,4,5,87,34,79]
# # length=len(li)
# # for i in range(length,0,-1):
# #         print(li[i-1],end=" ")
#
# 1. for i in range(5):
# #     for j in range (5):
# #        print("*" ,end="")
# #     print()
# 2 for i in range(6):
# #     for j in range(i):
# #         print("*",end="")
# #     print()
# #

# 3.for i in range(5):
#      for j in range (i+1):
#        print("*" ,end=" ")
#      print()
# 4.
# for i in range(5):
#     for j in range (5-i-1):
#         print(" ",end=" ")
#     for k in range(i+1):
#       print("*",end=" " )
#     print()

# 5. for i in range(5):
#     for j in range (i):
#         print(" ",end=" ")
#     for k in range(5-i):
#       print("*",end=" " )
#     print()
##

#8
# for i in range(6,0,-1):
#     for j in range(6,0,-1):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#      print("*",end=" ")
#     print()

#8
# for i in range(5):
#     for j in range (5-i-1):
#         print(" ",end=" ")
#     for k in range(i+1):
#       print("*  ",end=" " )
#     print()
# #9
n=4
# for i in range(1,n+1):
#     for  j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#10
# n = 5  # peak height
#
# # increasing part
# for i in range(1, n+1):
#     print("  " * (n - i), end="")   # spaces before stars
#     print("* " * i)
# # decreasing part
# for i in range(n-1, 0, -1):
#     print("  " * (n - i), end="")   # spaces before stars
#     print("* " * i)

#11
# n=5
# for i in range(0,n):
#     print("  " * (i), end="")
#     print("*  " * (n-i))
# print()
# 12
# n=5
# for i in range(0,n):
#     print("  "* (i), end="")
#     print(" * "*(n-i))
# for i in range(2,n+1):
#     print("  "* (n-i), end=" ")
#     print(" * "*(i))

#13
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *

# n = 5
# for i in range(n):
#     # left stars
#     print("*" * (n - i), end="")
#
#     # middle spaces
#     print(" " * (2 * i), end="")
#
#     # right stars
#     print("*" * (n - i))

#14
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *
# n= int(input("Enter the of rows ="))
# for j in range(n) :
#     print("*", end=" ")
# print()
#
# for i in range(n-2) :
#  print("*",end=" ")
#  for j in range(n-2) :
#       print(" ",end=" ")
#  print("*")
#
# for j in range(n) :
#          print("*",end =" ")
# print()

# n = 5
# for i in range(n):
#     # left stars
#     print("*" * (n - i), end="")
#
#     # middle spaces
#     print(" " * (2 * i), end="")
#
#     # right stars
#     print("*" * (n - i))


# n=int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1,):
#         print(j+1,end=" ")
     #print()


class phone:
    dimension="5"
    colour="blue"
    brand="samsung"
    def sample(self):
        hioiij(self.dimension)
        print(self.colour)
        print(self.brand)
object=phone()
print(object.dimension)
print(object.colour)
print(object.brand)


