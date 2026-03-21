import math


def calc_seriece(x, eps):
    result = 0
    func_result = math.cos(x)
    for i in range(500):
        value = (-1)**i * (x ** (2*i)) / math.factorial(2*i)
        result += value
        if (abs(func_result - result) < eps):
            break
    return [x, i, result, func_result, eps]
    

def print_result(list_results):
    print("| x = ", list_results[0], "| n = ", list_results[1], "| F(x) = ", list_results[2], " | Math F(x) = ", list_results[3], " | eps = ", list_results[4], " |")


def check_input():
    value = int(input("Введите ваше число: "))
    k = 0
    while (value != 100):
        if (value < 10):
            k += 1
        value = int(input("Введите ваше число: "))
    print("Общее число введенных чисел меньше 10 равно: ", k)


def str_check():
    str = input("Введите вашу строку: ")
    count_digits = 0
    count_lowest = 0
    for i in  str:
        if (i.isdigit()):
            count_digits += 1
        if (i.islower()):
            count_lowest += 1
    print("Количество цифр в стрке: ", count_digits, " количество букв в нижнем регистре: ", count_lowest)


def is_consonant(char):
    vowels = 'aeiouAEIOU'
    return char.isalpha() and char not in vowels


def analyze_text(text):
    start_word = True
    amount_words_starts = 0
    for i in text:
        if(is_consonant(i) and start_word):
            amount_words_starts += 1
            start_word = False
        if (i == ' '):
            start_word = True
    print("Amount of words that starts with consonant: ", amount_words_starts)


def same_alphas(text):
    is_word = True
    count_words = 0
    words = 0
    indexes = []
    for i in range(len(text) - 1):
        if (text[i] == text[i+1] and is_word):
            count_words += 1
            is_word = False
            indexes.append(words)
        if (text[i] == ' '):
            is_word = True
            words += 1
    print("Amount of words with same alphas: ", count_words)
    print(indexes)


def print_in_alphabetical_order(text):
    words = text.split()
    sort = sorted(words)
    print(sort)

# x = int(input("Введите значение x: "))
# eps = float(input("Введите желаемую точность вычислений eps:"))
# result = calc_seriece(x, eps)
# print_result(result)

# check_input()
# str_check()

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка! Введите число: ")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка! Введите число: ")


def enter_elements():
    count = get_int("Введите количество элементов которое будет в списке: ")
    values = []
    for i in range(count):
        value = get_float("Введите элемент списка: ")
        values.append(value)
    return values

def task_execution(value_list):
    C = get_float("Введите параметр C элементы больше которого будут подсчитываться: ")
    amounts = 0
    for i in value_list:
        if (i > 0 and i > C):
            amounts += 1
    print("Количество положительных элементов списка больше ", C,  " равно: ", amounts)

def calc_multiplying(value_list):
    max_value = abs(value_list[0])
    index_max = 0
    for i in range(len(value_list)):
        if (abs(value_list[i]) > max_value):
            max_value = value_list[i]
            index_max = i 

    result = value_list[index_max]
    for i in range(index_max + 1, len(value_list)):
        result *= value_list[i]
    print("Произведение элементов стоящих после максимального по модулю равно: ", result)


text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

analyze_text(text)
same_alphas(text)

print_in_alphabetical_order(text)


values = enter_elements()
task_execution(values)
calc_multiplying(values)

print("Hello with request") 