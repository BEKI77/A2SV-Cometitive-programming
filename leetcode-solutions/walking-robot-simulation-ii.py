class Robot:

    def __init__(self, width: int, height: int):
        self.wi = width - 1
        self.hi = height - 1
        self.dir_mp = { 'East':'North', 'North':'West', 'West':'South','South':'East' }
        self.pos_step = { 'East':[1,0], 'North': [0,1], 'West':[-1,0], 'South':[0,-1] }
        self.position = [0,0]
        self.dir = 'East'
        self.per = 2*(self.wi+self.hi)
    def step(self, num: int) -> None:
        if num > self.per:
            num = num - (num//self.per)*self.per

            if num==0 and self.position==[0,0]:
                self.dir = 'South'
        
        while num>0:
            cur_move = self.pos_step[self.dir]
            max_move = min(self.max_move_dir(), num)
            num -= max_move
            new_wi, new_hi = self.position[0]+cur_move[0]*max_move, self.position[1] + cur_move[1]*max_move
            self.position = [new_wi, new_hi]

            if num>0:
                self.dir = self.dir_mp[self.dir]

    def max_move_dir(self)->int:
        if self.dir == 'East': return self.wi - self.position[0]
        if self.dir == 'North': return self.hi - self.position[1]
        if self.dir == 'West': return self.position[0]
        if self.dir == 'South': return self.position[1]         
    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()