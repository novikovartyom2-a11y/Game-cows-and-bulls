def main():
    while True:
        number = random.randint(1000, 9999)
        if len(set(str(number))) == 4:
            break


while True:
    chislo = input("Ваш вариант: ")

    if len(chislo) != 4:
        print("Ошибка: введите ровно 4 цифры")
        continue
    count += 1

    bulls = 0
    cows = 0
    for i in range(4):
        if chislo[i] == str(number)[i]:
            bulls += 1
        elif chislo[i] in str(number):
            cows += 1
if __name__ == "__main__":
    main()
# Если файл запущен напрямую: __name__ == "__main__"
# Если файл импортирован: __name__ будет равно имени файла