def true_email(email):
    user, domain = email.split('@')

    if not user or not domain:
        return False

    for char in user:
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
    if not true_email(email):
        raise ValueError("Некорректный адрес электронной почты")
    return email

email_addr = input("Введите адрес электронной почты: ")

try:
    validated_email = validate_email(email_addr)
    print("Адрес электронной почты корректен:", validated_email)
except ValueError as e:
    print("Ошибка:", e)
