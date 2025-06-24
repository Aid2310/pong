import tkinter as tk

class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pong")

        self.canvas = tk.Canvas(master, width=1000, height=400, bg="black")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        self.paddle = self.canvas.create_rectangle(250, 380, 350, 390, fill="red")

        self.ball_dx = 4
        self.ball_dy = -4

        self.score = 0
        self.score_text = self.canvas.create_text(130, 20, text="Score: 00000000", fill="white", font=("Doto ExtraBold", 16))
        self.ball_dx_text = self.canvas.create_text(520, 20, text="Speed:4", fill="white", font=("Doto ExtraBold", 16))
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

        self.game_loop()

    def move_left(self, event):
        self.canvas.move(self.paddle, -30, 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 30, 0)

    def game_loop(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        # Botsing met muren
        if ball_coords[0] <= 0 or ball_coords[2] >= 1000:
            self.ball_dx = -self.ball_dx
        if ball_coords[1] <= 0:
            self.ball_dy = -self.ball_dy

        # Botsing met paddle
        if (ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]) and (ball_coords[3] >= paddle_coords[1]) and (self.ball_dy > 0):
            self.ball_dy = -self.ball_dy
            self.ball_dy -= 0.2
            self.ball_dx += 0.2
            self.score += 100
            self.canvas.itemconfig(self.score_text, text=f"Score: 000000{self.score}")
            self.canvas.itemconfig(self.ball_dx_text, text=f"Speed:{self.ball_dy}")

        # Game over
        if ball_coords[3] >= 400:
            self.canvas.create_text(500, 200, text="Game Over", font=("Doto ExtraBold", 48), fill="red")
            return

        self.master.after(20, self.game_loop)

root = tk.Tk()
game = PongGame(root)
root.mainloop()
