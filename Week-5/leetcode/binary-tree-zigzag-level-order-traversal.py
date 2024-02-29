# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        currentLevel = []
        nextLevel = []
        ltr = True
        currentLevel.append((root,0))
        ans = []
        while currentLevel:
            temp,lvl = currentLevel.pop()

            if len(ans) == lvl:
                ans.append([temp.val])
            else:
                ans[lvl].append(temp.val)       

            if ltr: 
                if temp.left:
                    nextLevel.append((temp.left, lvl+1))
                if temp.right:
                    nextLevel.append((temp.right, lvl+1))
            else:
                if temp.right:
                    nextLevel.append((temp.right, lvl+1))
                if temp.left:
                    nextLevel.append((temp.left, lvl+1))

            if not currentLevel:
                ltr = not ltr
                currentLevel, nextLevel = nextLevel, currentLevel
                
        return ans