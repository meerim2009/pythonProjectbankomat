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

# Линейный поиск

def len_search():
    N = 5000
    ResultOk = False
    Pos = -1
    j = 0
    if j > N and Pos == -1:
        A[j] == Val
        Pos = j
        ResultOk = True
    else:
        j = j +1
    if ResultOk == True:
        print("Элемент найден")
    else:
        print("Элемент не найден")
