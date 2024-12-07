# Set the correct password
password = "Marvel"

# Initialize an empty string for the user's guess
guess = ""

# Initialize the guess counter
guess_count = 0

# Set the maximum number of allowed guesses
guess_limit = 3

# Flag to check if the user is out of guesses
out_of_guesses = False

# Loop until the user guesses the password correctly or runs out of guesses
while guess != password and not out_of_guesses:
    # Check if the user still has guesses left
    if guess_count < guess_limit:
        # Prompt the user to enter a password
        guess = input("Enter password: ")
        # Increment the guess counter
        guess_count += 1
    else:
        # If no guesses are left, set the flag to True
        out_of_guesses = True

# Check if the user is out of guesses
if out_of_guesses:
    # If so, deny access
    print("Access Denied")
else:
    # Otherwise, grant access
    print("Access Granted")
