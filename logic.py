from datetime import datetime


def calculate_days_left():
    
    current_date_input = input("Enter the current date (YYYY-MM-DD) or press Enter to use today's date: ")
    if current_date_input.strip() == "":
        current_date = datetime.now()
    else:
        current_date = datetime.strptime(current_date_input, "%Y-%m-%d")
    
   
    future_date_input = input("Enter the future date (YYYY-MM-DD) or press Enter to use January 1 of next year: ")
    if future_date_input.strip() == "":
        future_date = datetime(current_date.year + 1, 1, 1)
    else:
        future_date = datetime.strptime(future_date_input, "%Y-%m-%d")
    
    days_left = (future_date - current_date).days + 1 
    return days_left

days_left = calculate_days_left()
print(f"There are {days_left} days left between the two dates (including today).")
