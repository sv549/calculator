def decorator(func):
    def decorator_do_twice(a,b):
        func()
        func()

        return decorator_do_twice()
