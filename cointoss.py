import random
import tkinter as tk

board = tk.Tk()
board.geometry("300x400")
board.title("Coin Flip Simulator")

flips = 0
head = 0
tail = 0


def coin_flip():
    global flips, head, tail
    chance = ["heads", "tails"]
    res = random.choice(chance)
    result.delete(0, tk.END)
    result.insert(tk.END, res)
    flips += 1
    if res == "heads":
        head +=1
    elif res =="tails":
        tail += 1
    proba.delete(0,tk.END)
    proba.insert(tk.END, f"You filpped {flips} times")
  


def simulate():
    global flips, head, tail
    try:
        n = int(n_times.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        proba.delete(0,tk.END)
        n_times.delete(0,tk.END)
        proba.insert(tk.END, "Number too small or too big. Input a valid number")
        return
    
    for i in range(n):
        chance = ["heads", "tails"]
        res = random.choice(chance)
        result.delete(0, tk.END)
        flips += 1
        if res == "heads":
            head += 1
        elif res == "tails":
            tail += 1
    bias_head = 100 * (head / flips)
    bias_tail = 100 * (tail / flips)
    proba.delete(0,tk.END)
    if bias_head > bias_tail:
        proba.insert(tk.END, f"You simulated {n} flips. The coin shows bias towards heads with {bias_head:.2f}% probability while tails has {bias_tail:.2f}%")
    elif bias_tail > bias_head:
        proba.insert(tk.END, f"You simulated {n} flips. The coin shows bias towards tails with {bias_tail:.2f}% probability while heads has {bias_head:.2f}%")
    




result = tk.Entry(board, width=20, justify="center")
result.grid(row=2, column=1, columnspan=3, pady=20, padx=10)
proba = tk.Entry(board, width=100)
proba.grid(row=1, column=0, columnspan=3, pady=20)
flip = tk.Button(board, width=20, height=2, text="Flip the Coin", command=coin_flip)
flip.grid(row=2, column=0, padx=10)
press = tk.Button(board, width=20, height=2, text="Simulate N flips at once", command=simulate)
press.grid(row=3, column=0, padx=10)
n_times = tk.Entry(board, width=20, justify="center")
n_times.grid(row=3, column=1, columnspan=3, pady=20, padx=10)




board.mainloop()