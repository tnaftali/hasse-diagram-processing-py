import Validation


def insert_number():
    str_num = input('Please insert a positive integer number: ')
    while not Validation.is_valid_number(str_num):
        str_num = input('Please insert a valid integer positive number: ')
    return int(str_num)