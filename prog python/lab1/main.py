import math


def acquaintance():
    print('\n=====ЗНАКОМСТВО=====\n')
    
    name = input('Как вас зовут? \n')
    speciality = input('На какой специальности Вы обучались ранее? \n')
    
    print(f'\nЯ {name}, обучался на специальности {speciality}.\n')
    
    input('\nНажмите Enter, чтобы продолжить\n')

def math_oper():
    print('\n=====МАТЕМАТИЧЕСКИЕ ОПЕРАЦИИ=====\n')
    
    while True:
        num1 = input('Введите число A: ')
        try:
            num1 = int(num1)
        except ValueError:
            print('Ошибка, введите число')
            continue
        num2 = input('Введите число B: ')
        try:
            num2 = int(num2)
        except ValueError:
            print('Ошибка, введите число')
            continue
        break
    
    print(f'\nВаши числа: {num1} и {num2}\n')
    print(f'Сумма A и B: {num1+num2}')
    print(f'Сумма квадратов двух чисел A и B: {num1**2 + num2**2}')
    print(f'Разница между A и B: {num1 - num2}')
    print(f'Произведение A и B: {num1*num2}')
    print(f'Частное от деления A на B: {num1 // num2}')
    print(f'Остаток от деления A на B: {num1%num2}')
    print(f'Натуральный логарифм числа A: {math.log(num1)}')
    print(f'Экспонента числа A: {math.exp(num1)}')
    print(f'Число A в степени B: {math.pow(num1, num2)}')
    
    input('\nНажмите Enter, чтобы продолжить\n')


def time_convert():
    print('\n=====КОНВЕРТАЦИЯ ВРЕМЕНИ=====\n')
    
    sec, min, hour = 0, 0, 0
    
    while True:
        num = input('Введите число (кол-во секунд): ')
        try:
            num = int(num)
        except ValueError:
            print('Ошибка, введите число')
            continue
        if num < 0:
            print('Ошибка, введите число > 0')
            continue
        break
    
    if num >= 60:
        sec = num%60
        min = num//60
        if min >= 60:
            hour = min//60
            min = min%60
    else:
        sec = num
        
    print(f'{num} секунд = {hour} ч. {min} мин. {sec} сек.')
    
    input('\nНажмите Enter, чтобы продолжить\n')


def rest_order():
    print('\n=====ЗАКАЗ В РЕСТОРАНЕ=====\n')
    
    while True:
        order = input('Введите сумму заказа (руб.): ')
        try:
            order = float(order)
        except ValueError:
            print('Ошибка, введите корректное число')
            continue
        if order < 0:
            print('Ошибка, сумма не может быть отрицательной')
            continue
        break
        
    tax = order * 0.13        
    tips = order * 0.18       
    total = order + tax + tips 

    print(f'\nСтоимость заказа: {order:.2f} руб.')
    print(f'Налог (13%):      {tax:.2f} руб.')
    print(f'Чаевые (18%):     {tips:.2f} руб.')
    print('-' * 30)
    print(f'ИТОГО:            {total:.2f} руб.')

    input('\nНажмите Enter, чтобы продолжить\n')


def bank_acc():
    print('\n=====СЧЕТ В БАНКЕ=====\n')
    
    while True:
        deposit = input('Введите сумму первоначального депозита (руб.): ')
        try:
            deposit = float(deposit)
        except ValueError:
            print('Ошибка, введите число')
            continue
        if deposit < 0:
            print('Ошибка, депозит не может быть отрицательным')
            continue
        break
        
    balance = deposit
    percent = 0.04 
    
    print(f'\nНачальный депозит: {deposit:.2f} руб.\n')
    
    for year in range(1, 4):
        balance = balance + (balance * percent)
        print(f'Баланс в конце {year}-го года: {balance:.2f} руб.')
        
    input('\nНажмите Enter, чтобы продолжить\n')


def main():
    while True:
        print('=====Задачи===== \n')
        print('[1] Знакомство')
        print('[2] Математические операции')
        print('[3] Конвертация времени')
        print('[4] Заказ в ресторане')
        print('[5] Счет в банке')
        print('[6] Выход из программы')
        print('=' * 20)
        
        choice = input("Выберите номер задачи (1-6): ").strip()
    
        if not choice.isdigit():
            print("Ошибка, введите число от 1 до 6")
            continue
            
        menu_entry_index = int(choice)
            
        match menu_entry_index:
            case 1:
                acquaintance()
            case 2:
                math_oper()
            case 3:
                time_convert()
            case 4:
                rest_order()
            case 5:
                bank_acc()
            case 6:
                print("\nВыход...")
                break
            case _:
                print("Ошибка")

if __name__ == "__main__":
    main()