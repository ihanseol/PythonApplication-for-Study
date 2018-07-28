
#
# name space, variable scope
#
#


def case1_outer_function():
    a=1
    def inner_funtion():
        b=2
        print('inside a = ', a)

    inner_funtion()
    print("outside a = ", a) 



def case2_outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a=30
        print(' inside a = ',a)

    inner_function()
    print(' outside = ',a)


a = 10

case2_outer_function()
print('a = ',a)

print(' id a ',id(a),' id 10 : ',id(10))




