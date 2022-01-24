a = int(input("enter the nums: "))
f = 0
s = 1

if a <= 0:
    print("the fibonacci series is\n", f)
else:
    print(f, s, end=" ")
    for x in range(2, a):
        next = f+s  #next element func
        print(next, end=" ")
        f=s
        s=next