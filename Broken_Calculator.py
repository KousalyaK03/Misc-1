# Approach:
# Instead of moving forward from startValue to target, we work backward from target to startValue.
# If the target is greater than startValue:
#    - If target is even, we divide by 2 (reverse of multiplication).
#    - If target is odd, we increment by 1 (reverse of subtraction) to make it even.
# Continue this until target is less than or equal to startValue, at which point we subtract to reach startValue.

# Time Complexity: O(log target), since we are halving the target in most cases.
# Space Complexity: O(1), as we use only a few variables.

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0  # Initialize count of operations

        # Work backward from target to startValue
        while target > startValue:
            if target % 2 == 0:  
                target //= 2  # If target is even, divide by 2
            else:
                target += 1  # If target is odd, increment to make it even
            operations += 1  # Increment operation count
        
        # If target has become smaller than startValue, we need to add the remaining difference
        return operations + (startValue - target)  # The remaining difference is handled by subtraction
