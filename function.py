# what is function?
# function is a block of code which is
# executed only when it is called.

# types of function
# 1. built in function: print(), input(), len(), etc
# 2. user defined function: which is created by user

# def hello():
#     print("Hello World")
#
# hello()
# hello()

# def add(x,y):
#     print(x+y)
#
# add(10,20)
# add(30,40)

# def total(numbers):
#     sm =0
#     for a in numbers:
#         sm+=a
#     print(sm)
#
# total([1,2,3,4,5,6,7,8,9,10])

# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sita', 'gender': 'female', 'status': True},
#     {'name': 'hari', 'gender': 'male', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': False},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
# ]


# function return value

# def message():
#     name ='ram'
#     name1 ='sita'
#     return [name,name1]
#
# print(message())
#
# def add(x,y):
#     return x+y
#
# print(add(10,20))

# def add_sub(x,y):
#     tot =x+y
#     sub =x-y
#     return [tot,sub]
#
# print(add_sub(10,20))
#
# def a():
#     return "hello"
#
# def b():
#     print(a())
#
# b()


# def take_value():
#     p, t, r = 10, 20, 40
#     return [p, t, r]
# def calculator():
#     x  = take_value()
#     p = x[0]
#     t = x[1]
#     r = x[2]
#     return p*t*r/100
#
# def display():
#     print(calculator())
# display()

nep =int(input("Enter nepali marks: "))
eng =int(input("Enter english marks: "))
math =int(input("Enter math marks: "))
sci =int(input("Enter science marks: "))
comp =int(input("Enter computer marks: "))

def total():
    return nep+eng+math+sci+comp
def percentage():
    return total()/5
def grade():
    per = percentage()
    if per>=80:
        return "A+"
    elif per>=60:
        return "A"
    elif per>=40:
        return "B"
    elif per>=20:
        return "C"
    else:
        return "D"

def result():
    print("Total marks:",total())
    print("Percentage:",percentage())
    print("Grade:",grade())

result()
