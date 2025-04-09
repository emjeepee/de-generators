"""

You have already come across the Fibonacci sequence in our study of recursion. 
Starting with the numbers 1, 1, ..., 
we generate the next member of the sequence 
by adding the previous two numbers. 
So the first few terms are:

1, 1, 2, 3, 5, 8, ...
Suppose we want to find the nth member of the sequence. 
As we saw, we can use a recursive function:

def fib(n):
    if n <= 2: return 1
    return fib(n - 1) + fib(n - 2)

This looks elegant and is useful for learning about recursion, 
but it is an impractical solution to the problem. 
It is very slow, taking significant time to compute even 
relatively early terms of the sequence (such as fib(40)).

Your first task today will be to recreate the fib function, 
except this time it should return a generator.

An example of how the fib function should work is shown below:

fib_gen = fib(3)

next(fib_gen) # 1
next(fib_gen) # 1
next(fib_gen) # 2
next(fib_gen) # StopIterationError
The generator should be capable of computing fib(10000) 
in less than one second.

Hints
The builtin time module might be useful for measuring how long execution takes.

Note: the easiest way to get the nth Fibonacci number is to use the formula. 
Unfortunately, that's too easy. Use a generator.

"""

# 1 1 2 3 5 8 13

# if i = 3 counter_a = 1 counter_b = 1 counter_c = 0
# yield counter_a + counter_b

# if i = 4 counter_a = 1 counter_b = 2 
# counter_c = counter_a + counter_b 
# counter_a = counter_b 
# counter_b = counter_c 
# yield counter_a + counter_b

# if i = 5 counter_a = 2 counter_b = 3 
# yield counter_a + counter_b 

# the following function will call yield
# n times:
def fib(n):
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

    # 1    1    2    3    5    8    13


# def fib_2(n):
#     if n <= 2: 
#         yield 1
#     yield fib(n - 1) + fib(n - 2)







# fib_num = fib(6) # generator obj
# print(next(fib_num)) # result is a value 


# def fib(n):
#     if n <= 2: return 1
#     return fib(n - 1) + fib(n - 2)