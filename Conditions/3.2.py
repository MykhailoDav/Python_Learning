import math

X = float(input('X = '))
A = float(input('A = '))
B = float(input('B = '))
C = float(input('C = '))

if X < 5 and C != 0:
    F = -A*X**2-B
elif X > 5 and C == 0:
    F = (X-A)/X
else:
    F = -X/C

print(F)