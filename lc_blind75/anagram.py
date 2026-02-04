def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    chars = [0] * 26  # assuming only lowercase letters a-z
    for i in range(len(s)):
        chars[ord(s[i]) - ord('a')] += 1
        chars[ord(t[i]) - ord('a')] -= 1

    for count in chars:
        if count != 0:
            return False

    return True

if __name__ == "__main__":
    print(is_anagram('listen', 'silent'))