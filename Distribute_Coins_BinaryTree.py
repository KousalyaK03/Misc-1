# Approach:
# We perform a postorder traversal of the tree to calculate the number of moves needed.
# Each node should have exactly one coin. If a node has extra coins, it passes the excess to its parent.
# If a node has a deficit, it requests the required coins from its parent.
# The absolute sum of all coin excess/deficit across nodes gives the minimum moves required.

# Time Complexity: O(n), since we visit each node once in a postorder traversal.
# Space Complexity: O(h), where h is the height of the tree (O(log n) for balanced trees, O(n) in the worst case).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0  # Variable to store the number of moves

        def dfs(node):
            if not node:
                return 0  # Base case: If node is None, return 0 excess coins

            # Recursively get the excess/deficit from left and right subtrees
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)

            # The number of moves needed is the sum of absolute excess from left and right
            self.moves += abs(left_excess) + abs(right_excess)

            # Return the net excess coins at this node to pass to its parent
            return node.val + left_excess + right_excess - 1  # -1 since each node needs one coin
        
        dfs(root)  # Start the postorder traversal from the root
        return self.moves  # Return the total number of moves
