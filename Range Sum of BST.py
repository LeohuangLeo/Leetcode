#938
class Solution:
    def rangeSumBST(self, root, L, R):
        self.ans = 0
        def CalSum(node):
            if node:
                if node.val >= L and node.val <= R:
                    self.ans += node.val
