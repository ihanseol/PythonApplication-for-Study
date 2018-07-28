

def line():
    print("-"*40)


def computeHCF(x,y):
    while(y):
        x, y = y, x%y

    return x



def computeHCF1(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if ((x%i == 0) and (y%i == 0)) :
            hcf = i

    return hcf


#-------------------------------------------------------------------------------------------------------------------------------

def LCM(x, y):
    if (x > y) :
        greater = x
    else:
        greater = y

    while(True):
        if (greater%x == 0 ) and (greater%y == 0):
            lcm = greater
            break
        greater += 1

    return lcm



#source code using gcd function

def gcd(x, y):

    while(y):
        x, y = y, x % y

    return x



def LCM2(x, y):
    lcm = (x*y)//gcd(x,y)
    return lcm


#-------------------------------------------------------------------------------------------------------------------------------

#return multi values by list
#2018/7/28

def swap(x,y):
    x,y = y,x
    result = [x]
    result.append(y)

    return result



line()
print(computeHCF(54, 24))
print(computeHCF1(54,24))
line()

print("LCM by loop " + str(LCM(54, 24)))
print("LCM by gcd function " + str(LCM2(54, 24)))
line()




result = swap(1,2)
for i in result:
    print( 'the value is ' + str(i))

line()






