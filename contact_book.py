import re

def validate_email(email):
    """Validate the email address using a regular expression"""
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

def main():
    """Get user input and validate the email address"""
    email = input("Please enter your email address: ")
    print("The email address you entered is valid." if validate_email(email) else "The email address you entered is not valid.")

if __name__ == "__main__":
    main()