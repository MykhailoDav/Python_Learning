import math

x = float(input('X = '))

A = x**2*math.sin(x/2)

if x <= -5:
    B = math.atan(math.exp(x))
if x > -5 and x <= 0:
    B = 1 + x**3/4
if x > 0:
    B = math.log(abs(x)) - x/5

y1 = A + B

print('1)', y1)

if x <= -5:
    B = math.atan(math.exp(x))
elif x > 0:
    B = math.log(abs(x)) - x/5
else: # -5 < x <= 0
    B = 1 + x**3/4




y2 = A + B

print('2)', y2)

