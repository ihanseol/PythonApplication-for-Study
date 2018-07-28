


def greet_name(name_):
    """ this function is for greeting 
        to the person passed in as a 
        parameter """
    print("hello " + name_  + " good morning")


def greet2(name, msg=" Good morning "):
    print(" ABC " + name + msg)

def greet3(*name):
    for i in name:
        print('Hello ' + i)


def absolute_value(val):
    if (val>=0) :
        return val
    else:
        return -val



greet_name("minhwasoo")
greet2("min")
greet3("james","jessica","kim","john")


print(absolute_value(-2))
