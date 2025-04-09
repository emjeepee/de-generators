def fib(n):
    if n <= 2: return 1
    return fib(n - 1) + fib(n - 2)

fib_sequence = fib(6)
# print(fib_sequence)


def fib_test(n):
    a = 1
    b = 1
    c = 0
    for i in range(1,n + 1): 
        if i <= 2: 
            yield a 
        if i > 2:
            yield a + b 

            c = a + b 
            a = b 
            b = c 


fib_gen = fib_test(1)

try:
    next(fib_gen)
    next(fib_gen)
except StopIteration:    
    print(f'StopIteration raised')
    print(StopIteration.msg)

