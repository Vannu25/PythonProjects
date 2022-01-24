def pyfunc(rows):
    for x in range(rows):
        print(''*(rows-x-1)+'*'*(2*x+1))
pyfunc(5)

#pyramid

def pyfunc(rows):
    for x in range(rows):
        print(' '*(rows-x-1)+'*'*(2*x+1))
pyfunc(5)

#right to left
def pyfunc(rows):
    for x in range(rows):
        print('  '*(rows-x-1)+'*'*(2*x+1))
pyfunc(5)