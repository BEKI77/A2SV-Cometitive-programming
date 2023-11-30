class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        n = len(command)
        for i in range(0,n):
            if command[i]=='G':
                ans+='G'
            elif command[i:i+2] == '()':
                ans+='o'
            elif command[i:i+4] == '(al)':
                ans+='al'
        return ans