banknotes = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
qualities = [10, 5, 5, 3, 2, 1, 2, 3, 3, 2, 0, 2]


def test(summary, newBanknotes, newQualities):
    for j in range(-len(newBanknotes), 0):
        index = int(str(j)[1:])-1
        sumOfBanknotes = newBanknotes[index] * newQualities[index]
        summa = summary
        if summary >= newBanknotes[index]:
            print(newBanknotes[index])
            summa -= newBanknotes[index]
            test(summa, newBanknotes, newQualities)
            break


while True:
    summaryOut = int(input('Сколько хотите вывести: '))
    summaryBanknotes = 0
    newQualities = []
    newBanknotes = []

    for i in range(len(banknotes)):
        if qualities[i] >= 1:
            summaryBanknotes += banknotes[i] * qualities[i]
            newQualities.append(qualities[i])
            newBanknotes.append(banknotes[i])

    if summaryOut > summaryBanknotes:
        print('В банкомате нету столько денег!')
    else:
        test(summaryOut, newBanknotes, newQualities)
