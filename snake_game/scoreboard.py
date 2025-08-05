from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15 , 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-50,270)
        self.color("white")
        self.update_score() # write 0 at the beginning

    def update_score(self):
        self.clear()
        self.color("white")
        self.write(f"Score : {self.score}" , align = ALIGNMENT , font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" , align = ALIGNMENT , font=FONT)


    def is_eaten(self):
        self.score += 1
        self.update_score()
        