def validate_password(password):
    if len(password) < 8:
        return False
    return True

password = input("Enter your password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is weak. Please choose a stronger password.")

