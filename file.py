# x = create a file
# r = read a file
# w = write in a file
# a = add in the last postion

# a=open('demo.txt','r')
# # print(a.read(100))
# # print(a.readline())
# # print(a.readline())
# # print(a.readline())
# # print(a.readline())
# # a.seek(10)
# # print(a.tell())
# # print(a.read())
# a.close()

# li=['mango\n','banana\n','apple\n','orange']

# a=open('demo.txt','w')
# a.writelines(li)
# a.close()



# with open('C:/Users/Hp/Desktop/test.txt','r') as f:
#     # f.write("print('hello world')")
#     a=f.read()
#     print(a)

# task1 and task2
# with open('data.txt','r') as a:
#     a.write('sameer')
#     b=a.read()
#     print(b)

# task3
# with open('data.txt','a') as a:
#     a.write('  jalandhar')

# task4
# with open('data.txt','r') as a:
#     content=a.read()
#     count=len(content)
# print('total characters:',count)    

# taask5
# with open('data.txt','r')as a:
#     b=a.read()
#     c=b.split()
#     c=len(b)
# print('total words:',c)    

# task6
# with open('data.txt','r')as a:
#     b=a.read()
#     c=len(b)
# print('total lines:',c)    

# task7
# with open('data.txt','r')as a:
#     b=a.read()
# with open('copy.txt','w')as c:
#     c.write(b)

#task8 
# with open('copy.txt','r')as c:
#     b=c.read(5)
# print('first 5 characters:',b)    

#task9  
# with open('copy.txt','r')as a:
#     for i in range(5):
        # print(a.readline())      

# task10
# with open('copy.txt','r')as a:
#    b=a.read()
# print('exists')   

#task11
# with open('copy.txt','r')as a:
#     b=a.read()
# word=input('enter your word:')
# c=b.split().c(word)
# print('occurences:',c)

# a=open('copy.txt','r')
# w=str(a.read())
# # print(w.count('python'))
# w=w.replace('python','digital marketing')
# # print(type(w))
# a.close()

# b=open('copy.txt','w')
# b.write(w)
# b.close

# task13
# with open('numbers.txt','w')as file:
#     file.write(f'{10}\n {20}\n {30}\n {40}')
#     file.close()

# with open('numbers.txt','r')as file:
#     total=0
#     for line in file:
#         total=total+int(line)
# print('sum',total)    

# task14
# with open('numbers.txt','r')as file:
#     for line in file:
#         name,marks=line.split()
#         if int(marks)>75:
#             print(name,marks)
# file.close()         

# task15   
# with open('numbers.txt','r')as file:
#     lines=file.readlines()
#     file.close()
# with open('numbers.txt','w')
#     for line in lines:
#         if line in lines:
#             if line.strip()!='':
#                file.close()     


# task16
# with open('numbers.txt','w')as file:
#     while True:
#          text=input('enter your text:')
#          if text=='stop':
#           break
#          file.write(text+'\n')
# print('data saved successfully')        
    
# task17
# numbers=[10,20,30,40,50,60]
# with open('numbers.txt','w')as file:
#     for i in numbers:
#         file.write(str(i)+'\n')
# with open('numbers.txt','r')as file:
#     b=file.read()
# print(b)    

# task18
# a=open('copy.txt','r')
# a1=a.read()
# a.close()
# b=open('data.txt','r')
# b1=b.read()
# b.close()
# c=open('merged.txt','w')
# c1=c.write(a1+'\n'+b1)
# c.close()
# print('files merged')  

# task19
# with open('data.txt','r')as file:
#     a=file.read()
#     file.close()
# ch=input('enter character:')
# print('count',a.count(ch))    

#task20 
# file=open('data.txt','r')
# a=file.read()
# file.close()
# a=a.upper()
# file=open('uppercase.txt','w')
# file.write(a)
# file.close()
# print('converted to uppercase')
