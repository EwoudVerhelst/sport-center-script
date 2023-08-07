import datetime

# Get the current date and time
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define the file name
file_name = "current_datetime.txt"

# Write the date and time to the file
with open(file_name, "w") as file:
    file.write(current_datetime)

print(f"Current date and time ({current_datetime}) has been written to {file_name}.")
