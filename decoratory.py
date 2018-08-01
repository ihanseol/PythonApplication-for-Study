#
# decorator
# https://youtu.be/7gKKNLOQTCE
#




def line():
    print("-"*50)


def alert_start(func):
    def new_func(*args,**kwargs):
        print(" function is running ...")
        return func(*args, **kwargs)
    
    return new_func



def alert_end(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print(" function is ending ...")
        return result
    return new_func


@alert_start
def sum_all(*args):
    return sum(args)

# alert_start(sum_all)   
# @alert_end
# @alert_start
# like this we can add multiple decorator ....



new_func = alert_start(print)
new_print = alert_end(print)

#new_func(" hello world ")
new_print(" hello minhwasoo ")


new_print2 = alert_end(alert_start(print))
new_print2(" this is called by new print 2 ")

line()

print(sum_all(1,2,3,4,5))


# ---------------------------------------------------------------------------

line()

def print_name(func):
    def inner(*args, **kwargs):
        print (" ** are running fuction ... ")
        return func(*args, **kwargs)
    return inner


# ---------------------------------------------------------------------------

def print_name2(name):
    def outer(func):
        def inner(*args,**kwargs):
            print(" Mr {} are running this function ... ".format(name))
            return func(*args, **kwargs)
        return inner
    return outer


@print_name2(' minhwasoo ')
def sum_all2(*args):
    return sum(args)

print( sum_all2(1,2,3,4,5 ))

# ---------------------------------------------------------------------------
# just in case recursive function 
# decorator function is called n times ..
# so be careful when we use decorator function ...
#
# ---------------------------------------------------------------------------


@print_name2("sol")
def sum_all3(a, *b):
    return a + (sum_all3(*b) if b else 0  )


print(sum_all3( 1, 2, 3, 4 ))


line()


def check_n(func):
    def inner(*a, **b):
        print(a)
        return func(*a, **b)
    return inner


@check_n
def fib(n):
    if (n<2):
        return n
    return fib(n-1) + fib(n-2)
    

#for i in range(1,10):
#    print(fib(i))


print(fib(10))















