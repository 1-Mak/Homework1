student_name = str(input('Введите имя студента: '))
student_surname = str(input('Введите фамилию студента: '))
student_birthdate = int(input('Введите год рождения студента: '))
print(student_name,'_',student_surname,'_',student_birthdate, sep='')
student_name,student_surname = student_surname,student_name
print(student_name,'_',student_surname,'_',student_birthdate + 60, sep='')