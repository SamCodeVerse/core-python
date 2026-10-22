# a={'name':'naveen','rollno':1233}
a={}
# print(len(a))

# print(type(a))

# c=['mango','orange','banana']

# d=a.fromkeys(c,'na')

# print(d)

# print(a['rollno'])

# a['Class']="MCA"

# print(a.get('name'))

# a.update({'name':'sameer','class':'BA'})

# a.pop('name')

# a.popitem()

# print(a.keys())
# print(a.values())

# print(a.items())

# a=dict([('name','aman'),('class','BCA')])
# a.clear()

# del a

# for i in a:
#     print(i,a[i])

# print(a)



# a={
#     'child1':
#     {
#         'name':'john',
#         'age':23
#      },
#     'child2':
#      {
#         'name':'adam',
#         'age':45
#         }
#     }

# print(a)

# CHILD1

# name : john
# age : 23

# child2

# name : adam
# age : 45

# a={'child1':{'name':'john','age':23}}
# print(a)

# a={
#     'child1':
#     {
#         'name':'john',
#         'age':23
#      },
#     'child2':
#      {
#         'name':'adam',
#         'age':45
#         }
#     }
# for i in a:
#     print(i)
#     print()
#     print('name:',a[i]['name'])
#     print('age:',a[i]['age'])
    

# a={}
# n=int(input('number of times you have to enter:'))
# for i in range(n):
#     name=input('enter the name:')
#     age=int(input('enter the age:'))
#     Class=input('enter the class:')
#     a[name]=age
# print(a)   


# a={}
# for i in range(3):
#     key=input("enter your key: ")
#     value=input("enter your value: ")
#     # a[key]=value
#     a.update({key:value})

# print(a)

# task1
# a={'name':'sameer','age':20,'city':'jalandhar'}
# print(a)

# task2
# a={'name':'sameer','age':20,'city':'jalandhar'}
# print(a.get('city'))

# task3
# a={}
# for i in range(3):
#     key=input('enter your input:')
#     value=input('enter your value:')
#     a[key]=value
# print(a)    

# task4
# a={'name':'john','age':'20','city':'jalandhar'}
# print(type(a))

# task5
# a={'integer':23,'name':'jack','float':2.04}
#  print(a)

# task6
# a={'name':'john','age':'20','city':'jalandhar'}
# a.update({'name':'jack'}) 
# print(a)

# task7
# a={'name':'john','age':'20','city':'jalandhar'}
# a.update({'class':'b.tech'})
# print(a)

# task8
# a={'name': 'john', 'age': '20', 'city': 'jalandhar', 'class': 'b.tech'}
# a.pop('name')
# print(a)

# task9
# a={'name': 'john', 'age': '20', 'city': 'jalandhar', 'class': 'b.tech'}
# b=a.copy()
# print(b)

# task10
# a={'name': 'john', 'age': '20', 'city': 'jalandhar', 'class': 'b.tech'}
# print(len(a.keys()))

# task11
# a={}
# for i in range(1):
#     name=input('enter your name:')
#     age=int(input('enter your age:')) 
#     a[name]=age
# print(a)    

# task12
# a={}
# for i in range(1):
#     subjectname=input('enter the name of subject:')
#     marks=int(input('enter the marks:'))
#     a[subjectname]=marks
# print(a)    

# task13
# product={}
# for i in range(1):
#     name=input('enter the name of product:')
#     price=int(input('enter the price of product:'))
#     product[name]=price
# print(product)    

# task14
# a={'num1':{'mango'},'num2':{'watermelon'}}
# print(a) 

# task15
# a={'city':'jalandhar','temprature':40}
# print(a)

# task16
# a={'name':'jack','city':'jalandhar','course':'python'}
# c=input('enter yor key: ')

# avail=False

# for i in a.keys():
#     if c==i:
#         avail=True

# if avail:
#     print("key exists")
# else:
#     print('key doesnot exist')

# task17
# a={'name':'john','age':19}
# if a['age']>18:
#     print('age is greater than 18')
# else:
#     print('age is smaller than 18')    

# task18
# a={'name':'john','age':19,'marks':75}
# if a['marks']>40:
#     print('pass')
# else:
#     print('fail')    

# task19
# value={'a':34,'b':65}
# if value['a']>value['b']:
#     print('a is greater')
# else:
#     print('b is greater')    

# value={'a':34,'b':650,'c':4,'d':780,'e':860}
# c=1000
# for i in value.values():
#     if c>i:
#         c=i

# print('graeter number is: ',c)

#task20
# product={'name':'bottle','quantity':0}
# if product['quantity']==0:
#     print('the quantity is zero')
# else:
#     print('the quantity is not zero')    

# task21
# a={'name':'john','age':19}
# if a['age'] %2==0:
#     print('number is even')
# else:
#     print('number is odd')    

# task22
# user={'password':34568}
# password=int(input('enter your password:'))
# if user['password']==password:
#     print('welcome')
# else:
#     print('try again')    

# task23
# wheather={'city':'jalandhar','temprature':34}
# if wheather['temprature']>35:
#     print('high temprature')
# else:
#     print('low temprature')  

# task24 
# a={'salary':65000}
# if a['salary']>50000:
#     print('is greater')
# else:
#     print('is smaller')      

# task25
# a={'username':'bill','password':24323}
# username=input('enter your name:')
# if a['username']==username:
#     print('welcome')
# else:
#     print('try again')    

# task26
# a={'name':'joe','mark':[45,56,78]}
# print(a)

# task27
# a={'food':['pulses','maggi','parantha','juice','egg']}
# print(a)

# task28
# a={'subjects':['hindi','english','evs','maths']}
# print(a) 

# task29
# student={'marks':[45,56,78]}
# student['marks'].append(89)
# print(student)

# task30
# student={'marks':[45,56,78]}
# print(student['marks'][1])

# task31
# a={'coordinates':(20,30)}
# print(a['coordinates'])

# task32
# a={'date':(3,10,2026)}
# print(a)

# task33
# a={'date':(3,10,2026)}
# print(a['date'][1])

# task34
# a={'date':(3,10,2026)}
# a['date']=(4,10,2026)
# print(a)

# task35
# a={'date':(3,10,2026)}
# print(type(a['date']))

# task41
# book={'title':'gulliver travels','price':250,'author':'jonathan swift'}
# print(book) 

# task42
# mobileinfo={'brand':'realme','RAM':8,'price':20000}
# print(mobileinfo)

# task43
# car={'name':'hotwheels car','price':450}
# car['price']=550
# print(car)

# task46
a={'name':'john','account number':'135623','balance':1500}
if a['balance']>1000:
    print('sufficient balance')
else:
    print('insufficient balance')    