def decorator(func):
    def decorator_do_twice(a,b):
        if a < 0 and b < 0:
            print("Must be a number greater than 0")
        

        return decorator_do_twice()
