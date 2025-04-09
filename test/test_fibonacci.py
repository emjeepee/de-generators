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

def test_function_fib_raises_first_StopIter_exception():
    fib_gen = fib(4)
    
    stop_iter_raised = False

    expected = True

    for i in range(5):
        try:
            next(fib_gen)
        except StopIteration:
            print("StopIteration WAS reaised")
            stop_iter_raised = True
            result = stop_iter_raised
            assert result == expected


def test_function_fib_raises_first_StopIter_exception_second_time():
    fib_gen = fib(3)
    
    # stop_iter_raised = False
    # expected = True

    for i in range(1, 6):
        try:
            next(fib_gen)
        except StopIteration:
            with pytest.raises(StopIteration):
                next(fib_gen)
            












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
