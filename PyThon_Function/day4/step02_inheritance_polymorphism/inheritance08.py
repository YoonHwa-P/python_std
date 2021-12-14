# /c/ProgramData/Anaconda3/python
# -*- conding: utf-8 -*-

class Player:
    MAX_POSITION = 10
    MAX_SPEED = 3

    def __init__(self):
        self.position = 0

    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION

    def draw(self):
        drawing = "-" * self.position + "|" +"-" * (Player.MAX_POSITION - self.position)
        print(drawing)

class Racer(Player):
    MAX_SPEED = 5

# Player and Racer 객체 생성
if __name__ == "__main__":
    p = Player()
    r = Racer()

    print("p.MAX_SPEED = ", p.MAX_SPEED)
    print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

