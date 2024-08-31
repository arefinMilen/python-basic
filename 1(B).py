def add_missing_days(days):
    missing_days = ['Monday', 'Wednesday']
    for day in missing_days:
        days.append(day)
    days.sort()
    return days

def check_day(day):
    if day == 'Friday':
        return 'Today is a holiday'
    else:
        return 'Today is a working day'

# Initial list of days
days_of_week = ['Saturday', 'Sunday', 'Tuesday', 'Thursday']

# Add missing days
days_of_week = add_missing_days(days_of_week)

# Check if today is a holiday
today = 'Friday'
print(check_day(today))

# Check if a specific day is a holiday
specific_day = 'Monday'
print(check_day(specific_day))
