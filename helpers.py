import datetime

def day_of_week():

    # Get the current date
    current_date = datetime.datetime.now()

    # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, and so on)
    day_of_week = current_date.weekday()

    return day_of_week

def get_tommorow():

    # Get the current date
    current_date = datetime.datetime.now()

    # Calculate the date of tomorrow
    tomorrow_date = current_date + datetime.timedelta(days=1)

    # Format the date as "dd-mm" without leading zeros
    formatted_day = tomorrow_date.strftime('%d').lstrip("0")
    formatted_month = tomorrow_date.strftime('%m').lstrip("0")
    formatted_date = f"{formatted_day}-{formatted_month}"

    print("Date of tomorrow:", formatted_date)
    return formatted_date

