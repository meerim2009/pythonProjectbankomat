banknotes = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
quantities = [10, 5, 5, 3, 2, 1, 2, 3, 3, 2, 0, 2]

output = input('Введите сумму для снятия')
withdraw = USERINNPUT
total_availabel = 0
result = ''
remain_to_give = withdraw
for i in len(banknotes) - 1:
    total_availabel = total_availabel + banknotes[i] * quantities[i]

if remain_to_give > total_availabel then
    output = input('Недостаточно средств для снятия')
else:
    for i in len(banknotes) - 1 to 0:
        if remain_to_give >= banknotes[i] then
            quantity = remain_to_give // banknotes[i]
        if quantity <= quantities[i] then
            result = result + '' + quantity + 'x' + banknotes[i]
            quantities[i] - quantity
            remain_to_give <= remain_to_give - quantity * banknotes[i]
            if remain_to_give = 0:
                break
            endif
        else:
        result = result + '' + quantity + 'x' + banknotes[i]
        remain_to_give <= remain_to_give - quantity * banknotes[i]
        quantities[i] = 0
        endif
    endfor

if withdraw = 0 then
    output = input('Вы получили' + result + 'всего' + withdraw)
elseif:












