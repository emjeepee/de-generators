from src.fibonacci import fib
import pytest

def test_fibonacci_function_returns_first_item():
    fib_gen = fib(1)
    assert next(fib_gen) == 1 


def test_fibonacci_function_returns_fourth_items():

    fib_gen = fib(4) 
    assert next(fib_gen) == 1
    assert next(fib_gen) == 1
    assert next(fib_gen) == 2
    assert next(fib_gen) == 3

def test_fibonacci_function_returns_seven_items():

    fib_gen = fib(7) 
    assert next(fib_gen) == 1
    assert next(fib_gen) == 1
    assert next(fib_gen) == 2
    assert next(fib_gen) == 3
    assert next(fib_gen) == 5
    assert next(fib_gen) == 8
    assert next(fib_gen) == 13

def test_fibonacci_function_raises_Stop_Iteration_error():
    fib_gen = fib(4)

    for i in range(5):
        next(fib_gen)
        if i ==  4:
            print(next(fib_gen()))
            #assert next(fib_gen) == StopIteration 

    # while True:
    #     try:
    #         next(fib_gen)
    #     except StopIteration:
    #         with pytest.raises(StopIteration):
    #             next(fib_gen)
    #             break

# def test_fibonacci_function_raises_Stop_Iteration_error():
#     fib_gen = fib(7)

#     while True:
#         try:
#             next(fib_gen)
#         except StopIteration:
#             with pytest.raises(StopIteration):
#                 next(fib_gen)
#                 break
