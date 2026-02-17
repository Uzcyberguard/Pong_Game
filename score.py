class Score():
    def __init__(self,t):
        self.sc = t
    def write(self):
        self.sc.penup()
        self.sc.goto(-200,300)

        self.sc.write("❤️❤️❤️❤️❤️",align="center",font=("Arial",18,"bold"))
