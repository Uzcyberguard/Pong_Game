class Players_Moving:
    def __init__(self,player1,player2):
        self.p1 = player1
        self.p2 = player2
        self.p1.speed("fastest")
        self.p2.speed("fastest")
    def p_up(self):
        if self.p1.ycor()<=260:
            self.p1.sety(self.p1.ycor()+12)

            self.p2.sety(self.p2.ycor()+12)
    def p_down(self):
        if self.p1.ycor()>= -250:
            self.p1.sety(self.p1.ycor()-12)

            self.p2.sety(self.p2.ycor()-12)