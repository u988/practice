#   python is easy and simple,free and open source,its a high level language


# print("heello world")

# VARIABLES
#a variables is a name given to a memory location in a program

# name="uday"
# age= 23
# price=25.99

#  DATA TYPES

# INTEGERS
# STRING
# FLOAT
# BOOLEAN 
# NONE


#  1) write a pgm to input 2 numbers and print their sum

# a= int(input("enter a first number:" ))
# b=int(input("enter a second number:" ))

# sum= a+b
# print(sum)

#  2)  WAP to input 2 floating point numbers & print their average.

# a= float(input("enter a first number:" ))
# b= float(input("enter a second number:" ))

# avg= (a+b)/2
# print("avg:",avg)

#  3) WAP to input side of a square & print its area.

# a= float(input("enter a first number:" ))

# print("aarea is :",a ** 2)

#  4) WAP to input 2 int numbers, a and b.Print True if a is greater than or equal to b. If not print False.

# a= int(input("enter a first number:" ))
# b= int(input("enter a second number:" ))

# print(a>=b)

#  5) WAP to input user’s first name & print its length.
# a= str(input("enter a first number:" ))
# print(a)
# print(len(a))

# 6) WAP to find the occurrence of ‘$’ in a String.
# str= "hii,$Iam the $ symbol $99.90"
# print(str.count("$"))

# 7) WAP to check if a number entered by the user is odd or even.
# a = int(input("enter a number:" ))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# 8) WAP to find the greatest of 3 numbers entered by the user.
# a = int(input("enter a first number:" ))
# b = int(input("enter a second number:" ))
# c = int(input("enter a third number:" ))
# if a>=b and a>=c:
#     print("A is greter number")
# elif b>=c:
#     print("B is greter")
# else:
#     print("C is greter number")

# 9) WAP to check if a number is a multiple of 7 or not.

# a=int(input("enter a number"))
# num=7
# if  a%num==0:
#     print("it has multiple")
# else:
#     print("its not multiple")


# 10)  WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# list=[]
# a=(input("enter a first movie name:" ))
# b=input("enter a second movie name:" )
# c=input("enter a third movie name:" )

# list.append(a)
# list.append(b)
# list.append(c)
# print(list)


# grade=["a","b","a","b"]
# grade.sort()
# print(  grade)

# student={
#     "name":"uday",
#     "class":10,
#     "subjects":{
#         "cn":90.99,
#         "dbms":78.99,
#         "ml":89.87
#     }
# }
# new={"ml":99.43}
# student.update(new)
# print(student)


# animal={
#     "cat":"a small animal",
#     "table":["a piece of furniture","list of facts figure"],
# }
# print(animal)

# marks={}
# x=int(input("enter ml:"))
# marks.update({"ml":x})
# x=int(input("enter cn:"))
# marks.update({"cn":x})
# x=int(input("enter dbms:"))
# marks.update({"dbms":x})
# print(marks)

# n=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(i*n)
#     i +=1


# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# idx =0
# while idx < len(nums):
#     if (nums[idx]==x):
#         print("found",idx)
   
#     idx +=1


# def calc():
#     word="java"
#     with open("demo1.txt","r")as f:
#         data=f.read()
#         if data.find(word) !=-1:
#             print("found")
#         else:
#             print("not found")

# calc()

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hii",self.name,"your score is",sum/3)
s1=student("bmw",[90,89,87])
s1.avg()








