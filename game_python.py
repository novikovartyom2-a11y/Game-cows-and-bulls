#!/usr/bin/env python3
import random

def main():
    # Генерируем 4-значное число с разными цифрами
    while True:
        number = random.randint(1000, 9999)
        if len(set(str(number))) == 4:
            break

    print("Компьютер загадал 4-значное число")

    popit = 0

    while True:
        chislo = input("Ваш вариант: ")

        # Проверка на число пользователя
        if len(chislo) != 4 or not chislo.isdigit(): #4-знач число ли и состоит ли оно из цифр
            print("Ошибка: введите ровно 4 цифры")
            continue

        popit += 1

        # Считаем быков и коров
        bulls = cows = 0
        for i in range(4):
            if chislo[i] == str(number)[i]:
                bulls += 1
            elif chislo[i] in str(number):
                cows += 1

        print(f"Попытка {popit}: {bulls} быков, {cows} коров")

        if bulls == 4:
            print(f"Вы угадали число {number} за {attepopitmpts} попыток")
            break


if __name__ == "__main__":
    main()
#Если файл запущен напрямую: __name__ == "__main__"
#Если файл импортирован: __name__ будет равно имени файла