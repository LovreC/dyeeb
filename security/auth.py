from flask import request

def authenticate_user(email, password):
    # Dummy authentication (replace with real logic)
    if email == "test@example.com" and password == "password123":
        return True
    return False
