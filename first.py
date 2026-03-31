#age = 80
#if(age>=18):
#    print("eligeble for vote")
#else:
#    print("not eligeble for vote")



# light = "yellow"
# if(light == "green"):
#     print("go")
# elif(light=="yellow"):
#     print("wait")
# elif(light=="red"):
#     print("stop")
# else:
#     print("wrong signal")




# marks=67
# if(marks>=90):
#     print("grade A")
# elif(marks>=80):
#     print("grade B")
# elif(marks>=70):
#     print("grade C")
# else:
#     print("grade D ")
 


# marks = int(input("enter student marks:" ))
# if(marks>=90):
#     grade="A"
# elif(marks>=80 and marks<=90):
#     grade="B"
# elif(marks>=70 and marks<=80):
#     grade="C"
# else:
#     grade="D"
# print("the grade is :",grade)




# lergest three number

# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number:"))
# if(a>=b):
#     print("A is lerger")
# elif(b>=c):
#     print("B is larger")
# elif(c>=a):
#     print("C is larger")

#          or

# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number:"))
# d=int(input("enter fourth number:"))
# if(a>=b and  a>=c  and a>=d):
#      print("A is lergest number")
# elif(b>=c and b>=d):
#      print("B is lergest number")
# elif(c>=d):
#     print("C is lergest number")
# else:
#      print("D is lergest number")




  # ODD AND EVEN NUMBER

# num=int(input("enter anumber"))
# if(num % 2 ==0):
#     print("EVEN")
# else:
#     print("ODD")



#    CHAPTER 3
#    LISTS

# marks=[90.2,80.3,45,56.5,76.9]
# print(marks)
# print(len(marks))   #length of list
# print(marks[2])


# student=["uday",23,"shimoga"]
# print(student)
# print(student[0:3])

#       or

# marks=[90,26,56,76,65,78,34]
# print(marks)
# print(len(marks))
# print(marks[1:5])
# print(marks[0:])
# print(marks[ :5])
# print(marks[-3:-1])


        #LIST METHODS

# lists=[2,3,4,1,7,7]
# lists.append(9)
# print(lists.sort())
# print(lists.sort(reverse=True))
# print(lists.insert(4,5))
# print(lists.reverse())
# print(lists.remove(1))
# print(lists.count(7))
# lists.pop(1)
# print(lists)

# lists=["kgf","kantara","su from so"]
# print(lists)

# movies=[]
# mov1=movies.append(input("enter a first movie:" ))
# mov2=movies.append(input("enter a second movie:" ))
# mov3=movies.append(input("enter a third movie:" ))
# print(movies)



#           DICTIONARY


# info = {
#      "name":"uday",
#      "subjects":["cn","dbms","os","ml"],
#      "loction":"bglr",
#      "age":23,
#      "marks":90.98
#  }
# print(info)
# info={"name":["manu"]},
# print(type(info))
# print(info)



# student={
#     "name":input("enter student name:"  ),
#     "age":input("enter student age:"),
#     "subjects":input("enter student subjects :"),
#     "marks":input("enter student marks :"),
# }
# print(student)




# info={
#    "python":input("enter marks"),
#    "java":input("enter a marks"),
#    "c":input("enter a marks"),
# }
# print(info )

            #WHILE LOOP


# count = 1
# while count<=5:
#     print("hello")
#     count +=2



# i=1
# while i<=100:
#     i+=1
#     print(i)
# print("lop endded")



# n=int(input("enter anumber :"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1


# num=[2,3,4,5,6,45,43,23,23,21]
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

#     or


# heros="yash","sudeep","raj b shetty","rishab shetty","uday"
# film=0
# while  film < len(heros):
#        print(heros[film])
#        film +=1



# IF CONDITON

# num =(12,21,34,54,64,65)
# x=34
# i=0
# while  i < len(num):
#   if num[i]==x:
#      print("findind loop")
#      print(i)
#   i+=1
# else:
#    print("loop end")


#   BREAK AND CONTINUE


# i=0
# while  i <= 5:
#     if (i%2 !=0):
#       i += 1
#       continue
#     print(i)
#     i+=1
    
# nums=[12,5,4,6,36,3,66]
# i=0
# while  i<len(nums):
#       print(nums[i])
#       i +=1


# num=[1,4,9,16,25,36,49,64,81,100]
# x=25
# idx=0
# while idx<len(num):
#     if num[idx]==x:
#       print(x)
#     idx+=1

# n=int(input("enter a number"))
# sum=1
# for i in range(1,n+1):
#     sum +=i
# print(sum)


# n=5
# fact=1
# i=1
# while  i<=n:
#     fact *=i
#     i +=1
# print(fact)


# n=int(input("enter a number:"))
# def call__fuc(usd):
#     ind=usd*83
#     print(usd,"usd",ind,"ind")
# call__fuc(n)

# n=5
# fact=1
# i=1
# while i<=n:
#     fact+=i
#     i+=1
# print(fact)


# def fact(n):
#     if  n==0 or n==1:
#         return 1
#     return fact(n-1)*n
# print(fact(5))


def fib(n):
    if n==0:
        return 1
    return fib(n-1)+n
val=fib(5)
print(val)
