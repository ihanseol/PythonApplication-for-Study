#python code get_number
#2018/7/28




check_ = True

def get_number(str_):
    condition_ = True
    
    while condition_ == True:
        try:
            number = input(str_)
            number = float(number)
            condition_ = False
        except ValueError:
            condition_ = True

    return number




num1 = get_number('enter first number : ')
num2 = get_number('enter second number : ')

sum = float(num1) + float(num2)

print("")
print(' the number is 1: %8.2f 2: %8.2f' % (float(num1), float(num2)))

print(' the sum of {0} + {1} = {2} '.format(num1, num2,sum))



