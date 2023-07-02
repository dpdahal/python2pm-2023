# # x=6
# # y=8
# # z=90

# # if x>y and x>z:
# #     print("x is greater")
# # elif y>x and y>z:
# #     print("y is greater")
# # elif x==y and x==z:
# #     print("All are equal")
# # else:
# #     print("z is greater")


# x=10

# if x>5:
#     a =50
#     if a>20:
#         pass


# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# # c = int(input("Enter c : "))

# a=50
# b=6
# c=60

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")

# username
# password
# admin admin002
# user user002


# username = input("Enter username : ")
# password = input("Enter password : ")

# if username=='admin' and password=='admin002' or username=='user' and password=='user002':
#     print("Login Success")
# else:
#     print("Login Failed")


# data =['ram','sita','gita']

# if 'ram' in data:
#     print("ram is in data")



# name = input("Enter name : ")
# print(name)

print("product: 1.iphone(Rs: 200000) 2.samsung(Rs:10000) 3.nokia(rs:5000)")
product = int(input("Enter product : "))
total_price =0
quantity=0
product_name=''
if product==1:
    quantity = int(input("Enter quantity : "))
    total_price = quantity*200000
    product_name='iphone'
elif product==2:
    quantity = int(input("Enter quantity : "))
    total_price = quantity*10000
    product_name='samsung'
elif product==3:
    quantity = int(input("Enter quantity : "))
    total_price = quantity*5000
    product_name='nokia'
else:
    print("Invalid product")
print("Product Name : ",product_name)
print("Total Quantity : ",quantity)
print("Total Price : ",total_price)

