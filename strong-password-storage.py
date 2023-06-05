import bcrypt

def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt)

    # Store the username and hashed password in the database
    store_user_credentials(username, hashed_password)

    return "User created successfully." 