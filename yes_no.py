"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

def uniq(spis):
    i = 0
    for i in range(0, (len(spis) - 1)):
        if spis[i] in spis[i + 1:]:
            print('Yes')
            quit()
        else:
            i + 1
    print('No')



print('Enter list of numbers')
spis = list(map(int,input().split()))

uniq(spis)




