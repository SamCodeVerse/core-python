# print("hello")


# try:
#     v=7
#     print(v)
#     a=int(input("enter the value of a: "))

# except NameError:
#     print("first define v")
# except ValueError:
#     print("please enter only intiger value")

# a=int(input("enter the value of a: "))

# try:
#     g=6
#     print(g)
#     # int('kjsdfl')
# except Exception as e:
#     print(e)
# finally:
#     print("this is finally massage")

# a=9
# b=7

# if a>b:
#     raise SyntaxError("a is greater then b")


# # print(v)
# print("this is below message")

# task1
# try:
#    a=int(input('enter your first number:'))
#    b=int(input('enter your second number:'))
#    result=a/b
#    print('result',result)

# except ZeroDivisionError:
#  print('error:cannot be divided by zero')

# task2  
# try:
#     a=int(input('enter the an integer:'))
#     print('you entered number a',a)
# except ValueError:
#     print('invalid input!please enter a valid integer')    

# task3
# try:
#     a=int(input('enter the first number:'))
#     b=int(input('enter the second number:'))
#     result=a/b
#     print('result',result)
# except ZeroDivisionError:
#     print('division by zero is not allowed')    

# task4
# try:
#    a=[45,34,56,78]
#    print(a[4])
# except IndexError:
#    print('index error:invalid index')

# task5
# try:
#     # a={'student name':['john,ajay,jack']}
#     students={'name1':'john','name2':'jack','name3':'oggy'}
#     print(students['name4'])
# except KeyError:
#     print('student not found')    

# task7
# try:
#     a=int(input('enter the first number:'))
#     b=int(input('ente the second number:'))
#     print(a/b)
# except ValueError:
#     print('invalid number entered')
# except ZeroDivisionError:
#     print('division by zero is not allowed')       

# task8 

# password=input('enter the password:'))
# if len(password)<8:
#     raise SyntaxError('password must contain at least 8 characters')
# print('password accepted')

# task9
# age=int(input('enter the age here:'))
# if age<0:
#     raise ValueError('invalid age entered')
# print('valid age')

# task10
# age=int(input('enter the age here:'))
# if age<18:
#     raise ValueError('you are not eligible to vote')
# print('eligible to vote')

# task11
# number=int(input('enter the number here:'))
# if number<0:
#     raise SyntaxError('number must be positive')
# print('positive number')

# task12
# username=input('enter username here:')
# password=int(input('enter the passord here:'))
# if username=='admin' or password=='23453':
#     raise SyntaxError('invalid username or password')
# print('login successful')

# task13
# marks=int(input('enter the marks:'))
# if marks<0 or marks>100:
#     raise SyntaxError('marks should be between 0 and 100')
# print('valid marks')

# task14
# amount=int(input('enter the amount here:'))
# if amount>10000:
#     raise ValueError('insufficient balance')
# print('sufficient balance')

# task15
# try:
#     a=int(input('enter first subject marks:'))
#     b=int(input('enter the second subject marks:'))
#     c=int(input('ente third subject marks:'))
#     d=int(input('enter the fourth subject:'))
#     e=int(input('ente the fifth subject:'))
# except SyntaxError:
#     print('write the values in number')