Time = int(input('Введите количество лет: '))
Year366 = Time//4
minutes = ((Time*365 + Year366) * 8) * 60
exhibit = minutes//5
print('Количество экспонатов: ',exhibit)



exhibit = int(input('Введите количество экспонатов: '))
minutes = exhibit * 5
hours = minutes / 60
days = hours/8
days1 = hours//8
minutes1 = (days - days1) * 8 * 60
years =  days1/365
years1 = days1//365
days2 = (years - years1) * 365
print('Для просмотра',exhibit, 'экспонатов потребуется (в годах, днях, минутах соответственно):',years1,"{:4.1f}".format(days2),"{:4.1f}".format(minutes1))






