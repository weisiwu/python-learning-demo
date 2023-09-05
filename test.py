def my_decorator(fn):
    def wrapper():
        print("执行前")
        fn()
        print("执行后")

    return wrapper


@my_decorator
def hello_world():
    print("hello world")


hello_world()
