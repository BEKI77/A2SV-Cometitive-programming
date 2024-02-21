class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        li = []
        for i in range(len(tokens)):
            temp = tokens[i]
            if temp == '+':
                sec = li[-1]
                li.pop()
                fir = li[-1]
                li.pop()
                li.append(fir+sec)
            elif temp == '-':
                sec = li[-1]
                li.pop()
                fir = li[-1]
                li.pop()
                li.append(fir-sec)
            elif temp=='*':
                sec = li[-1]
                li.pop()
                fir = li[-1]
                li.pop()
                li.append(fir*sec)
            elif temp =='/':
                sec = li[-1]
                li.pop()
                fir = li[-1]
                li.pop()
                li.append(int(fir/sec))
            else:
                li.append(int(temp))
        return li[-1]