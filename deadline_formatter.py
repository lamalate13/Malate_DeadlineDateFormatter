# Deadline and Date Formatter
# Version 2: Added Date Formatting

from datetime import date

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Create and format the date
event_date = date(year, month, day)

formatted_title = event_title.strip().upper()
formatted_date = event_date.strftime("%B") + f" {event_date.day}, {event_date.year}"

# Display formatted output
print("\nFormatted Output:")
print("Event:", formatted_title)
print("Date:", formatted_date)
print("Year:", event_date.year)
print("Month:", event_date.strftime("%B"))
print("Day:", event_date.day)
print("Weekday:", event_date.strftime("%A"))
