'''
The **kwargs allows you to pass keyworded variable length of arguments to a function.
You should use **kwargs if you want to handle named arguments in a function.

*args = list of arguments -as positional arguments
**kwargs = dictionary - whose keys become separate keyword arguments and
the values become values of these arguments.

The syntax is the * and **. The names *args and **kwargs are only by convention but there's no hard requirement to use them.
You would use *args when you're not sure how many arguments might be passed to your function, 
i.e. it allows you pass an arbitrary number of arguments to your function.
Similarly, **kwargs allows you to handle named arguments that you have not defined in advance:
'''


# EXAMPLE 1: You would use *args when you're not sure how many arguments might
# be passed to your function, i.e. it allows you pass an arbitrary number of arguments to your function:
# ==============================================================================
def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}. {1}'.format(count, thing)

print_everything('apple', 'banana', 'cabbage')
print


# EXAMPLE 2: The **kwargs allows you to handle named arguments that you have not defined in advance:
# ==============================================================================
def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)

table_things(apple = 'fruit', cabbage = 'vegetable')


# EXAMPLE 3: Using une function with 3 different types of parameters:
# ==============================================================================
def func(arg, *args, **kwargs):
    # arg is a positional-only parameter.
    print arg

    # args is a tuple of positional arguments.
    # because the parameter name has * prepended.
    if args:
        print args

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended
    if kwargs: # if kwargs is not empty
        print kwargs

# func() # It will raise error related to parameters.
func('required argument')
func('required argument', 1, 2, '3')
func('required argument', 1, 2, '3', keyword1=4, keyword2='foo')
print


# EXAMPLE 4: You can use these along with named arguments too:
# ==============================================================================
# The explicit arguments get values first and then everything else is passed to *args and **kwargs.
# The named arguments come first in the list. For example:
def print_three_things(arg1, arg2, arg3, arg4):
    print 'arg1 = {0}, arg2 = {1}, arg3 = {2}, arg4 = {3}'.format(arg1, arg2, arg3, arg4)

mylist = ['cat', 'dog', 'cow', 'bird']
print_three_things(*mylist)
print