def bank(a, years, pr):
    interest_rate = float(pr)/100
    total_amount = a

    for year in range(years):
        total_amount += total_amount*interest_rate

    return total_amount

vk = float(input('Введите сумму вклада '))
ye = int(input('Введите срок вклада '))
pr = float(input('Введите проценты '))
final = bank(vk, ye, pr)

print(f'Cумма на счету через {ye} лет составит:{final} рублей ')
    
    
