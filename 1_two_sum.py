import argparse
import timeit
from random import randint


def two_sum(nums, target):
    """https://leetcode.com/problems/two-sum/
    Given an array nums of integers, return how many of them contain an even number of digits.
    Credit to: https://leetcode.com/problems/two-sum/discuss/952424/solution-using-dicts-O(n)-Py3 for providing a
    solution I studied that allowed me to better understand using hash tables to reduce time complexity for problems of
    this type. Before this, my solution was (O)n^2 complexity, using a nested loop that was very inefficient for large
    lists.

    Example:
        $ python 1295_numbers_even_digits.py [--nums_len] [--timeit_number]

    Results:
        Per leetcode submission:
        Runtime: 28 ms, faster than 94.99% of Python online submissions for Two Sum.
        Memory Usage: 13.4 MB, less than 98.04% of Python online submissions for Two Sum.

    :param nums: 2 <= len(list) <= 10^3, -10^9 <= nums[i] <= 10^9
    :type nums: list
    :param target: -10^9 <= target <= 10^9
    :type target: int
    :returns: indexes of two nums that add to target
    :rtype: list
    """
    needed_to_index_table = dict()
    for i in range(len(nums)):
        needed = target - nums[i]
        if nums[i] not in needed_to_index_table:
            needed_to_index_table[needed] = i
        else:
            return[needed_to_index_table[nums[i]], i]


def nums(nums_len):
    return [randint(-10 ** 9, 10 ** 9) for _ in range(nums_len)]

def target(nums):
    """Create a sum of two values for random indexes in nums such that the indexes are not equal for use as target.

    :param nums: a list of numbers
    :type nums: list
    :returns: the sum of two unique index's values from nums
    :rtype: int
    """
    target_1 = randint(0, len(nums) - 1)
    target_2 = None
    while not target_2 or target_2 == target_1:
        target_2 = randint(0, len(nums) - 1)
    print(target_1, nums[target_1])
    print(target_2, nums[target_2])
    return nums[target_1] + nums[target_2]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--nums_len', type=int, default=10 ** 3, help='The length of the list of numbers.')
    parser.add_argument('--timeit_number', type=int, default=100000, help='The number of times timeit should loop for'
        ' timing the function. Large --nums_length and --timeit_number values will result in lengthy execution.')
    args = parser.parse_args()
    nums_list = nums(args.nums_len)
    target = target(nums_list)
    print('Values %s add to %s.' % (two_sum(nums_list, target), target))
    print('%s seconds to execute two_sum(nums_list, target) %d times, where len(nums) = %d.'
        % (timeit.timeit('two_sum(nums_list, target)', number=args.timeit_number, globals=globals()),
           args.timeit_number, args.nums_len))
