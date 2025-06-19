import tkinter as tk
import random

doors = [0, 1, 2]

#functtion to simulate
def simulate():
    win_switch = 0
    win_stay = 0
    #reads(get()) the number inputted on the entry widget then converts it into int(just to be safe)
    games = int(times.get())
    #loop for n simulations
    for i in range(games):
        #"hides" the car in a random door
        car = random.choice(doors)
        #the player chooses a door
        guess = random.choice(doors)
        #the host will open the remaining door which, doesnt have the car and hasnt been picked by the player
        if guess != car:
            newdoors = doors.copy()
            newdoors.remove(car)
            newdoors.remove(guess)
            host = newdoors[0]
        #happens when player chose the correct door(they dont know), the host opens the whichever of the two
        elif guess == car:
            newdoors = doors.copy()
            newdoors.remove(car)
            host = random.choice(newdoors)
        #forces the change of door lol
        newguess = doors.copy()
        newguess.remove(host)
        newguess.remove(guess)
        final = newguess[0]
        #if the player won by switching 
        if final == car:
            win_switch += 1
        #if the player won by staying
        else:
            win_stay += 1
    #insert the results to the textbox 
    yourcar.delete("1.0",tk.END)
    yourcar.insert(tk.END, f"You simulated {games} games. Switching doors won {win_switch} out of {games} games. Winrate: {100 * (win_switch / games):.2f}%. Staying doors won {win_stay} games. Win rate: {100 * (win_stay / games):.2f}")
        


#overall widgets and UI
game = tk.Tk()
game.title("2 goats and 1 car")
game.geometry("300x400")
switch = tk.Button(game,width=30,text="Simulate Monty Hall N times", command=simulate)
switch.grid(row=1,column=0,pady=10)
times = tk.Entry(game,width=20)
times.grid(row=1,column=1, pady= 10)
yourcar = tk.Text(game,width=50, height=5)
yourcar.grid(row=2,column=0,columnspan=1, pady= 20,padx=20)

#keeps the window open i think
game.mainloop()