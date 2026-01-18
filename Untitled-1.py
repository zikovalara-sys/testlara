mystr = "Привіт козаки і козачки"
print(mystr)
#У рядку можна звертатися до окремих символів за індексом
#індексація у рядку починається з 0
name ="Петро" # індекси 0 1 2 3 4 d рядку
# [] - оператор індексації - для звертення до індексу до рядка
print(name[2])
#name[0]="c"

name = "Мальвіна"
print("name = ", name)
#
print("name[2:4] = ", name[2:4])#
print("name[0:3] = ", name[0:3])#

name = """ Аліса в 
країні чудес"""
print("name = ", name)

testStr = "Привіт" + name
print("testStr = ", testStr)
# ітерація по рядку
print("----ітерація по рядку--- ")
name = "Василь"
for char in name:
    print(char)

#чи підходить рядок під рядок
print("---Перевірка входження рядка в рядок----")
print('си' in name)
print('ка' in name)

print("---Довжина рядка---")
print("len(name) = ", len(name))

hello = "Hello"
print("hello = ", hello)
print("reverse hello =", hello[::-1])

