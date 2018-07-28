import sys


for i in range(3):
    for j in range(10):
        print(j,end='',flush=True)

print('')

for j in range(3):
    for i in range(0,10):
        sys.stdout.write(str(i))
    
print('')

for j in range(3):
    for i in range(0,10):
        sys.stdout.write('{}'.format(i))
    
print('')


marks = [10, 20, 30, 33, 45, 55]

for number in range(len(marks)):
    print(" Congratulations %d number students " %  (number+1))

 
def gugu(n):
    result=[]
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)

    return result


<<<<<<< HEAD
=======

>>>>>>> c015d95a48437e576ab2c3b806b14704017236be
print(gugu(3))

for i in gugu(4):
    print("gugudan {0} dan {1} ".format(3,i))


a = "PYTHON"
print("{0:>30}".format(a))


