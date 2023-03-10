def valid_num(number):
    if number.isdigit() == False:
        return False
    else:
        return True

# Задача 1
# Найдите сумму цифр трехзначного числа.

while True:
    n = input('Введите трехзначное число:\n')
    if valid_num(n) == False or (100 <= int(n) <= 999) == False:
        print('Это не число либо не ТРЕХЗНАЧНОЕ число.\n')
    else:
        print(sum(list(map(lambda x: int(x), [i for i in n]))))
        break

