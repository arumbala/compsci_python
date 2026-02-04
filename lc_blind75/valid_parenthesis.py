def is_valid(s: str) -> bool:
    stack = []  # list works perfectly as stack in Python

    # Mapping of opening → expected closing bracket
    pairs = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pairs:  # it's an opening bracket
            stack.append(pairs[char])  # push the expected closing one
        elif not stack or stack.pop() != char:
            # either stack is empty or top doesn't match current closing bracket
            return False

    return len(stack) == 0

if __name__ == "__main__":
    print(is_valid('()[]'))