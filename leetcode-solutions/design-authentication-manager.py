class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.time=timeToLive
        self.map = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId]= currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map and self.map[tokenId]+self.time > currentTime:
            self.map[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for i in self.map:
            if self.map[i]+self.time > currentTime:
                ans+=1

        return ans


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)