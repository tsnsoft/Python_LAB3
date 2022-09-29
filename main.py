#!/usr/bin/env python3
# coding=utf-8

import random


def random_array(n, m, max_value=10):
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%4d\t" % j, end='')
        print()


def counting(array):
    print()
    count_zero = 0
    count_pos = 0
    for i in array:
        for j in i:
            if j == 0:
                count_zero += 1
            if j > 0:
                count_pos += 1
    print("Число нулей - %d, число положительных чисел - %d" % (count_zero, count_pos))
    print()
    return count_zero, count_pos


def main():
    array = random_array(7, 8)
    print("Условие задания: Если в таблице количество нулей больше пяти,\n"
          "и количество положительных чисел больше трех,\n"
          "то увеличить максимальный элемент в два раза")
    print_array(array)
    counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':
            array = random_array(7, 8)
            print_array(array)
            count_zero, count_pos = counting(array)
        elif key == '2':
            if count_zero <= 5 and count_pos <= 3:
                print("Число нулей в таблице (%d) не больше пяти " % count_zero)
                print("или число положительных чисел (%d) не больше трех" % count_pos)
                print("Задание не будет выполнено.")
            else:
                print("Количество нулей в таблице больше пяти и число положительных чисел больше трех.")
                max_value = -1
                for i in range(len(array)):
                    for j in range(len(array[i])):
                        if array[i][j] > max_value:
                            max_value = array[i][j]
                for i in range(len(array)):
                    while True:
                        try:
                            index = array[i].index(max_value)
                            array[i][index] *= 2
                        except ValueError:
                            break
                print("Макс. элемент таблицы (все, если их больше одного) был(и) увеличен(ы) в два раза.")
                print_array(array)
                break
        elif key == '3':
            exit(0)


if __name__ == '__main__':
    main()
