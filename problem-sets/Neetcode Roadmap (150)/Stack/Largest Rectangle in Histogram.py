class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # until taller found than current, pop them and calc their max
        # keep the start from to the recent tallest
        # calculate the max area from the stacked bars
        stack = []
        out = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                si, sh = stack.pop()
                out = max(out, sh * (i - si))
                start = si
            stack.append((start, h))
        for si, sh in stack:
            out = max(out, sh * (len(heights) - si))
        return out


# Test case 1: heights in ascending order
solution = Solution()
heights = [1, 2, 3, 4, 5]
assert solution.largestRectangleArea(heights) == 9

# Test case 2: heights in descending order
heights = [5, 4, 3, 2, 1]
assert solution.largestRectangleArea(heights) == 9

# Test case 3: heights with alternating values
heights = [2, 1, 2, 1, 2]
assert solution.largestRectangleArea(heights) == 5

# Test case 4: heights with repeated values
heights = [2, 2, 2, 2, 2]
assert solution.largestRectangleArea(heights) == 10

# Test case 5: empty heights list
heights = []
assert solution.largestRectangleArea(heights) == 0

print("All tests passed!")
