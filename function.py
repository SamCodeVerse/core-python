# def hello():
#     for i in range(10):
#         print("hello")

# hello()
# hello()

# c=6 
# def add():
#     print(c)
#     x=6

# # print(x)
# add()

# print("outer c",c)

# def add():
#     return 2+4
  

# print(add())
# add()

# def numberCheck(a):
#     
#     if a%2==0:
#         return "number is even"
#     return "number is odd"

# print(numberCheck(5))

# def add(a,b):
#     return a-b

# print(add(b=2,a=5))

# def order(name,city='Jalandhar',age=18):
#     print('name: ',name)
#     print('city:',city)
#     print('age:',age)

# order('aman',age=23)

# def order(*args):
#     print("order is ",args)

# order('pizza','thumsup','burger')


# def details(**a):
#     print(a)

# details(name='karan',age=32,order_no=3242)


# task1
# def greet():
#     for i in range(3):
#         print('welcome to python programming')
# greet()        

# task2
# def add_numbers(a,b):
#     return(a+b)
# print(add_numbers(10,20))

# task3
# def check_even_odd(a):
#     if a%2==0:
#         print('number is even')
#     else:
#         print('number is odd')    
# check_even_odd(4)  

# task4   
# def largest(a,b):
#     if a>b:
#         return a
#     else:
#         return b 
# print(largest(45,66))       

# task5
# def student_result(marks):
#     if marks>40:
#         print('pass')
#         if marks>=80:
#          print('grade A')
#         elif marks>=60:
#            print('grade B')
#         elif marks>=40:
#            print('grade C')
#     else:
#        print('fail')
# marks=int(input('enter the marks:')) 
# student_result(marks)             

#task6 
# def list_sum(a,b,c):
#     return(a+b+c)
# print(list_sum(10,20,30))

# task7
# def palindrome_checker(word):
#     if word==word[::-1]:
#         print('palindrome')
#     else:
#         print('not palindrome')
# word=input('enter the word:')
# palindrome_checker(word)        

#task8 
# def salary_bonus(salary):
#     if salary>50000:
#         bonus=salary*20/100
#     elif salary>30000:
#         bonus=salary*10/100
#     else:
#         bonus=salary*5/100
#     total_salary=salary+bonus
#     print('bonus',bonus)
#     print('total salary',total_salary)
# salary=int(input('enter the employee salary:'))
# salary_bonus(salary)                
 
# task9
# def login_system(username,password):
#     newusername='admin'
#     newpassword=353463
#     for i in range(1):
#         if username==newusername and password==newpassword:
#             print('login successful')
#         else:
#             print('account blocked')
# username=input('enter the username:') 
# password=input('enter the password:') 
# login_system(username,password)              

# task10
# def libarary_system():
#     book=['english','maths','python','html','css']
#     for i in range(1):
#         books=input('enter the name of book:')
#         if books in book:
#             print('book is avaailable')
#         else:
#             print('book is not available') 
# libarary_system()            
 
    

# li=[]

# def add():
#     a=input("enter your element:")
#     li.append(a)

# def remove():
#     a=input('enter the element you want to remove:')
#     if a in li:
#         li.remove(a)
#     else:
#         print('element not found')    

# def view():
#     print(li)

# while True:
#     print('1.add')
#     print('2.remove')
#     print('3.view')
#     print('4.exit')
#     choice=int(input('enter your choice:'))
#     if choice==1:
#         add()
#     elif choice==2:
#         remove()
#     elif choice==3:
#         view()
#     elif choice==4:
#         exit
#         break
#     else:
#         print('invalid choice')        
            
# balance=10000
# def deposit(balance):
#     amount=int(input('enter the deposited amount:'))
#     balance=balance+amount

# def withdraw():
#     amount=int(input('enter the amount withdrawl:'))
#     if amount<=balance:
#         balance=balance-amount
#         print('your balance is:',balance)
#     else:
#         print('insufficient balance')

# def check(balance):
#     print('check balance',balance)

# while True:
#     print('1.deposit')
#     print('2.withdrawl')
#     print('3.check')
#     print('4.exit')
#     choice=int(input('enter your choice:'))
#     if choice==1:
#         deposit(balance)
#     elif choice==2:
#         withdraw()
#     elif choice==3:
#         check(balance)
#     elif choice==4:
#         exit
#         break
#     else:
#         print('invalid choice')      
# 
# 
#                            
    
    
