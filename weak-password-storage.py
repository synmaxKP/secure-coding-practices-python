import hashlib

def create_user(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # Store the username and hashed password in the database
    store_user_credentials(username, hashed_password)

    return "User created successfully."
