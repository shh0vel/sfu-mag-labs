import math


def main():
    while True:
        print('\n=====Задачи (Лабораторная № 2)===== \n')
        print('[1] Високосный год')
        print('[2] Функция')
        print('[3] ЖД Билет')
        print('[4] Спортсмен')
        print('[5] Пароль')
        print('[6] Зоопарк')
        print('[7] Совершенные числа')
        print('[8] Выход')
        print('=' * 20)
        
        choice = input("Выберите номер задачи (1-8): ").strip()
    
        if not choice.isdigit():
            print("Ошибка, введите число от 1 до 8")
            continue
            
        menu_entry_index = int(choice)
            
        match menu_entry_index:
            case 1:
                leap_year()
            case 2:
                function()
            case 3:
                train_ticket()
            case 4:
                athlete()
            case 5:
                password()
            case 6:
                zoo()
            case 7:
                perfect_numbers()
            case 8:
                print("\nВыход...")
                break
            case _:
                print("Ошибка")


def leap_year():
    print('\n=====ВИСОКОСНЫЙ ГОД=====\n')
    
    while True:
        year = get_int('Введите желаемый год: ')
        if year <= 0:
            print('Ошибка, год - положительное число')
            continue
        break
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print(f'Год {year} - високосный!')
    else:
        print(f'Год {year} - невисокосный')
    
    input('\nНажмите Enter, чтобы продолжить\n')


def function():
    print('\n=====ФУНКЦИЯ=====\n')
    
    x = get_float('Введите число X: ')
    y = 0
    if x < 0:
        y = math.sin(x)
        print(f'{x} < 0 \nОтвет: {y=}')
    elif x >= 0 and x <= 1:
        y = math.cos(x)
        print(f'0 <= {x} <= 1 \nОтвет: {y=}')
    else:
        y = math.tan(x)
        print(f'{x} > 1 \nОтвет: {y=}')
    print()

    input('\nНажмите Enter, чтобы продолжить\n')
    
    
def train_ticket():
    print('\n=====ЖД БИЛЕТ=====\n')
    
    price_per_km = 10
    while True:
        distance = get_int("Введите расстояние до пункта: ")
        days = get_int("Введите длительность пребывания в пункте (дней): ")
        if distance <= 0:
            print('Ошибка, расстояние должно быть положительным числом')
            continue
        if days <= 0:
            print('Ошибка, длительность должна быть положительным числом')
            continue
        break
    
    base_price = (distance * 2) * price_per_km
    if distance > 1000 and days > 7:
        discount = base_price * 0.30
        final_price = base_price - discount
        print(f'\nСтоимость поездки: {base_price:.2f} руб')
        print(f'\nВаша скидка: {discount:.2f} руб')
        print(f'\nИтого к оплате: {final_price:.2f} руб.')
    else:
        final_price = base_price
        print(f'\nСтоимость поездки: {base_price:.2f} руб')
        print('\nУ вас нет скидки')
        print(f'\nИтого к оплате: {final_price:.2f} руб.')
        
    input('\nНажмите Enter, чтобы продолжить\n')
        

def athlete():
    print('\n=====СПОРТСМЕН=====\n')
    
    while True:
        x = get_float('В первый день спортсмен пробежал (км): ')
        if x <= 0:
            print('Ошибка, расстояние должно быть положительным числом')
            continue
        break
        
    while True:
        y = get_float('Какую дистанцию должен пробежать: ')
        if y <= 0:
            print('Ошибка, расстояние должно быть положительным числом')
            continue
        if y < x:
            print('Ошибка, дистанция не должна быть меньше пробега в первый день')
            continue
        break

    day = 1
    current_x = x 
    
    while current_x < y:
        current_x *= 1.10  
        day += 1           
        
    print('\nОтвет:')
    print(f'На {day}-й день пробег спортсмена составит не менее {y} км.')
    print(f'(Точный пробег на этот день: {current_x:.2f} км)')
    
    input('\nНажмите Enter, чтобы продолжить\n')



def password():
    print('\n=====ПАРОЛЬ=====\n')
    
    correct_pass = "qwerty"
    secret = "Добро пожаловать!"
    
    while True:
        input_pass = input("Введите пароль: ")
        if input_pass == correct_pass:
            print(f'Пароль верный\n{secret}')
            input('\nНажмите Enter, чтобы продолжить\n')
            break
        else:
            print('Пароль неверный!\n')
            continue
    
    
def zoo():
    print('\n=====ЗООПАРК=====\n')
    
    visitor_age = None
    visitors_group = []
    k = 1
    total_amount = 0
    while True:
        visitor_age = input(f'Введите возраст посетителя {k}: ')
        if visitor_age == "":
            break
        try:
            visitor_age = int(visitor_age)
        except ValueError:
            print('Ошибка введите число')
            continue
        if visitor_age not in range(1,130):
            print('Введите корректный возраст')
            continue
        k += 1
        visitors_group.append(visitor_age)
    for i in visitors_group:
        if i < 3:
            total_amount += 0
        elif i > 65:
            total_amount += 200
        elif i >= 3 and i < 12:
            total_amount += 150
        else:
            total_amount += 250
            
    print(f'Общая стоимость билета для этой группы из {k-1} человек - {total_amount:.2f} руб. \n')
    
    input('\nНажмите Enter, чтобы продолжить\n')


def perfect_numbers():
    print('\n=====СОВЕРШЕННЫЕ ЧИСЛА=====\n')
    
    for num in range(1,101):
        div_sum = 0
        for i in range(1, num):
            if num%i == 0:
                div_sum += i
        if div_sum == num:
            print(f'{num} - совершенное число')
            
    input('\nНажмите Enter, чтобы продолжить\n')


def get_int(text):
    while True:
        user_input = input(text)
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка, введите число")
            
            
def get_float(text):
    while True:
        user_input = input(text)
        try:
            return float(user_input)
        except ValueError:
            print("Ошибка, введите число")


if __name__ == "__main__":
    main()