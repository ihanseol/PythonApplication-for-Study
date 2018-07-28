

#
# https://www.programiz.com/python-programming/examples/armstrong-number
#
#


def check_amstrong(n):
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10

    if n == sum:
        print(n, " is a amstrong number ")
    else:
        print(n, " is not a amstrong number ")

       
def check_armstrong_ndigit(n):
    order = len(str(n))

    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit**order
        temp //= 10

    if n == sum:
        print(n, ' is a amstrong number ')
    else:
        print(n, ' is not amstrong number ')






check_amstrong(663)
check_armstrong_ndigit(1634)


