#! python3
# suuretu

import sys

# init
a1 = 1

def update(n):
    if n < 2:
        return 1
    else:
        return 2*update(n-1) + 3*(n-1) - 1

def sum(n):
    sum = 0
    for i in range(n):
        sum += update(n)
    return sum

if __name__ == '__main__':
    print(update(int(sys.argv[1])))
    print(sum(int(sys.argv[1])))
