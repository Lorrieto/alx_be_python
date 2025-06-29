import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
    
display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.date.today()
    days_ahead = timedelta(days= number_of_days)
    future_date = current_date + days_ahead
    future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:",future_date)
    
calculate_future_date()
