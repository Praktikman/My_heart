import math

print(dir(math))
b=input('Please enter sin, cos or tan.... >>  ')
a=input('Please enter number >> ')
c=eval('math.' +b)
print(c(int(a)))
