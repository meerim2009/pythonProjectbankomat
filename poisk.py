# Бинарный поиск

def binarySearch(N, Val):
    N = 5000
    first = 0
    last = N-1
    ResultOk = False

    while first < last:
        middle = (first + last)//2
        if Val == A[middle]:
            first = middle
            last = first
            pos = middle
            ResultOk = True
        else:
            if Val > A[middle]:
                first = middle + 1
            else:
                last = middle - 1
    if ResultOk == True:
        print("Элемент найден")
    else:
        print("Элемент не найден")
