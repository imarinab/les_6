"""
С помощью декораторов реализовать конвейер сборки бургера
Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"
Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"
Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"
Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"
Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"
Написать функцию beef, которая:
 - печатает "### говядина ###"
Написать функцию chicken, которая:
 - печатает "|||| курица ||||"
1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка
2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""

def bread(funct):
    def wrapper(*args, **kwargs):
        print("</------------\\>")
        funct()
        print("<\\____________/>")
    return wrapper


def tomato(funct):
    def wrapper(*args, **kwargs):
        print("*** tomato ****")
        funct()
    return wrapper


def salad(funct):
    def wrapper(*args, **kwargs):
        print("~~~~ salad ~~~~~")
        funct()
    return wrapper

def cheese(funct):
    def wrapper(*args, **kwargs):
        print("^^^^^ cheese ^^^^^^")
        funct()
    return wrapper

def onion(funct):
    def wrapper(*args, **kwargs):
        print("----- onion ------")
        funct()
    return wrapper


@bread
@cheese
@salad
def chicken():
    print("|||| chicken ||||")


@bread
@onion
@tomato
def beef():
    print("### beef ###")

print("CHEESEBURGER")
chicken()
print("\n \n")
print("HAMBURGER")
beef()