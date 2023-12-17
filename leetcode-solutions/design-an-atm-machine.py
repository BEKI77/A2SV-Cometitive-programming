class ATM:

    def __init__(self):
        self.bank =[0]*5
        self.pos= [20,50,100,200,500]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.bank[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        cnt=[0 for _ in range(5)]
        for i in range(4,-1,-1):
            cnt[i] = min(self.bank[i], amount//self.pos[i])
            amount -= cnt[i]*self.pos[i]
        
        if amount==0: 
            self.deposit([-x for x in cnt])
            return cnt
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)