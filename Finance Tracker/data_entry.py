from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I":"Income", "E":"Expenses"}
def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid Format. Enter date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount Must be a non-negative Integer")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    pass

def description():
    pass