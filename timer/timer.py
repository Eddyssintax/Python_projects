#timer for your function
import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.monotonic()
        retval = func(*args, **kwargs)
        after = time.monotonic()- before
        print(f"Function {func.__name__}: {after:05f} seconds")
        return retval
    return wrapper
