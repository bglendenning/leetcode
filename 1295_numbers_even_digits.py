import argparse
import timeit
from random import randint


def numbers_with_even_digits(nums):
    """https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
    Given an array nums of integers, return how many of them contain an even number of digits.

    Example:
        $ python 1295_numbers_even_digits.py [--nums_len] [--timeit_number]

    Results:
        Per leetcode submission:
        Runtime: 32 ms, faster than 93.15% of Python online submissions for Find Numbers with Even Number of Digits.
        Memory Usage: 13.4 MB, less than 59.89% of Python online submissions for Find Numbers with Even Number of Digits.

    :param nums: 1 <= len(nums) <= 500, 0 <= nums[i] <= 1
    :type nums: list
    :returns: number of values in nums with even number of digits
    :rtype: int
    """
    count = 0
    for n in nums:
        if not len(str(n)) % 2:
            count += 1
    return count


def nums(nums_len):
    return [randint(1, 100000) for _ in range(nums_len)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nums_len', type=int, default=500, help='The length of the list of numbers.')
    parser.add_argument('--timeit_number', type=int, default=100000, help='The number of times timeit should loop for'
        ' timing the function. Large --nums_length and --timeit_number values will result in lengthy execution.')
    args = parser.parse_args()
    nums_list = nums(args.nums_len)
    print('%d numbers with even number of digits found in %s.' % (numbers_with_even_digits(nums_list), nums_list))
    print('%s seconds to execute numbers_with_even_digits(nums) %d times, where len(nums) = %d.'
        % (timeit.timeit('numbers_with_even_digits(nums_list)', number=args.timeit_number, globals=globals()),
            args.timeit_number, args.nums_len))
