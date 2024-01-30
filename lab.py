# # Завдання №1

import datetime 
from datetime import  datetime, timedelta

def get_days_from_today():
    dfey_input = input("Введіть дату:(YYYY-MM-DD) ")
    try :
        date = datetime.strptime(dfey_input, "%Y-%m-%d")
        now = datetime.now()
        get_days_from_today = abs(now.toordinal() - date.toordinal())
        return(get_days_from_today)
    except ValueError:
        print("{dfey_input} ввели неправильний формат дати")

date = get_days_from_today()
print(f"{date} днів")

# # # Завдання №2

import random

def get_numbers_ticket(min, max, quantity):
    N = 999
    population = range(1, N+1)
    get_numbers_ticket = random.choices(population, weights=None, cum_weights=None, k=6)
    return(get_numbers_ticket)

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# # Завдання №3

import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11  ",
]
def normalize_phone(raw_numbers):
    pattern = r"[\s\D]"
    repl = r""
    match = re.sub(pattern, repl, raw_numbers)
    if len(match) == 10:
        normalize_phone = f"+38{match}"
    elif len(match) == 11:
            normalize_phone = f"+3{match}"
    elif len(match) == 12:
            normalize_phone = f"+{match}"
    else:
        normalize_phone = match
    return(normalize_phone)

sanitized_numbers = [normalize_phone(num)for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Завдання 4
import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.01.31"},
    {"name": "Jane Smith", "birthday": "1990.02.3"},
    {"name": "Hane NGith", "birthday": "1984.06.15"}
    ]

def get_upcoming_birthdays(users = None):
    now = dtdt.today().date() #поточний час
    birthday = []
    for user in users:
        date_user = user["birthday"] 
        date_user = str(now.year) + date_user[4: ]
        date_user = dtdt.strptime(date_user, "%Y.%m.%d").date() #парсинг дати
        week_day = date_user.isoweekday()
        difference_day = (date_user - now).days
        if 1 < difference_day < 7 :
            if difference_day < 6 :
                birthday.append({"name": user["name"], "birthday":date_user.strftime("%Y.%m.%d")})
            else:
                if difference_day == 7:
                    birthday.append({"name": user["name"], "birthday":(date_user + dt.timedelta(days = 1)).strftime("%Y.%m.%d")})
                elif difference_day == 6:
                    birthday.append({"name": user["name"], "birthday":(date_user + dt.timedelta(days = 2)).strftime("%Y.%m.%d")})
    return birthday
   
print(get_upcoming_birthdays(users))

