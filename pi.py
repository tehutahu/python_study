#! python3
# gaus=rujandoru

import numpy

# update
def update(a, b, t, p):
    new_a = (a + b)/2
    new_b = numpy.sqrt(a * b)
    new_t = t - p *(a - new_a)**2
    new_p = 2 * p
    return new_a, new_b, new_t, new_p

# init
a = 1
b = 1 / numpy.sqrt(2)
t = 1 / 4
p = 1
pi = (a + b)**2/(4*t)
count = 10
print('0 : {0:.10f}'.format(pi))

# run
for i in range(count):
    a, b, t, p = update(a, b, t, p)
    pi = (a + b)**2/(4*t)
    print("{0} : {1:.15f}".format(i+1, pi))
