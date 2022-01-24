a = int(input("enter number: "))
if a>1:
    for x in range(2, a):
        if(a%x) != 0:
            print("It's a prime number")
            break
        else:
            print("It's not a prime")
            break
else:
    print("not prime")
