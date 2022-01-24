def pal(num):
    x1 = num[::-1]   #func to reverse
    if x1 == num:
        print("Palindrome")
    else:
        print("Not a Palindrome")

print(pal('madam'))
print(pal('Vanashree'))
print(pal('malayalam'))



