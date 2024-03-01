# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        isBst = True
        li = []
        def rec(root):
            if root and not root.left and not root.right:
                isBst = True
                li.append(root.val)
                return (root.val,root.val,root.val,True)
            elif root and not root.left:
                rL,rR, curVal, isBst = rec(root.right)
                val = curVal+root.val
                if rR<=root.val:
                    isBst = False
                    val = 0
                if isBst:
                    li.append(val)
                return (max(rL,root.val), min(rR,root.val), val, isBst)
            elif root and not root.right:
                lL, lR, curVal, isBst = rec(root.left)
                val = curVal+root.val
                if lL>=root.val:
                    isBst = False
                    val = 0
                if isBst:
                    li.append(val)
                return (max(lL, root.val),min(lR,root.val), val, isBst)
            else:
                lL,lR,lCur, isBst1 = rec(root.left)
                rL,rR,rCur, isBst2 = rec(root.right)
                
                if  lL>= root.val or lR>=root.val:
                    isBst1 = False
                    isBst2 = False   
                if  rR<=root.val or rL<=root.val:
                    isBst1 = False
                    isBst2 = False 

                
                if isBst1 and isBst2:
                    val = rCur+lCur+root.val
                    li.append(val)
                else:
                    val = 0
                return (max(rL,root.val),min(lR,root.val), val ,isBst1 and isBst2)
            
        rec(root)
        ans = sorted(li)[-1]
        return ans if ans>0 else 0