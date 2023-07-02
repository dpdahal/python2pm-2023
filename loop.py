# what is loop?
# loop is a way to repeat a task
# there are two types of loop
# 1. for loop: for loop is used to iterate over a sequence
# 2. while loop: while loop is used to
# iterate over a block of code as
# long as the condition is true
# 3. Nested loop: nested loop is a loop inside a loop

# data = [12, 34, 66, 56, 76]
#
# a = 6
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# for num in data:
#     print(num)
#
# for a in range(1,11):
#     print("hello python")

# for a in range(1,11):
# data = [12, 11, 23, 44, 56, 77]
# # count total even and odd number from a list
# total_even=0
# total_odd=0
# for num in data:
#     if num % 2 == 0:
#         total_even += 1
#     else:
#         total_odd += 1
#
# print("total even number is", total_even)
# print("total odd number is", total_odd)

# data = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]
#
# for num in data:
#     for a in num:
#         print(a)

# 1-10
# 10-1
# for x in range(1, 11,2):
#     print(x)
#
# for x in range(10, 0, -1):
#     print(x)

# for x in range(1,11):
#     for i in range(1,11):
#         print(x,"*",i,"=",x*i)


# WAP to enter number of students
# and their marks in five subjects
# and print total marks and average marks

# x=1
# while x<=10:
#     if x%2==0:
#         print(x)
#     x+=1

# x=1
# num = int(input("enter a number"))
# while x<=num:
#     print("Hello python")
#     x+=1
#
# data =['ram','sita','gita','hari']

# x=1
# num = int(input("enter a number: "))
# names =[]
# while x<=num:
#     name = input("enter a name: ")
#     names.append(name)
#     x+=1
#
# a =0
# while a<len(names):
#     print(names[a])
#     a+=1
#
# b =1
# num = int(input("enter a number: "))
# while b<=10:
#     print(num,"*",b,"=",num*b)
#     b+=1

# data = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]
#
# x = 0
# while x < len(data):
#     y = 0
#     while y < len(data[x]):
#         print(data[x][y])
#         y += 1
#     x += 1

# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sita', 'gender': 'female', 'status': True},
#     {'name': 'hari', 'gender': 'male', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': False},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
# ]
# total_user = len(data)
# total_active_user = 0
# total_male = 0
# total_female = 0
# total_inactive_user = 0
# total_active_male = 0
# total_inactive_male = 0
# total_active_female = 0
# total_inactive_female = 0
#
# for user in data:
#     if user['status'] == True:
#         if user['gender'] == 'male':
#             total_active_male += 1
#         if user['gender'] == 'female':
#             total_active_female += 1
#
#         total_active_user += 1
#     else:
#         if user['gender'] == 'male':
#             total_inactive_male += 1
#         if user['gender'] == 'female':
#             total_inactive_female += 1
#
#     total_inactive_user += 1

students=[
    {'name':'ram','marks':{'nep':78,'sc':56,'en':67,'ma':89,'cm':90}},
    {'name':'ram','marks':{'nep':78,'sc':56,'en':67,'ma':89,'cm':90}},
    {'name':'ram','marks':{'nep':78,'sc':56,'en':67,'ma':89,'cm':90}},
]
