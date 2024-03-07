# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mp = defaultdict(list)
        ans = 0
        def rec(i,lvl,root):
            if root:
                mp[lvl].append(i)
                rec(i*2,lvl+1,root.left)
                rec(i*2 + 1, lvl+1,root.right)
                      
        rec(0,0,root)
        ans = max(max(mp[i])-min(mp[i])+1 for i in mp)
        return ans