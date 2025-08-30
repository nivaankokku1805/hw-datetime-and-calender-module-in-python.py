import calendar

# Get all month names
months = list(calendar.month_name)

# Remove the first empty string (index 0)
months = months[1:]

print("Months using calendar module:")
print(months)

#example 2

import datetime

# Generate month names using datetime
months = [datetime.date(2023, month, 1).strftime('%B') for month in range(1, 13)]

print("Months using datetime module:")
print(months)