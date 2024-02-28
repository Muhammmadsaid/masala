n = int(input())
max = 0
min = 9
while n > 0:
    a = n % 10
    if a > max:
        max = a
    if a < min:
        min = a
    n = n // 10
print('Максимальная цифра равна',max)
print('Минимальная цифра равна',min)
