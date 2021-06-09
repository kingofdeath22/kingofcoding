a = int(input('Введите 1 число'))
b = int(input('Введите 2 число'))
if a%b == 0:
    print("%d делится на %d" % (a,b))
else:
    print("%d не делится на %d" % (a,b))
    print("Остаток: %d" % (a%b))
print("Частное: %d" % (a//b))