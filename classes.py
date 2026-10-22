# class person:

#     # name='naveen'
#     # occ='developer'
#     # emp_id=23434

#     def __init__(self):
#         self.name='joy'
#         self.occ='digital marketer'
#         self.empid=23452
#         # print("this is init function")
#         # print(f'name {self.name} \noccupation {self.occ} \nemployee id {self.emp_id}')
#     def change(self):
#         self.name='jack'
#         self.occ='backend developer'
#     # def show(self):
#     #     print(f'name {self.name} \noccupation {self.occ} \nemployee id {self.emp_id}')


# a=person()

# a.change()

# print(a.name)
# b=person()
# a.name='aman'
# b.name='joy'

# print(a.name)
# print(b.name)
# print(a.occ)
# a.show()


# class Person:
#     def __init__(self,name,occ,id):
#         self.name=name
#         self.occ=occ
#         self.id=id

#     def show(self,salary):
#         print(f'name {self.name} \noccupation {self.occ} \nemployee id {self.id}')
#         print(salary)


# a=Person('jack','python developer',223445)
# b=Person('joy','digital marketer',234534)

# # a.name='josaf'

# print(a.name)
# print(b.name)
# a.show(4523543)


# class calculator:
#     def add(self,a,b):
#         print('addition:',a+b)
#     def sub(self,a,b):
#         print('subtraction:',a-b)
#     def multiply(self,a,b):
#         print('multiplication:',a*b)
#     def divide(self,a,b):
#         if b!=0:
#             print('division:',a/b)
#         else:
#             print('cannot be divided by zero')
# c=calculator()
# a=int(input('enter your first number:'))
# b=int(input('enter the second number:'))
# c.add(a,b)
# c.sub(a,b)
# c.multiply(a,b)
# c.divide(a,b)         
                   

# class bankingaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     def display(self,balance):
#         self.name        
# balance=bank('jack',5000)
# while TRUE:
#     print("1.deposit")
#     print("2.withdrawl")
#     print('3.check balance')
#     print('4.exit')
#     choice=input('enter your choice:')
#     if choice=='1':
#         amount=int(input('enter amount to deposit:'))
#         balance.deposit()
#     elif choice=='2':
#         amount=int(input('enter amount to withdrawl:'))
#         balance.withdrawl(amount)
#     elif choice=='3':
#         balance.checkbalance()
#     elif choice=='4':
#         print('exit')
#         break
#     else:
#         print('invalid choice')

# class bank:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print('successfully deposit')
#     def withdrawl(self,amount):
#         if amount<=self.balance:
#             self.balance=self.balance-amount
#             print('withdrawl successfully')
#         else:
#             print('insufficient balance')
#     def checkbalance(self):
#         print('account holder:',self.name) 
#         print('balance:',self.balance)                                       
# account=bank('jack',5000)
# while True:
#     print("1.deposit")
#     print("2.withdrawl")
#     print('3.check balance')
#     print('4.exit')
#     choice=input('enter your choice:')
#     if choice=='1':
#         amount=int(input('enter amount to deposit:'))
#         account.deposit(amount)
#     elif choice=='2':
#         amount=int(input('enter amount to withdrawl:'))
#         account.withdrawl(amount)
#     elif choice=='3':
#         account.checkbalance()
#     elif choice=='4':
#         print('exit')
#         break
#     else:
#         print('invalid choice')


# class Car:
#     def wheel(self):
#         print('four wheel')

# class honda(Car):
#     def speed(self):
#         print('have 200 speed')

# o=honda()

# o.speed()
# o.wheel()

# class A:
#     def showA(self):
#         print('this is class A')
# class B(A):
#     def showB(self):
#         print('this is class B')

# class C:
#     def showC(self):
#         print('this is class C')

# class D(C,B):
#     def showD(self):
#         print('this is class D')


# a=D()

# task1
# class animal:
#     def eat(self):
#         print('animal is eating')
# class dog(animal):
#     pass

# d=dog()
# d.eat()
            
# task2
# class person:
#     def show_name(self):
#         print('my name is jack')
# class student(person):
#     pass
# s=student()
# s.show_name()        

# task3
# class calculator:
#     def add(self,a,b):
#         print('addition:',a+b)
# class advancedcalculator(calculator):
#     def multiply(self,a,b):
#         print('multiplication:',a*b) 
# c=advancedcalculator()
# c.add(10,5)


