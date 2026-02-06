"""
LeetCode #371: Sum of Two Integers

Given two integers a and b, return the sum of the two integers
without using the operators + and -.

Hint: Use bit manipulation (XOR for sum, AND for carry)
"""


def get_sum(a: int, b: int) -> int:
    while b != 0:

        # Step 1: Add bits without considering carry
        sum_without_carry = a ^ b

        # Step 2: Find bits that need to carry (both bits are 1)
        carry = a & b

        # Step 3: Shift carry left (carry goes to next bit position)
        carry_shifted = carry << 1

        # Prepare for next iteration
        a = sum_without_carry
        b = carry_shifted

    return a


if __name__ == "__main__":
    # Example 1
    print(f"1 + 2 = {get_sum(1, 2)}")  # Expected: 3

    # Example 2
    print(f"2 + 3 = {get_sum(2, 3)}")  # Expected: 5

    # Example 3: With zero
    print(f"0 + 5 = {get_sum(0, 5)}")  # Expected: 5

    # Example 4: Larger numbers
    print(f"10 + 20 = {get_sum(10, 20)}")  # Expected: 30