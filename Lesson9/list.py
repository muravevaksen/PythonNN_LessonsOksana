print(list('dsddssd')) # создает отдельные элементы строки и они изменяемы

var1 = list('ssserhgtfb')
var1[0] = '0'
var1[5] = '0'
var1 = '___'.join(var1) # объединяет список в строку, внутри кавычек разделитель
print(var1)

print(r'1\n2') # выводит строку вместе со спец символами
print('1\\n2')
print('Bob\'s name')