a =int(input('Введите первое число : '))
b = int(input('Введите второе число : '))
c = int(input('Введите третье число : '))
d = int(input('Введите четвертое число : '))
if a == b and a == c and a == d and b == c and b ==d and c == d:
    print(4)
elif a == b and a != c and a != d or a == c and a != b and a != d or a == d and a != b and a != c or c == b and c != a and c != d or c == d and c != a and c != b:
    print(2)
elif a == b and a == c and a != d or a == b and a == d and a != c or a == c and a == d and a !=b:
    print(3)
else:
    print(0)
