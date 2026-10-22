# import math as ma

# print(math.factorial(5))

# print(math.sqrt(25))

# print(m.pow(3,2))

# import random as r

# print(r.random())

# print(r.randint(10000,99999))

# li=['mango','orange','banana','apple']



# print(r.choice(li))
# print(r.sample(li,k=2))

# import calc

# print(calc.add(3,5))


# import numpy as np

# a=np.array([3,4,5,7,68,8,9])

# print(a)



# a=[('name','jack'),('class','mca')]

# b=dict(a)

# print(b)

# print(r.choices(list(b.values()),k=1))

# import random as r
# a=r.randint(1,10)
# attempts=0
# while True:
#     guess=int(input('guess the number:'))
#     attempts=attempts+1
#     if guess==a:
#         print('correct,you have guess the number')
#         print('random number is',a)
#         print('attempts used',attempts)
#         break
#     elif guess>a:
#         print('the number is bigger')
#     else:
#         print('the number is smaller')  
#         

li=['stone','paper','scissor']
import random as r


yourscore=0
opponentscore=0
while True:
    opponent=r.choice(li)
    you=input('enter stone,paper,scissor:')
    print('opponent chose:',opponent)
    if you not in li:
        print('invalid choice')
    elif you==opponent:
        print('its a tie')
    elif you=='stone' and opponent=='scissor':
        print('you won')
        yourscore+=1
    elif you=='paper' and opponent=='stone':
        print(' you won')
        yourscore+=1

    elif you=='scissor' and opponent=='paper':
        print(' you won')
        yourscore+=1
    else:
        print('opponent won')
        opponentscore+=1

    play=input('you want to play (yes/no):')
    if play=='no':
        print('game over')
        print('final score')
        print('you:',yourscore)
        print('opponent:',opponentscore)
        break


