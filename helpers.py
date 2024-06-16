import random
import string
import allure


@allure.step('Генерируем случайную строку')
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
