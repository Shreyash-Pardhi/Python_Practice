import datetime
def Date(func):
    def datee(*args, **kwargs):
        print(f"Date and Time: {datetime.datetime.now()}")
        func(*args, **kwargs)
    return datee