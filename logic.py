from datetime import datetime

# Function to calculate days left including the current date
def calculate_days_left():
    # Prompt the user for current date, allow default to today's date
    current_date_input = input("Enter the current date (YYYY-MM-DD) or press Enter to use today's date: ")
    # If the user doesn't enter a date, use today's date
    if current_date_input.strip() == "":
        current_date = datetime.now()
    else:
        current_date = datetime.strptime(current_date_input, "%Y-%m-%d")
    
    # Prompt the user for future date, allow default to January 1 of the next year
    future_date_input = input("Enter the future date (YYYY-MM-DD) or press Enter to use January 1 of next year: ")
    # If the user doesn't enter a date, use January 1 of the next year
    if future_date_input.strip() == "":
        future_date = datetime(current_date.year + 1, 1, 1)
    else:
        future_date = datetime.strptime(future_date_input, "%Y-%m-%d")
    
    # Calculate the difference in days and include the current date
    days_left = (future_date - current_date).days + 1  # Adding 1 to include current date
    return days_left

# Call the function and print the result
days_left = calculate_days_left()
print(f"There are {days_left} days left between the two dates (including today).")
