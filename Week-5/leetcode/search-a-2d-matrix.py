class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr,nc = len(matrix)-1, len(matrix[0])-1
        l,r = 0 , nr
        while l<=r:
            m = l+((r-l)//2)
            if matrix[m][0] <= target <= matrix[m][nc]:
                lc,rc = 0 , nc
                while lc<=rc:
                    mn = lc + ((rc-lc)//2)
                    if matrix[m][mn]<target:
                        lc = mn+1
                    elif matrix[m][mn]>target:
                        rc = mn-1
                    else:
                        return True
                return False
            elif target<matrix[m][0]:
                r = m-1
            else:
                l = m+1

        return False