import math

X = float(input('X = '))
R = float(input('R = '))

if X <= -R:
    Y = R
else:
    if -R < X <= 0:
        Y = -(1/2)*X
    else:
        if 0 < X <= R:
            Y = R - math.sqrt(R**2 - X**2)
        else:
            if R < X <= 6:
                Y = math.sqrt((R)**2 - (X - R)**2)
            else:
                Y = - ((X - 2*R)/(6 - 2*R))

print(Y)