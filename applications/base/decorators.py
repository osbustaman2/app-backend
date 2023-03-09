def aunthenticate_user(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper


