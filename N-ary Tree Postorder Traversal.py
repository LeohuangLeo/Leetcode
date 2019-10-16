#590
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lis = []
        if not root:
            return lis
        lis = [root.val] + lis
        for i in root.children[::-1]:
            lis = self.postorder(i) + lis
        return lis
