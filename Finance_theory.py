#deposite — вырученные проценты,
#money — первоначальная сумма вложений,
#per_cent — годовая ставка,
#Time — количество дней вклада,
#days_a_year — количество дней в году
#Условие: Time_of_deposite,days_a_year  = 365,365

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = list(per_cent.values())
money = int(input('Первоначальная сумма вложений:'))

deposite_tkb = a[0]*money//100
deposite_skb = a[1]*money//100
deposite_vtb = a[2]*money//100
deposite_sber = a[3]*money//100
print('ТКБ:',deposite_tkb,"||",'СКБ:',deposite_skb,"||",'ВТБ',deposite_vtb,"||",'СБЕР',deposite_sber)

list_of_deposits = [(deposite_tkb), (deposite_skb), (deposite_vtb), (deposite_sber)]
print ('Максимальная сумма, которую вы можете заработать:', max(list_of_deposits))