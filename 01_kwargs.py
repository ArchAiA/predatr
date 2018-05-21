# Keyword Arguments, Continued
# Functions can take multiple keyword arguments, just like they can take multiple arguments.

# You can define a function as taking any combination of arguments and keyword arguments, but note that keyword arguments must always come after normal arguments!

def func1():
    # code...

def func2(arg1, arg2, arg3, kwarg1=1, kwarg2=True, kwarg3=[1,2,3]):
    # code...

def func3(kwarg1=True, kwarg2=False):
    # code...
# Remember that arguments must be provided when the function is called, but keyword arguments are not required, as there is a default specified. You could, for example, call func3() above without inputs, as all of the arguments are keyword arguments.

