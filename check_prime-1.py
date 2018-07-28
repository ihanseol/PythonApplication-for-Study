#
#
# https://www.programiz.com/python-programming/examples/prime-number
#
#

# in here for loop else .... the scope of for loop



def line():
    print("-"*30)

def check_prime(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0 :
                print( num, " is not a prime number ")
                print(i, "times", num//i, " is ", num)
                break
        else:
            print("{0} is a prime number".format(num))
    else:
        print( num , " is not a prime number ")


def check_range(n):
    for i in range(2,n):
        print(i)



def print_prime(x,y):
    if x>y:
        x,y = y,x

    for num in range(x,y+1):
         if num > 1:
            for i in range(2, num):
                 if (num%i) == 0:
                     break
            else:
                print(num)


    
#-----------------------------------------------------------------------------------------------------------------------------
print_prime(30,80)

line()
check_prime(407)
line()
check_prime(3)




