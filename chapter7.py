
# with open("demo.txt","w")as f:
#     f.write("today is sunday")
# with open("demo.txt","r")as f:
#     data=f.read()
#     print(data) 

# f=open("demo1.txt","w")
# f.write("hii uday")
# f.close



# DELETING A FILE
# import os
# os.remove("demo.txt")

# PRACTICE QUESTION


# with open("demo2.txt","w")as f:
#     f.write("hii uday\nwe are learning file i/o using java\ni like programming in java")

# with open("demo2.txt","r")as f:
#     data=f.read()
#     print(data)

# new_data=data.replace("java","python")
# print(new_data)

# with open("demo2.txt","w")as f:
#     f.write(new_data) 

# def cacl():
#     with open("demo2.txt","r")as f:
#         data=f.read()
#         if(data.find("python")!=-1):
#             print("found")
#         else:
#             print("not found")
# cacl()


# with open("demo2.txt","r")as f:
#     data=f.read()
#     new_data=data.replace("python","java")
#     print(new_data)
# with open("demo2.txt","w")as f:
#     f.write(new_data)

# def find_line():
#     word="programming"
#     data=True
#     line=1
#     with open("demo2.txt","r")as f:
#         while data:
#             data=f.readline()
#             if  word in data:
#                 print(line)
#                 return
#             line +=1
#         return-1
# find_line()

# def find():
#     word="ml"
#     data=True
#     line=1
#     with open("demo2.txt","r")as f:
#         while data:
#             data=f.readline()
#             if word in data :
#                 print(line)
#                 return
#             line +=1
#     return-1
# print(find())          


# count=0
# with open("demo2.txt","r")as f:
#     data=f.read()

#     num=data.split(",")
#     for val in num:
#         if (int(val)%2==0):
#             count +=1
# print(count)
with open("dem.txt","r")as f:
    data=f.read()
    print(data)