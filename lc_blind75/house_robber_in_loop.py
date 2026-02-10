"""
LeetCode #198: House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. The only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected — if two adjacent houses are broken into
on the same night, it will automatically contact the police.

Given an integer list nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Hint: At each house you have two choices — rob it (skip the previous) or skip it.
      rob(i) = max(rob(i-1), rob(i-2) + nums[i])

Approach: Bottom-up iterative DP (space-optimized, two variables)
Time:  O(n) — single pass
Space: O(1) — only two variables
"""
from typing import List

def rob(nums: List[int]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    prev1 = nums[0]
    prev2 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev2, nums[i] + prev1)
        prev1 = prev2
        prev2 = current

    return prev2

if __name__ == "__main__":
    # Example 1: [1,2,3,1] -> rob house 0 + house 2 = 1+3 = 4
    print(f"[1,2,3,1]: {rob([1, 2, 3, 1])}")  # Expected: 4

    # Example 2: [2,7,9,3,1] -> rob house 0 + house 2 + house 4 = 2+9+1 = 12
    print(f"[2,7,9,3,1]: {rob([2, 7, 9, 3, 1])}")  # Expected: 12

    # Example 3: single house
    print(f"[5]: {rob([5])}")  # Expected: 5

    # Example 4: two houses — pick the larger
    print(f"[1,2]: {rob([1, 2])}")  # Expected: 2