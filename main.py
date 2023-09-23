def inputMas(mas_length):
    mas = []
    print("Вводите значение в массив по одному")
    while mas_length > 0:
        mas.append(int(input()))
        mas_length -= 1
    return mas

mas_length1 = int(input("Введите кол-во элементов первого списка: "))
mas_length2 = int(input("Введите кол-во элементов второго списка: "))
mas1 = inputMas(mas_length1)
mas2 = inputMas(mas_length2)

result = sorted({x for x in mas1 if x in mas2})

print("Итоговый список: ", *result)

