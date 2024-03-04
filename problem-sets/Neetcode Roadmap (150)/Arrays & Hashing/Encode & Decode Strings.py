class Solution:
    def encode(self, strs):
        out = ""
        for s in strs:
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s):
        out = []
        i = j = 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            out.append(s[i:j])
            i = j
        return out


solution = Solution()

# Test case 1: Empty string
strs = []
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
assert strs == decoded, "Test case 1 failed"

# Test case 2: Single string
strs = ["hello"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
assert strs == decoded, "Test case 2 failed"

# Test case 3: Multiple strings
strs = ["hello", "world", "python"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
assert strs == decoded, "Test case 3 failed"

# Test case 4: Strings with special characters
strs = ["!@#$%^&*()", "1234567890", "abcdefghijklmnopqrstuvwxyz"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
assert strs == decoded, "Test case 4 failed"

print("All test cases passed")
