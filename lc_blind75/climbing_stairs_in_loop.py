"""
LeetCode #70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
"""
def climb_stairs(n: int) -> int:
    if n <= 2:
        return max(n, 0)

    prev1 = 1
    prev2 = 2
    for i in range(2, n):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current

    return prev2


if __name__ == "__main__":
    # Example 1: n = 2 -> 2 ways (1+1 or 2)
    print(f"n=2: {climb_stairs(2)}")  # Expected: 2

    # Example 2: n = 3 -> 3 ways (1+1+1, 1+2, 2+1)
    print(f"n=3: {climb_stairs(3)}")  # Expected: 3

    # Example 3: n = 4 -> 5 ways
    print(f"n=4: {climb_stairs(4)}")  # Expected: 5

    # Example 4: n = 1 -> 1 way
    print(f"n=1: {climb_stairs(1)}")  # Expected: 1