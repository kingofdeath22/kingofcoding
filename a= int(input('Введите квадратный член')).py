a= int(input('Введите квадратный член'))
b= int(input('Введите член с x'))
c= int(input('Введите свободный член'))
D= (b**2)-4*a*c
print('D= ',D)
if D>0:
    x1= (-b+(D**0.5))/(2*a)
    x2= (-b-(D**0.5))/(2*a)
    print('x1= ',x1,'x2= ',x2)
elif (D==0):
    x1= (-b+(D**0.5))/(2*a)
    print('x1= ',x1)
elif D<0:
    print('корней нет')

