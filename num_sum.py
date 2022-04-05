"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.
Можно пользоваться только функциями, операторами и условиями.
"""

"""
def sum_of_numbers(number):
    return number % 10 + f(numner // 10)
"""

def sum_of_numbers(number, res=0):
    if not number:
        return res
    res += number % 10
    number //= 10
    return sum_of_numbers(number, res)


print('Enter the number')
number = int(input())

print(sum_of_numbers(number))
