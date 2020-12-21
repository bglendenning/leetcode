import argparse
import timeit
from random import randint


def find_max_consecutive_ones(nums):
    """https://leetcode.com/problems/max-consecutive-ones/
    Given a binary array, find the maximum number of consecutive 1s in this array.

    Example:
        $ python max_consecutive_ones.py [--nums_len] [--timeit_number]

    Results:
        Per leetcode submission:
            Runtime: 284 ms, faster than 93.22% of Python online submissions for Max Consecutive Ones.
            Memory Usage: 13.6 MB, less than 87.07% of Python online submissions for Max Consecutive Ones.

    :param nums: 0 <= len(list) <= 10,000. contains only values of 0 & 1
    :type nums: list
    :returns: maximum number of consecutive 1s in nums
    :rtype: int
    """
    total = temp = 0
    for n in nums:
        if n:
            temp += n
            if temp > total:
                total = temp
        else:
            temp = 0
    return total


def nums(nums_len):
    return [randint(0, 1) for _ in range(nums_len)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nums_len', type=int, default=100, help='The length of the list of 1s & 0s.')
    parser.add_argument('--timeit_number', type=int, default=100000, help='The number of times timeit should loop for'
        ' timing the function. Large --nums_length and --timeit_number values will result in lengthy execution.')
    args = parser.parse_args()
    nums_list = nums(args.nums_len)
    print('%s seconds to execute find_max_consecutive_ones(nums) %d times, where len(nums) = %s.'
        % (timeit.timeit('find_max_consecutive_ones(nums_list)', number=args.timeit_number, globals=globals()),
            args.timeit_number, args.nums_len))