# task4
# class vehicle:
#     def start(self):
#         print('vehicle started')
# class car(vehicle):
#     def drive(self):
#         print('car is driving')
# class bike(vehicle):
#     def ride(self):
#         print('bike is riding')
# c=car()
# c.start()
# c.drive()

# b=bike()
# b.start()
# b.ride()

# task5 
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class manager(employee):
#     def show(self):
#         print('name:',self.name)
#         print('salary:',self.salary)
# m=manager('aman',1000)
# m.show()         

#task6    
# class person:
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self, name,marks):
#         super().__init__(name)
#         self.marks=marks
#     def show(self):
#         print('name:',self.name)
#         print('marks:',self.marks)
# s=student('jack',56)
# s.show()        

# class Car:
#     def move(self):
#         print('move')
# class Boat:
#     def move(self):
#         print('slay')
# class Plane:
#     def move(self):
#         print('fly')

# a=Car()
# b=Plane()
# c=Boat()

# a.move()
# b.move()
# c.move()


# class BankAcc:
#     def __init__(self):
#         self.name="naveen" # public
#         self._Accno=234323423424  #protected
#         self.__pin=1234  # private

#     def show(self):
#         print(self.__pin)


# a=BankAcc()

# print(a.name)
# print(a._Accno)
# # print(a.__pin)

# a.show()


# task1
# class dog:
#     def sound(self):
#         print('dog is barking')
# class cat:
#     def sound(self):
#         print('cat says meow')

# a=dog()
# b=cat()
# a.sound()
# b.sound()           

# task2 
# class calculator:
#      def add(self,a,b):
#          print('addition:',a+b)
# c=calculator()
# c.add(50,20)     

# task3
# class circle:
#     def area(self):
#         print('circle area:',3.14*10*10)
# class rectangle:
#     def area(self):
#         print('rectangle area:',20*5)
# c=circle()
# r=rectangle() 
# c.area()
# r.area()               

# task4
# class student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def show(self):
#         print('marks:',self.__marks)
# a=student(76)
# a.show()    

# task5
# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def show(self):
#         print('balance:',self.__balance)
# a=bankaccount(5000)
# a.show()      

#task6   
# class user:
#     def __init__(self,password):
#         self.__password=password
#     def show(self):
#         print('password:',self.__password)
# a=user(234234)
# a.show()                    

# task7
# class car:
#     def start(self):
#         print('porshe')
# class bike:
#     def start(self):
#         print('hill cat')
# a=car()
# b=bike()
# a.start()
# b.start()                

# task8
# class manager:
#     def calculate_salary(self):
#         print('manager salary:60000')
# class develpor:
#     def calculate_salary(self):
#         print('develpor salary:40000')
# a=manager()
# b=develpor() 
# a.calculate_salary()
# b.calculate_salary()              

# task9
# class animal:
#     def sound(self):
#         print('a sound of animal')
# class dog:
#     def sound(self):
#         print('dog is barking')
# class cat:
#     def sound(self):
#         print('cat says meow')
# a=animal()
# b=dog()
# c=cat()
# a.sound()
# b.sound()
# c.sound()                        

# task10
# class emailnotification:
#     def send(self):
#         print('you got a email')
# class smsnotification:
#     def send(self):
#         print('you got a sms')
# a=emailnotification()
# b=smsnotification()
# a.send()
# b.send()                

# task11
# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print('deposit successful')
#         else:
#             print('invalid amount')
#     def show_balance(self):
#         print('balance:',self.__balance)
# a=bankaccount(10000)
# a.deposit(500)
# a.show_balance()

# task12
# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def withdrawl(self,amount):
#         if amount<=0:
#             print('invalid amount')
#         elif amount<=self.__balance:
#             self.__balance-=amount
#             print('withdrawl successful')
#         else:
#             print('insufficient balance')        
#     def show_balance(self):
#         print('balance:',self.__balance)
# a=bankaccount(10000)
# a.withdrawl(500)
# a.show_balance()

# task13
# class person:
#     def __init__(self,age):
#         self.__age=0
#         self.set_age(age)
#     def set_age(self,age):
#         if age>=0:
#             self.__age=age 
#         else:
#             print('invalid age')
#     def show_age(self):
#         print('age:',self.__age)
# a=person(20)
# a.show_age()
# a.set_age(-49)
# a.show_age()                       

# task14
# class product:
#     def __init__(self,price):
#         self.__price=price
        