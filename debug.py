from pprint import pprint


def debug(func):
    def wrapper(*args, **kwargs):
        if args:
            pprint(f"*args: {args}")
        if kwargs:
            pprint(f"**kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
