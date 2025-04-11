class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(max_gain(node.left), 0)
        right = max(max_gain(node.right), 0)
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)

    max_gain(root)
    return max_sum
