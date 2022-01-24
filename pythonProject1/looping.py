#for loop - it has built in funct like range , can be per on collections like list

# prices = [10, 20, 30, ]
#
# total = 0
# for price in prices:  # inside of prices list
#     total += price
# print(f"Total: {total}")

#nested loops

# for x in range(4):
#     for y in range(3):
#      print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    #print('x' * x_count) - shortcut
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
print('---------------------------------------')
numbers = [2, 2, 2, 2, 6]
for x_count in numbers:
    #print('x' * x_count) - shortcut
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)