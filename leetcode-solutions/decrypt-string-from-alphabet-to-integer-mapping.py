class Solution:
    def freqAlphabets(self, s: str) -> str:
        arr = []
        for i in s:
            if i == '#':
                first = arr.pop()
                second = arr.pop()
                arr.append(second * 10 + first)
            else:
                arr.append(int(i))

        ans= ''
        
        for num in arr:
            ans += chr(num + 96)
        
        return ans