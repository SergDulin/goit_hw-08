from datetime import datetime, timedelta

def get_period():
    current_date = datetime.now().date()
    start_period = current_date
    end_period = start_period + timedelta(days=7)
    return start_period, end_period

def get_birthdays_per_week(users):
    start_period, end_period = get_period()
    current_year = datetime.now().year
    birthdays_per_day = {}

    for user in users:
        birthday = user['birthday'].date().replace(year=current_year)

        if start_period <= birthday <= end_period:
            if birthday.weekday() in [5, 6]:
                day_of_week = 'Monday'
            else:
                day_of_week = birthday.strftime('%A')

            if day_of_week not in birthdays_per_day:
                birthdays_per_day[day_of_week] = []
            birthdays_per_day[day_of_week].append(user['name'])

    for day_of_week, user_list in birthdays_per_day.items():
        user_str = ', '.join(user_list)
        print(f"{day_of_week}: {user_str}")

if __name__ == "__main__":
    users = [
        {'name': 'Bill', 'birthday': datetime(1975, 8, 16)},
        {'name': 'Jill', 'birthday': datetime(2003, 7, 8)},
        {'name': 'Kim', 'birthday': datetime(1993, 7, 3)},
        {'name': 'Jan', 'birthday': datetime(1087, 6, 29)},
        {'name': 'Alex', 'birthday': datetime(2006, 7, 4)},
        {'name': 'Serhii', 'birthday': datetime(2001, 7, 1)},
    ]

    get_birthdays_per_week(users)
