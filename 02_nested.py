# Nested Functions
# Functions can call other functions within them, making it easy to organize your code into neat, clear pieces. Below are manual implementations of the sum(), mean(), and variance() functions for a list of numbers. The perform_calculation() function takes a list of numbers, along with an optional operation specifier for which function we want to run.

def sum(numbers):
    total = 0.
    for n in numbers:
        total += n
    return total

def mean(numbers):
    return sum(numbers) / len(numbers)

def variance(numbers):
    sq_mean_deviations = []
    num_mean = mean(numbers)
    for n in numbers:
        sq_mean_deviations.append((n - num_mean)**2)
    return mean(sq_mean_deviations)

def perform_calculation(numbers, operation='sum'):
    if operation == 'sum':
        return sum(numbers)
    elif operation == 'mean':
        return mean(numbers)
    elif operation == 'variance':
        return variance(numbers)
    else:
        return None
# The mean() function uses the sum() function internally, and the variance() function uses the mean() function. The perform_calculation() function is able to call any of these three functions. In addition, our code is more compact and clear than if we had coded the math operations from scratch every time.









# Passing Functions Into Functions
# Any Python object can be passed in as a function argument — even functions themselves! For example, we could change the perform_calculation() function to take a function instead of a string for the operation keyword argument.

def perform_calculation(numbers, operation=sum):
    return operation(numbers)
# Now, the operation variable is assigned as the function we want to perform on our numbers, and sum() is our default function. To modify the function to perform on our numbers, all we need to do is specify the alternate function.

perform_calculation(numbers, operation=mean)

perform_calculation(numbers, operation=variance)
# Notice here that we are not calling the function, as there are no parentheses following mean or variance when we pass it in to the operation keyword argument. Without parentheses, we are referring to the function object itself.





# *args
# You may be wondering if it is possible to define a function that can take an arbitrary number of arguments or keyword arguments. For example, if there was no way to know in advance exactly how many arguments or keyword arguments will be supplied to the function.

# What if we wanted our adder() function from earlier to add together any amount of numbers supplied as arguments? What if we wanted the function below to work?

adder(1, 2)
> 3

adder(4, 5, 6, 5)
> 20
# It's possible to define functions to work in this way. Instead of writing out each argument name, we can put *args in the function definition.

def adder(*args):
    total = 0
    print('args:', args)
    for arg in args:
        total += arg
    return total
# *args becomes a tuple containing the arguments supplied to the function when it's called. We then iterate through the *args tuple and add the values to the total. By printing *args in our function, we can see what happens.

adder(1, 2, 3)
> args: (1, 2, 3)
> 6

adder(7, 33)
> args: (7, 33)
> 40
