import tkinter as tk
import winsound
import random  # Voor willekeurige positie van de bal
print("Process has started")
print("Alpha V1.01")
class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pong")

        self.canvas = tk.Canvas(master, width=1000, height=400, bg="black")
        self.canvas.pack()

        # Paddle
        self.paddle = self.canvas.create_rectangle(250, 380, 350, 390, fill="red")

        # Bal maken op willekeurige positie
        self.create_ball()

        # Snelheid en score
        self.ball_dx = 4
        self.ball_dy = -4
        self.score = 0
        self.highscore = 0
        self.game_over = False

        # Teksten
        self.score_text = self.canvas.create_text(130, 20, text="Score: 00000000", fill="white", font=("Doto ExtraBold", 16))
        self.ball_dx_text = self.canvas.create_text(520, 20, text="Speed: 4", fill="white", font=("Doto ExtraBold", 16))
        self.highscore_text = self.canvas.create_text(870, 20, text="Highscore: 0", fill="white", font=("Doto ExtraBold", 16))

        # Besturing
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Button-1>", self.on_click)  # Klik om te herstarten

        self.game_loop()

    def create_ball(self):
        # Willekeurige X-positie
        x = random.randint(50, 950)
        self.ball = self.canvas.create_oval(x - 10, 190, x + 10, 210, fill="white")

    def move_left(self, event):
        x1, _, x2, _ = self.canvas.coords(self.paddle)
        if x1 > 0:
            self.canvas.move(self.paddle, -30, 0)

    def move_right(self, event):
        x1, _, x2, _ = self.canvas.coords(self.paddle)
        if x2 < 1000:
            self.canvas.move(self.paddle, 30, 0)


    def game_loop(self):
        if self.game_over:
            return

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        # Botsing met zijkanten
        if ball_coords[0] <= 0 or ball_coords[2] >= 1000:
            self.ball_dx = -self.ball_dx
            winsound.PlaySound("download.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            

        # Botsing met bovenkant
        if ball_coords[1] <= 0:
            self.ball_dy = -self.ball_dy
            winsound.PlaySound("download.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            

        # Botsing met paddle
        if (ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]) and \
           (ball_coords[3] >= paddle_coords[1]) and (self.ball_dy > 0):
            self.ball_dy = -self.ball_dy
            self.ball_dy -= 0.2
            self.ball_dx += 0.2
            self.score += 100
            winsound.PlaySound("download.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score:09}")
            self.canvas.itemconfig(self.ball_dx_text, text=f"Speed: {round(abs(self.ball_dy), 1)}")

        # Game over
        if ball_coords[3] >= 400:
            self.game_over = True
            if self.score > self.highscore:
                self.highscore = self.score
                self.canvas.itemconfig(self.highscore_text, text=f"Highscore: {self.highscore:09}")
            winsound.PlaySound("mariogameover1.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.canvas.create_text(500, 200, text="Game Over", font=("Matrix Mono", 24), fill="white")
            return

        self.master.after(20, self.game_loop)

    def on_click(self, event):
        if self.game_over:
            self.restart_game()

    def restart_game(self):
        self.canvas.delete("all")

        # Paddle en bal opnieuw tekenen
        self.paddle = self.canvas.create_rectangle(250, 380, 350, 390, fill="red")
        self.create_ball()

        # Reset score en snelheid
        self.ball_dx = 4
        self.ball_dy = -4
        self.score = 0
        self.game_over = False

        # Tekst opnieuw tekenen
        self.score_text = self.canvas.create_text(130, 20, text="Score: 000000000", fill="white", font=("Doto ExtraBold", 16))
        self.ball_dx_text = self.canvas.create_text(520, 20, text="Speed: 4", fill="white", font=("Doto ExtraBold", 16))
        self.highscore_text = self.canvas.create_text(820, 20, text=f"Highscore: {self.highscore:09}", fill="white", font=("Doto ExtraBold", 16))

        self.game_loop()

# Start het spel
root = tk.Tk()
game = PongGame(root)
root.mainloop()
