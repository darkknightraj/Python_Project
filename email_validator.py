import re

def is_valid_email(email):
    """
    Validates an email address using a regular expression.
    Returns True if the email is valid, otherwise False.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
if __name__ == "__main__":
    test_email = input("Enter an email to validate: ")
    if is_valid_email(test_email):
        print("The email is valid.")
    else:
        print("The email is invalid.")