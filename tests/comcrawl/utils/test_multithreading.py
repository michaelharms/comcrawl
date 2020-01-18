import threading
from comcrawl.utils.multithreading import make_multithreaded_function


def test_make_multithreaded_function():
    threads_to_use = 4
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    thread_history = {}

    def initial_function(num, history_reference):
        history_reference[num] = threading.active_count()
        return []

    multithreaded_function = make_multithreaded_function(initial_function, threads=threads_to_use)
    multithreaded_function(numbers, thread_history)

    # -1 because ignoring the main thread
    assert max(list(thread_history.values())) - 1 == threads_to_use
