# i=10
# while i>=1:
#     print(i)
#     i=i-1

# i=1
# while i<=10:
#     print(i*2)
#     i=i+1


# i=1
# while i<=10:
#     print('2 x',i,'=',i*2)
#     i=i+1

# a=int(input('enter your number'))
# i=1
# while i<=10:
#     print(a,'x',i,'=',i*a)
#     i=i+1

# i=1
# while i<=20:
#     if i%2!=0:
#         print(i,'odd')
#     else:
#         print(i,'even')    
#     i=i+1    

# print('odd\teven')
# i=1
# while i<=20:
#     if i%2==0:
#         print(i-1,"\t",i)
#     i+=1
    

# i=1
# while i<=20:
    # if i%2==1:
        # x=i
    # else:
        # print(x,"\t",i)
    # i+=1

text=input('enter the text here:')
i=0
v="aeiou"
vowels=0
consonents=len(text)
while i<5:
   if v[i] in text:
        vowels=vowels+text.count(v[i])
        
   i+=1

print(vowels)
print(consonents-vowels)
    

