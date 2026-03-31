# class student:
#     name="uday"
# S1=student()
# print(S1.name)



# class car:
#     color = "red"
#     brand = "toyota"
# cars = car()
# print(cars.color)
# print(cars.brand)

# cars1= car()           # 2 times same value print
# print(cars.color)
# print(cars.brand)
 

#   --INIT-- FUNCTION

# class Student:

#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks=marks
#         print("adding new student")


# s1=Student("uday",90)
# print(s1.name,s1.marks)
    
# s2=Student("arjun",90)
# print(s2.name,s2.marks)


#   CLASS AND OBJECT ATTRIBUTE( MAIN PREFERENCEE OBJECT ATTRIBUTE)

# class student:
#     colloge_name="nmit"
#     name="manu"  #class attribute
#     def __init__(self,name):
#         self.name=name  #object attribute
#         print("adding new student")
# s1=student("uday")
# print(s1.name)



#      METHODS


# class student:
#     @staticmethod
#     def col():
#         print("nmit")

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print("welcome student",self.name) 
#     def get_marks(self):
#         return self.marks

# s1=student("uday",90)
# s1.col()
# s1.welcome()
# print(s1.get_marks())




#  WAP

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hii",self.name,"your avg score is",sum/3)

# s1=student("uday",(45,67,90))
# s1.get_avg()



#    OOPS CONCEPT 4 PILLERS
#    1. ABSTRACTION  (hiding the implementation details of a class and showing the essintial features to the user )
#    2. ENCAPSULATION ( wrapping data and functions into a single unit(object))
#    3. INHERITANCE
#    4.  POLYMORPHISOM



#    WAP


# class account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.acount=acc
#     def debit(self,amount):
#         self.balance -= amount
#         print("your rs",amount,"has debited")
#         print("total balance =",self.get_balance())

#     # def balanc(self,amount):
#     #     self.account -=amount
#     #     print("insufficient balance",amount())
        

#     def credit(self,amount):
#         self.balance += amount
#         print("your rs",amount,"was credited")
#         print("total balance =",self.get_balance())
    
#     def get_balance(self):
#         return self.balance
    
# acc1=account(10000,12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.debit(40000)

#    delete function

# class student:

#     def __init__(self,name,age):
#         self.names=name
#         self.age = age
#         print("adding new student")

# s1=student("uday",23)
# print(s1.names,s1.age)
# del s1.names
# print(s1.names)


#    PRIVATE FUNCTION

# class account:
#     def __init__(self,account,password):
#         self.account=account
#         self.password=password
#     def reset(self):      # hide the password  
#         print(self.password)        

# acc=account("8055","uday")
# print(acc.account)
# print(acc.reset)
        
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)
# cal_fact(5)



# def sum(n):
#    if n==0:
#       return 0
#    return sum(n-1)+n
# sum1=sum(5)
# print(sum1)

# class car():
#     def __init__(self):
#             self.acc=False
#             self.clutch=False
#             self.brek=False
#     def start(self):
#           if self.acc and self.clutch :
#                 print("car is started")
#           else:
#                 print("car is not started")
# s1=car()
# s1.acc=True
# s1.clutch=False
# s1.start()



# class account():
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.acc=acc
#     def debit(self,amount):
#         if amount > self.balance:
#             print("insufficient balance")
#         else:
#             self.balance-=amount
#             print(amount,"amount is debited")
#         print("total balance is",self.get_balance())
        
#     def credit(self,amount):
#         self.balance+=amount
#         print(amount,"amount is credited")
#         print("total balance is",self.get_balance())

#     def get_balance(self):
#         return self.balance
    

# acc1=account(10000,1234)
  
# acc1.debit(11000) 

# acc1.credit(500)   


# class car():
#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("car stopped")
# class toyota(car):
#     def __init__(self,name):
#         self.name=name
# car1=toyota("fortuner")
# print(car1.name)
# print(car1.stop())


class a():
    name="uday"

    def  na(cls,name):
        cls.name=name

a1=a()
a1.na("kgf")
print(a1.name)
print(a.name)




        



