def is_valid_email(email):
    username, domain = email.split('@')

    if not username or not domain:
        return False

    for char in username:
        if not char.isalnum() and char not in '-_.':
            return False

    for char in domain:
        if not char.isalnum() and char not in '-.':
            return False

    if '.' not in domain:
        return False

    if '..' in domain:
        return False
    return True

def validate_email(email):
    if not is_valid_email(email):
        raise ValueError("Некорректный адрес электронной почты")
    return email

email_address = input("Введите адрес электронной почты: ")

try:
    validated_email = validate_email(email_address)
    print("Адрес электронной почты корректен:", validated_email)
except ValueError as e:
    print("Ошибка:", e)
