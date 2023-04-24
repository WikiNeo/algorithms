"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from typing import List
from collections.abc import Iterable


# return list
def flatten(input_arr: Iterable, output_arr: List[int]=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flatten(ele, output_arr)    #tail-recursion
        else:
            output_arr.append(ele)      #produce the result
    return output_arr


# returns iterator
def flatten_iter(iterable: Iterable):
    """
    Takes as input multidimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element