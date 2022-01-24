names = ['Vannu', 'Sid', 'Ramu']
print(names[:])    # : - return all items, or according to indexing

#find the largest number of list?

numbers = [3, 6, 5, 10, 4, 2, 12]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
print('----------------------------------------------')
#methods in list
# append() - to chnge
# insert()- in add item
# remove() - to remove item
# clear()-to clear all
# pop()-last item can be removed
# index- to check existing items
# count-to count the number of items
# sort- sorts the lists
# reverse- reverse the list
# copy- copy of original list


#remove duplicates form list

numbers = [2, 6, 2, 10, 4, 2, 12]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
    print(uniques)


