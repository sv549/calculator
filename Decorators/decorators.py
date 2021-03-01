def decorator(func):
    def decorator_do_twice():
        func()
        func()

        return decorator_do_twice()