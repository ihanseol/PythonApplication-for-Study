#
# loop
#


def line():
    print("-"*30)

numbers = [1,3,4,4,5,8,22,2,33]

result=0

for i in numbers:
    result = result+i

    
print(' result :', result)

print(range(10))
print(list(range(2,8)))
print(list(range(3,10,2)))


line()

for val in "string has a value":
    if (val == 'i'):
        break
    print(val)


print("the end")

line()

for val in "string has a value":
    if (val == 'i'):
        continue
    print(val)

 
line()


sequence = {'p','a','s','s'}

for i in sequence:
    print(i)
    
#infinite loop

while True:
    try:
        num = int(input('enter the number : '))
        break
    except ValueError:
        continue

print(' the number is ', num)


#loop condition in the middle


vowels = "aeiouAEIOU"

while True:
    v = input('enter a vowel : ')

    if v in vowels:
        break
    else:
        print(" that is not a vowels ")




#loop condition in the bottom

import random

while True:
    input(' Press enter to roll the dice ')

    num = random.randint(1,6)
    print('You got ', num)

    option = input('Roll again (y/n)')
    if option == 'n' or option == 'N' :
        break

    







