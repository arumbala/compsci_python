from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Given a sorted array of integers and a target value,
    return the index of the target if found, otherwise return -1.
    """

    if len(nums) < 1:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Example 1: target exists
    print(search([-1, 0, 3, 5, 9, 12], 9))  # Expected: 4

    # Example 2: target does not exist
    print(search([-1, 0, 3, 5, 9, 12], 2))  # Expected: -1
