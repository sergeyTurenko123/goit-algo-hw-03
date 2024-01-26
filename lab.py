Завдання №1

from datetime import  datetime, timedelta

def get_days_from_today():
    dfey_input = input("Введіть дату:(YYYY-MM-DD) ")
    date = datetime.strptime(dfey_input, "%Y-%m-%d")
    now = datetime.now()
    get_days_from_today = abs(now.toordinal() - date.toordinal())
    return(get_days_from_today)

date = get_days_from_today()
print(f"{date} днів")

Завдання №2

import random

def get_numbers_ticket(min, max, quantity):
    N = 999
    population = range(1, N+1)
    get_numbers_ticket = random.choices(population, weights=None, cum_weights=None, k=6)
    return(get_numbers_ticket)

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Завдання №3

def normalize_phone(phone_number):
