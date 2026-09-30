# a=[]

# print(type(a))

# fruits=['mango','banana',"apple"]

# print(fruits[1])

# fruits[0]="cherry"

# print(fruits)

# print(len(fruits))

# print(fruits[0][0])

# print(fruits.count('apple'))

# a="this is a python variavle"

# print(a.split())
# b=a.split()

# print(type(b))
# print(b[0])

fruits=['mango','Banana',"apple"]

# fruits.append("cherry")
# fruits.insert(1,'cherry')

# fruits.extend(['cherry','watermelon'])

# fruits.pop(1)

# fruits.remove("banana")

# b=fruits
# print(fruits.sort(reverse=True))

# fruits.clear()

# del fruits

# fruits.reverse()

# print(fruits)

# a="python"

# for i in fruits:
#     print(i)

 
# l=len(fruits)

# i=0
# while i<l:
#     print(fruits[i])
#     i+=1

# fruits=['mango','Banana',"apple"]

# print(fruits.index('apple'))


# a=[2,3,4,5,63,4,56,7,3,0,1,0,0,1,True,False]

# print(a.count(True))
# fruits=['mango','Banana',"apple",'kiwi']
# i=0
# while i<len(fruits):
#     print(i+1,fruits[i])
#     i+=1

#task1
# numbers=[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     print(num)

#task2
# students=['sam','rahul','sahil','mohit','sagar','sabbi']
# for name in students:
#     if name.startswith('s'):
#         print(name)

#task3
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=0
# odd=0
# for num in numbers:
#     if num%2==0:
#         even+=1
#     else:
#         odd+=1 
# print('total even numbers:',even)
# print('total odd numbers:',odd)      

#task4  
# cities=['jaipur','jalandhar','chandigarh','ludhiana','amritsar']
# city=input('enter city name:')
# if city in cities:
#     print('city exists in the list ')
# else:
#     print('city doesnot exists in the list')  

#task5
# marks=[50,34,78,95,87,93]
# highest=marks[0]
# for mark in marks:
#     if mark>highest:
#         highest=mark
# print('highest marks:',highest)        

#task6
# marks=[50,34,78,95,87,93]
# lowest=marks[0]
# for mark in marks:
#     if mark<lowest:
#         lowest=mark
# print('lowest marks:',lowest)  

#task7 
# numbers=[23,45,34,56,76,34,68,23,67,85,56]
# newlist=[]
# for i in numbers:
#     if i not in newlist:
#         newlist.append(i)
# for i in newlist:
#     print(i,'->',numbers.count(i))        

# task8
# words=['apple','banana','mango','kiwi','watermelon']
# longest=words[0]
# for word in words:
#     if len(word)>len(longest):
#         longest=word
# print('longest string:',longest)  

#task9  
# words=['apple','banana','mango','kiwi','watermelon']
# shortest=words[0]
# for word in words:
#     if len(word)<len(shortest):
#         shortest=word
# print('shortest string:',shortest)   

#task10 
# numbers=[2,3,4,5,6,7,8]
# total=0
# for num in numbers:
#    total=total+num
# print('total of inputs',total)

#task11 
# numbers=[34,23,45,12,24,56,78]
# total=0
# for num in numbers:
#     total=total+num
#     average=total/len(numbers)
# print('average of inputs:',average)       

#task12
# names=['sahil','gurpreet','sagar','kunal','vishal']
# for name in names:
#     if len(name)>6:
#         print(name)   

#task14 
# text=input('enter your text here:')
# v=['a','e','i','o','u']
# vowels=0
# consonents=len(text)
# for i in range(5):
#     if v[i] in text:
#         vowels=vowels+text.count(v[i])
# print('number of vowels:',vowels)
# print('number of consonents:',consonents-vowels)     

#task13
# list=['python','hello',34,3.4]
# for i in list:
#     print(i ,type(i))

#task15
# list=[['mango','banana','orange'],'cherry']

# print(list[0][0][0])

# emp=[['naveen','1234',234223],['aman','2345',234356]]


# print("--------------------------------------------------")
# print("emp_name\tempid\t\temp_salary")
# for i in emp:
#     print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}")

#task16
# list1=[10,20,30,40,50]
# list2=[30,40,50,60,70]
# for i in list1:
#     if i in list2:
#         print(i)

#task17
# words=['mango','hello','python','apple','kiwi','level']
# for word in words:
#     reverse=''
#     for i in range(1,len(word)+1):
#         reverse=reverse+word[-i]
#     if word==reverse:
#         print(word,'is palindrome') 
#     else:
#         print(word,"not palindrome")  

#task18 
# numbers=[10,15,20,30,35,45,50,60,75,90]
# for i in numbers:
#     if i%3==0 and i%5==0:
#         print(i)

#task19
# subject=['english','maths','physics','chemistry']
# marks=[65,75,74,85]
# for i in range(len(subject)):
#     print(subject[i],':',marks[i])

#task20
# usernames=['aman','rahul','rajat','harsh']
# passwords=[2345,3455,5753,5676]
# username=input('enter the username:')
# password=int(input('enter your password:'))
# if username in usernames:
#     index=usernames.index(username)
#     if password==passwords[index]:
#         print('login successful')
#     else:
#         print('incorrect password')
# else:
#     print('username not valid')        


tasks=[]
while True:
    print('----to do list----')
    print('1.add task')
    print('2.view task')
    print('3.remove task')
    print('4.exit')
    choice=int(input('choose option 1-4:'))
    if choice==1:
        task=input('enter the text:')
        tasks.append(task)
    elif choice==2:
        if len(tasks)==0:
            print('no tasks available')
        else:
            for i in range(len(tasks)):
                print(i+1,tasks[i])
    elif choice==3:
        if len(tasks)==0:
            print('no tasks available')
        else:    
            print('1.remove by number')
            print('2.remove by name')
            a=input('choose')
            if a=='1':
                num=int(input('enter the number:'))
                tasks.pop(num-1)
            elif a=='2':
                name=input('enter the name:')
                tasks.remove(name)    
    elif choice==4:
        print('good bye to do list')
        break
              
