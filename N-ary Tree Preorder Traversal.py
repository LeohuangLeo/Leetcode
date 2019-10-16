#589
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lis = []
        if not root:
            return lis
        lis.append(root.val)
        for children in root.children:
            lis += self.preorder(children)
        return lis
