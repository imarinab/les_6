"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"
Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""
from datetime import datetime


name = input('Print your name:\n')

def log_decorator(hello):
    print("'Hello()' function is in progress whith args: {name} and without kwargs")
    start = datetime.now()
    hello(name)
    print("Function 'Hello' completed")
    print(f"Function execution time - ", datetime.now() - start)
    return log_decorator

@log_decorator
def hello(name):
    print(f"Hello, {name}!")

