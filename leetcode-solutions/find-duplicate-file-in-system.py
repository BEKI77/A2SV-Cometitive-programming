class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        ans=[]
        for i in range(len(paths)):
            directoryinfo = paths[i].split()
            dirName = directoryinfo[0]
            for i in range(1,len(directoryinfo)):
                j = directoryinfo[i].index('(')
                fileType = directoryinfo[i][0:j]
                fileName = directoryinfo[i][j:]
                store[fileName].append(dirName+'/'+fileType)
        for i,j in store.items():
            if len(j)>1:
                ans.append(j)
        return ans

