from functools import reduce

def is_even(n):
    return  n%2==0

nums = [3, 5, 8, 6, 9, 15, 4]

evens = list(filter(is_even, nums))
print(evens)

#using lambda func

nums = [3, 5, 8, 6, 9, 15, 4, 16, 15, 14, 13]

odd = list(filter(lambda n : n%2!=0, nums)) #odd
print(odd)

#map
def add_all(a, b):
    return a+b
nums = [3, 5, 8, 6, 9, 15, 4, 16, 15, 14, 13]

evens= list(filter(lambda n : n%2==0, nums))
doubles = list(map(lambda n : n*2, evens))
print(doubles)
#sum = (reduce(add_all, doubles))
sum = reduce(lambda a,b : a+b, doubles)
print(sum)



