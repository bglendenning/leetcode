import argparse
import timeit
from random import randint


def duplicate_zeros(nums):
    """https://leetcode.com/problems/duplicate-zeros/
    Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to
    the right.

    Example:
        $ python duplicate_zeros.py [--nums] [--nums_len] [--timeit_number]

    Results:
        Per leetcode submission:
            Runtime: 44 ms, faster than 98.32% of Python online submissions for Duplicate Zeros.
            Memory Usage: 13.7 MB, less than 83.81% of Python online submissions for Duplicate Zeros.

    :param nums: 1 <= len(nums) <= 10^3, 0 <= nums[i] <= 9
    :type nums: list
    :returns: a list of numbers to match nums with a duplicate zero for each zero appearing in nums
    :rtype: list
    """
    arr_len = len(nums)
    insert = nums.insert
    i = 0
    while i < arr_len:
        if nums[i] == 0:
            insert(i, 0)
            i += 2
        else:
            i += 1
    # problem specifies that list must be edited "in place" and length of output should not exceed input length
    del(nums[arr_len:])
    return nums


def nums(nums_len):
    return [randint(0, 9) for _ in range(nums_len)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nums', type=str, help='Comma delimited string of numbers.')
    parser.add_argument('--nums_len', type=int, default=10 ** 3, help='The length of the list of numbers.')
    parser.add_argument('--timeit_number', type=int, default=10 ** 5, help='The number of times timeit should loop for'
        ' timing the function. Large --nums_length and --timeit_number values will result in lengthy execution.')
    args = parser.parse_args()
    if args.nums:
        nums_list = [int(s) for s in args.nums.split(',')]
    else:
        nums_list = nums(args.nums_len)
    print('nums_list with duplicate zeros %s: %s.' % (nums_list, duplicate_zeros(nums_list.copy())))
    print('%s seconds to execute duplicate_zeros(nums) %d times, where len(nums) = %d.'
        % (timeit.timeit('duplicate_zeros(nums_list)', number=args.timeit_number, globals=globals()),
            args.timeit_number, args.nums_len))
