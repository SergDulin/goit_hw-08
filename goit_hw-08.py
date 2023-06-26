from datetime import datetime, timedelta

def get_period():
    current_date = datetime.now().date()
    start_of_next_week = current_date + timedelta(days=(7 - current_date.weekday()))
    end_of_next_week = start_of_next_week + timedelta(days=6)
    return start_of_next_week, end_of_next_week