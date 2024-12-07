How It Works:

    Initialization:
        The password is predefined as "Marvel".
        The user gets a maximum of 3 attempts to guess the password.

    Main Loop:
        The program keeps asking the user for the password as long as:
            The user's guess is incorrect.
            They still have attempts remaining.
        After each guess, the program increments the guess_count.

    Access Decision:
        If the user uses all their attempts without guessing correctly, access is denied.
        If the user guesses correctly within the limit, access is granted.

Example Execution:
Case 1: Correct Password Within Limit

Enter password: Marvel

Access Granted

Case 2: Incorrect Password Exceeds Limit

Enter password: Thanos

Enter password: Spiderman

Enter password: Thor

Access Denied

Notes:

    The program is case-sensitive. "marvel" would be considered incorrect.
    You can customize the password and guess_limit values as needed.
