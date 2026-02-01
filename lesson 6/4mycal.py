# Робимо функцію, яка буде реалізовувати калькулятор
def myCalc():
    a = input("Вкажіть значення a: ->_")
    b = input("Вкажіть значення b: ->_")
    intA = int(a)
    intB = int(b)
    print(f"{a}+{b}={intA+intB}") #f - форматований рядок у Python
    print(f"{a}-{b}={intA-intB}")
    print(f"{a}*{b}={intA*intB}")
   # if int(b) !=0:
    #    print(f"{a}/{b}={intA/intB}")
   # else:
    #    print("Mаємо спробу ділення на 0 ")
    if int(b) ==0:
        print("Mаємо спробу ділення на 0 ")
    else:
        print(f"{a}/{b}={intA/intB}")
# виклик функції
myCalc()