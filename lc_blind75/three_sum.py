from typing import List
def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums.sort()  # ← crucial step
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Now solve 2Sum for the remaining part: target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    # Test case 1: Standard case with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums1))  # Expected: [[-1, -1, 2], [-1, 0, 1]]

    # Test case 2: No valid triplets
    nums2 = [1, 2, 3, 4, 5]
    print(three_sum(nums2))  # Expected: []

    # Test case 3: All zeros
    nums3 = [0, 0, 0, 0]
    print(three_sum(nums3))  # Expected: [[0, 0, 0]]

    # Test case 4: Less than 3 elements
    nums4 = [1, 2]
    print(three_sum(nums4))  # Expected: []