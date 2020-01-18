"""Multithreading Helpers

This module contains utility functions
to manage multi-threading.

"""

from typing import Callable, List
from concurrent import futures


def make_multithreaded(func: Callable,
                       threads: int) -> Callable:

    def multithreaded_function(input_list: List, *args) -> List:
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
