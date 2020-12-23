import argparse
import timeit
from random import randint


def squares_of_sorted_array(nums):
    """https://leetcode.com/problems/squares-of-a-sorted-array/
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
    non-decreasing order.

    Example:
        $ python 977_squares_of_sorted_array [--nums_len] [--timeit_number]

    Results:
        Per leetcode submission:
            Runtime: 176 ms, faster than 95.27% of Python online submissions for Squares of a Sorted Array.
            Memory Usage: 15.4 MB, less than 88.35% of Python online submissions for Squares of a Sorted Array.


    :param nums: 1 <= len(nums) <= 10^4, -10^4 <= nums[i] <= 10^4, sorted by value ascending
    :type nums: list
    :returns: squares of values in nums, sorted by value ascending
    :rtype: list
    """
    return sorted((n ** 2 for n in nums))


def nums(nums_len):
    return [randint(1, nums_len) for _ in range(nums_len)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nums_len', type=int, default=10 ** 4, help='The length of the list of numbers.')
    parser.add_argument('--timeit_number', type=int, default=10 ** 5, help='The number of times timeit should loop for'
        ' timing the function. Large --nums_length and --timeit_number values will result in lengthy execution.')
    args = parser.parse_args()
    nums_list = nums(args.nums_len)
    print('Squares of values in %s: %s.' % (nums_list, squares_of_sorted_array(nums_list)))
    print('%s seconds to execute squares_of_sorted_array(nums) %d times, where len(nums) = %d.'
        % (timeit.timeit('squares_of_sorted_array(nums_list)', number=args.timeit_number, globals=globals()),
            args.timeit_number, args.nums_len))
