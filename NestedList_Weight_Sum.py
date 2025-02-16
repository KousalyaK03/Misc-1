# Approach:
# We use a recursive approach to traverse the nested list and calculate the weighted sum.
# If an element is an integer, multiply it by its depth and add it to the sum.
# If an element is a list, recursively process it with an increased depth.
# We start with an initial depth of 1 and traverse all elements in the list.

# Time Complexity: O(N), where N is the total number of nested elements (both integers and lists).
# Space Complexity: O(D), where D is the maximum depth of nesting (due to recursive stack).

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_list, depth):
            total = 0  # Variable to store sum at the current level
            
            for item in nested_list:
                if item.isInteger():  
                    total += item.getInteger() * depth  # Multiply integer value by its depth
                else:
                    total += dfs(item.getList(), depth + 1)  # Recursively process nested lists with increased depth
            
            return total  # Return the accumulated sum for the current level
        
        return dfs(nestedList, 1)  # Start the DFS traversal with initial depth 1
