from datetime import datetime
import itertools
import numbers_1 as numbers_1
from time import sleep
import os
import time

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':']

def current_time():
    current_time = datetime.now()
    return current_time.strftime('%H:%M:%S')

def get_numerals(result, numerals):
    new_numerals = []
    for symbols in result:
        for numerals_number, i in enumerate(numerals):
            if symbols == i:
                new_numerals.append(numbers_1.used_numerals[numerals_number])
            
    new_numerals_0 = []
    new_numerals_1 = []
    new_numerals_2 = []
    new_numerals_3 = []
    new_numerals_4 = []

    for new_numeral in new_numerals:
        new_numerals_0.append(new_numeral[0])
        new_numerals_1.append(new_numeral[1])
        new_numerals_2.append(new_numeral[2])
        new_numerals_3.append(new_numeral[3])
        new_numerals_4.append(new_numeral[4])

    get_used_numerals = [new_numerals_0, new_numerals_1, new_numerals_2, new_numerals_3, new_numerals_4]
    return get_used_numerals


def final_result(get_used_numerals):
    for get_used_numeral in get_used_numerals:
        print(*get_used_numeral)

def blink():
     for i in itertools.count():
          time.sleep(0.5)
          os.system('clear')
          time.sleep(0.5)
          return blink

while True:
    result = list(current_time())
    get_used_numerals = get_numerals(result, numerals)
    final_result(get_used_numerals)
    sleep(1)
    os.system('clear')
    result_blink = blink()