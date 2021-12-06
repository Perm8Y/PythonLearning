import script
import tkinter as tk


def startGame():
    player1Card1["text"] = script.playerRe[0]
    player1Card2["text"] = script.playerRe[1]

def drawCard():
    player1Card3["text"] = script.playerDrawRe[2]

def judging():
    enemyCard1["text"] = script.enemyRe[0]
    enemyCard2["text"] = script.enemyRe[1]
    enemyCard3["text"] = script.enemyRe[2]

    judgement["text"] = script.winner

app = tk.Tk()
app.title("Card Game")

app.rowconfigure([0, 1, 2, 3], minsize=100, weight=1)
app.columnconfigure([0, 1, 2], minsize=100, weight=1)

player1Card1 = tk.Label(master=app, text="your card")
player1Card1.grid(row=0, column=0, sticky="nsew")
player1Card2 = tk.Label(master=app, text="your card")
player1Card2.grid(row=0, column=1, sticky="nsew")
player1Card3 = tk.Label(master=app, text="your card")
player1Card3.grid(row=0, column=2, sticky="nsew")

enemyCard1 = tk.Label(master=app, text="enemy card")
enemyCard1.grid(row=1, column=0, sticky="nsew")
enemyCard2 = tk.Label(master=app, text="enemy card")
enemyCard2.grid(row=1, column=1, sticky="nsew")
enemyCard3 = tk.Label(master=app, text="enemy card")
enemyCard3.grid(row=1, column=2, sticky="nsew")

judgement = tk.Label(master=app, text="-")
judgement.grid(row=2, column=1, sticky="nsew")

btnStart = tk.Button(master=app, text="Start", command=startGame)
btnStart.grid(row=3, column=0, sticky="nsew")

btnDraw = tk.Button(master=app, text="Draw", command=drawCard)
btnDraw.grid(row=3, column=1, sticky="nsew")

btnDone = tk.Button(master=app, text="Done", command=judging)
btnDone.grid(row=3, column=2, sticky="nsew")

app.mainloop()