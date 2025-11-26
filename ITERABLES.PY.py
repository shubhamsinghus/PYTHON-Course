s="Hello world"
count = 0
for i in s :
     if count%2==0:
         print(i)
     count+=1
from itertools import count

#2 before and after spaces letter
# sentence="hello world how are you?"
# i=0
# count = 0
# for ch in sentence:
#         if ch==" ":
#             # print(count)
#             print(sentence[count-1])
#             print(sentence[count+1])
#         count= count+1


#3
# st="Hello World  ,How are you  ?"
# for ch in st:
#     if ch.isupper():   # check if character is capital
#         print(ch)

#convert a="A"
# chr(97-32)
# print("a=",chr(97-32))

#a="ABCD"
# a=chr(97-32)+chr(98-32)+chr(99-32)+chr(100-32)
# print("a=",a)
#
# #a="abcd"
# a=chr(65+32)+chr(66+32)+chr(67+32)+chr(68+32)
# print("a=",a)
#
# print(ord("c"))


st="my name IS KULDEEP"

for i in st:
    a=i
    ASCI = ord(a)
    # print(  chr(ASC1-32))
    a =  chr(ASCI+32)
    print(a)