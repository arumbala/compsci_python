from typing import List
def two_sum(nums: List[int], target: int) -> List[int]:
    visited = {}
    for current_index, current_number in enumerate(nums):
        req_number = target - current_number
        if req_number in visited:
            return [visited[req_number], current_index]
        visited[current_number] = current_index
    return []

if __name__ == '__main__':
    result = two_sum([2,4,6,3,5], 10)
    print(result)