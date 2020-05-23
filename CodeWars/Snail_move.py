class snail_move:
    """docstring for snail_move"""
    def __init__(self, A: list):
        super(snail_move, self).__init__()
        self.x = 0
        self.y = 0
        self.A = A
        self.Final = []


    def move_right(self):
        i = row = self.x
        if i != 0:
            i += 1
        while i < len(self.A) - self.x:
            self.Final.append(self.A[self.y][i])
            i += 1
        self.x = i - 1


    def move_down(self):
        j = line = self.y + 1
        while j < len(self.A) - self.y:
            self.Final.append(self.A[j][self.x])
            j += 1
        self.y = j - 1

    def move_left(self):
        k = row = self.x - 1
        while k >= len(self.A) - (self.x + 1):
            self.Final.append(self.A[self.y][k])
            k -= 1
        self.x = k + 1


    def move_up(self):
        m = line = self.y - 1
        while m >= len(self.A) - self.y :
            self.Final.append(self.A[m][self.x])
            m -= 1
        self.y = m + 1

    def switch(self):
        if len(self.A) > self.y:
            self.x += 1




    def Final(self, A):
        A = self.A

        pass

def snail(A):
    if A == [[]]:
        return []
    S = snail_move(A)
    for i in range(len(A)):
        
        S.move_right()
        S.move_down()
        S.move_left()
        S.move_up()
        S.switch()

    return S.Final

B =[[ 1, 2, 3, 4],\
    [12,13,15, 5],\
    [11,17,16, 6],\
    [10, 9, 8, 7]]
print(snail(B))


