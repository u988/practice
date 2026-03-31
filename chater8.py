# class car:
#     def __init__(self,name):
#         self.name1=name
#         print("adding car in database")
# s1=car("bmw")
# print(s1.name1)


# class student:
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
#         print("adding student in database")
# s1=student("uday",89)
# print(s1.name,s1.marks)
# s2=student("manu",99)
# print(s2.name,s2.marks)
        
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hii",self.name,"your avg score is:",sum/3)

s1=student("uday",[90,89,78])
s1.avg()



 
