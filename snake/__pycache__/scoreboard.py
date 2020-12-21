from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 24
FONT = "Arial"
WEIGHT = "bold"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_board()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Your Score was: {self.score}", align=ALIGNMENT, font=(FONT,FONT_SIZE,WEIGHT))
    
    def update_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT,FONT_SIZE,WEIGHT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_board()