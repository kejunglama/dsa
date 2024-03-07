class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # from the nearest car
        stack = [] # 
        for p, s in pair: # for every car
            stack.append((target - p) / s) # add the speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if it is faster than one ahead pop it   
                stack.pop()
        return len(stack)


# Test case 1: Basic scenario with 3 cars
solution = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
assert solution.carFleet(target, position, speed) == 3

print("All test cases passed!")
