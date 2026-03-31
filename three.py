# def Udaya():
#     for i in range(1,4):
#         print(i)
#     print("How are you my baby")

# Udaya()



# a=int(input("enter first number"))
# b=int(input("enter a second number"))
# def sum(a,b):
#     s=a+b
#     return s
# print(sum(a,b))


# recursion

# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
# show(10)

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n *fact(n-1)
# print(fact(8))



# def show(n):
#     if n==0:
#         return 0
#     return show(n-1)+n
# sum=show(7)
# print(sum)

# f = open("demo.txt","r")
# # f.write("my name udaykumar")
# f.read()
# f.close()



# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)


# with open("demo.txt","w") as f:
#     f.write("i am from shimoga")



with open("practice.txt","r")as f:
    data = f.read()

    new_data=data.replace("python","c")
    print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)









