from tkinter import *
from tkinter import IntVar

# create tkinter window
root = Tk()
root.title("Select a Height")

# declare slide length
global maxheight
maxheight = 14


# connect to robot TODO add checks
def move(param):
    print(param)
    pass


# declare variable to hold input value init as 0
radiovalue = IntVar()
radiovalue.set(0)

# create radio options based on maxheight
for i in range(maxheight + 1):
    # make radio buttons and display with pack
    Radiobutton(root, font=8, text=str(i) + " ft", variable=radiovalue, value=i).pack()

# make button the sends value of radio to robo move function
Button(root, font=2, text="Move", command=lambda: move(radiovalue.get())).pack()

# necessary ignore
root.mainloop()
