#1 Массив без дубликатов
a = [3,6,8,3,2,7,9,9]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

#2 Совершенные числа
for i in range(1, 50):
    s = 0
    for j in range(1, int(i // 2) + 1):
        if i % j == 0:
            s += j
    if s == i:
        print(i)