def is_valid_name(name):
    return name.isalpha()

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10  # Assuming phone numbers are 10 digits
