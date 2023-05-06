import random
import string

def generate_password(length=12):
    """Generate a random password of specified length"""
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

def number_verifier(amount):
    """Verify that input is a number and format it to 2 decimal places"""
    if isinstance(amount, (int, float)):
        return round(amount, 2)
    else:
        raise ValueError("Input must be a number")
