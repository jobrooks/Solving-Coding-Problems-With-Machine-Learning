from datetime import datetime as dt

# Estimated time by the program
estimate = 0
# Actual time by the machine
time = 0

# Prompt the user for a password
password = input("Enter a password: ")

# Check the length of the password
if len(password) < 1 or len(password) > 20:
    print("Password must be between 1 and 20 characters")
    exit()

# Get the current time
start_time = dt.now()

# Calculate the estimated time
estimate += 1  # for the if statement
estimate += 1  # for the assignment of start_time
estimate += 3 * len(password)  # for the comparisons
estimate += 1  # for the return statement

# Check the password
for i in range(len(password)):
    # Estimate the time
    estimate += 3

    # Check if the character matches
    if password[i] != 'A':
        # Update the time
        time = dt.now() - start_time
        print("ACCESS DENIED ({:d} ms)".format(time.microseconds // 1000))
        exit()

# Update the time
time = dt.now() - start_time

# Check if the password is correct
if time.microseconds // 1000 == estimate:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED ({:d} ms)".format(time.microseconds // 1000))