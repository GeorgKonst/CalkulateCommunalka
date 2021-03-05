import csv

with open("Datacalc.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")

    # Чтение показателей прошлого месяца, запись в переменные
    for row in file_reader:
        date = row['Date']
        electric_last = row['Electric']
        cold_water_last = row['Cold_Water']
        hot_water_last = row['Hot_Water']

# Перевод строки в число
electric_last = int(electric_last)
cold_water_last = int(cold_water_last)
hot_water_last = int(hot_water_last)

# Показания текущего месяца
electric = int(input('Электричество: '))
cold_water = int(input('Холодная вода: '))
hot_water = int(input('Горячая вода: '))

# Цены
electric_price = 5.47
cold_water_price = 38.7
hot_water_price = 191.72
drainage_price = 27.47

# Сколько израсходовано за текущий месяц
count_electric = electric - electric_last
count_cold_water = cold_water - cold_water_last
count_hot_water = hot_water - hot_water_last
count_drainage = count_cold_water + count_hot_water

# Сколько денег вышло
sum_electric = int("%.f" %(count_electric * electric_price))
sum_cold_water = int("%.f" %(count_cold_water * cold_water_price))
sum_hot_water = int("%.f" %(count_hot_water * hot_water_price))
sum_drainage = int("%.f" %(count_drainage * drainage_price))
all_price = sum_electric + sum_cold_water + sum_hot_water + sum_drainage

# Изменение даты
mon = int(date[3:5]) + 1
year = int(date[6:])

if mon <= 9:
    date = date[0:3] + '0' + str(mon) + date[5:]
elif mon <= 12:
    date = date[0:3] + str(mon) + date[5:]
else:
    date = date[0:3] + '01.' + str(year + 1)

print('Электроэнергии:', count_electric, 'киловат на сумму', sum_electric, 'рублей')
print('Холодной воды:', count_cold_water, 'кубов на сумму', sum_cold_water, 'рублей')
print('Горячей воды:', count_hot_water, 'кубов на сумму', sum_hot_water, 'рублей')
print('Водоотведение:', count_drainage, 'кубов на сумму', sum_drainage, 'рублей')
print("Счет за коммунальные услуги составил:", all_price, 'рублей')

with open("Datacalc.csv", mode="a", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    file_writer.writerow([date, electric, cold_water, hot_water, all_price])
