import colorama
import inspect
class Apple:
    pass

def work_function():
    pass

class Vitamins(Apple):
    pass




dariya = "string"
print(callable(dariya))
print(callable(work_function))
print(inspect.isclass(Apple))
print(inspect.ismodule(Apple))