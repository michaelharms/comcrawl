"""Multithreading Helpers.

This module contains utility functions
to manage multi-threading.

"""

from typing import Callable, List
from concurrent import futures


def make_multithreaded(func: Callable,
                       threads: int) -> Callable:
    """Creates a multithreaded version of a function.

    Args:
        func: Function that is meant to be executed on
            a list of input objects.
        threads: The number of threads the multithreaded
            version of the function should use.

    Returns:
        A multithreaded version of the `func` input function.

    """

    def multithreaded_function(input_list: List, *args) -> List:
        """Executes function on input list using multiple threads.

        Args:
            input_list: The list of objects a function should be
                executed on.
            *args: Variable length argument list of additional
                parameters needed for the function to be executed.

        Returns:
            List of results after all input list elements were
            processed. Input order might not be preserved in
            output list.

        """
        results = []

        with futures.ThreadPoolExecutor(max_workers=threads) as executor:
            future_to_input_item = {
                executor.submit(
                    func,
                    input_item,
                    *args
                ): input_item for input_item in input_list
            }

            for future in futures.as_completed(future_to_input_item):
                result = future.result()

                if isinstance(result, List):
                    results.extend(result)
                else:
                    results.append(result)

        return results

    return multithreaded_function
