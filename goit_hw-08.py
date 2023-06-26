from datetime import datetime, timedelta

def get_period():
    current_date = datetime.now().date()
    start_of_next_week = current_date + timedelta(days=(7 - current_date.weekday()))
    end_of_next_week = start_of_next_week + timedelta(days=6)
    return start_of_next_week, end_of_next_week

def get_birthdays_per_week(users):
    start_of_next_week, end_of_next_week = get_period()
    birthdays_per_day = {}

    for user in users:
        birthday = user['birthday'].date()

        if start_of_next_week.month == birthday.month and start_of_next_week.day <= birthday.day <= end_of_next_week.day:
            day_of_week = birthday.strftime('%A')
            if day_of_week not in birthdays_per_day:
                birthdays_per_day[day_of_week] = []
            birthdays_per_day[day_of_week].append(user['name'])

    for day_of_week, user_list in birthdays_per_day.items():
        user_str = ', '.join(user_list)
        print(f"{day_of_week}: {user_str}")