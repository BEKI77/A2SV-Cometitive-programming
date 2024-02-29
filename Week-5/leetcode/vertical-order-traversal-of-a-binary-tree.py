# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dicCol = defaultdict(lambda: defaultdict(list))
        print(dicCol)
        def rec(root, xi,yi):
            if root:
                dicCol[xi][yi].append(root.val)
                rec(root.left, xi-1,yi+1)
                rec(root.right, xi+1, yi+1)
        ans = []
        rec(root, 0, 0)
        for i in sorted(dicCol):
            temp = []
            for j in sorted(dicCol[i]):
                for k in sorted(dicCol[i][j]):
                    temp.append(k)
            ans.append(temp)

        print(ans)
        return ans