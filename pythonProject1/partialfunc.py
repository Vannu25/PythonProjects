#Partial functions allow us to fix
# a certain number of arguments of a function
# and generate a new function.

from functools import partial

# A normal function
def f(a, b, c, x):
	return 1000*a + 100*b + 10*c + x

# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

#f is partial func

# Calling g()
print(g(5))


from functools import *

# A normal function
def add(a, b, c):
	return 100 * a + 10 * b + c
#a=3, b=2, c=1

# A partial function with b = 1 and c = 2
add_part = partial(add, c = 2, b = 1)

# Calling partial function
print(add_part(3))

#in functools we have the inbuilt partial func

