#! python3
# fibonacchi

import math, sys

# init
a = [1, 1]

#print(a[0], end=', ')


# update
def update(a):
     new_a = [a[1], a[0]+a[1]]
     return new_a

def fibonacchi(n):
    if n < 2:
        return n
    else:
        return fibonacchi(n-2) + fibonacchi(n-1)

if __name__ == '__main__':
    print(fibonacchi(int(sys.argv[1])))
