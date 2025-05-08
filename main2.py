from tkinter import *
text = "ABCDEFGHijklmnopqrstuvwxyz1234567890ßöüä"
a = text

root = Tk()
root.title('Type Speed Test')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.state('zoomed')

xpos = 1000/2.5

label = Label(root, text=text, font=("Cascadia Mono SemiLight", 30))
def Start():
    Title = Label(root, text="Willkommen zu [name]!\nDrücke auf den Knopf zum Starten", font=("Cascadia Mono SemiLight", 30))
    StartKnopf = Button(root, text="Start!",font=("Cascadia Mono SemiLight", 30), width=10)
    Title.place(x=(screen_width/2-300), rely=0.35)
    StartKnopf.place(x=screen_width/2-150, rely=0.5)

Start()

# def on_key_press(event):
#     global xpos
#     global a
#     print(a[0])
#     if event.char == a[0]:
#         xpos = xpos - (30*17/22)
#         a = a[1:]
#     label.place(x=xpos)
#     print(event.keysym)

# root.bind("<KeyPress>", on_key_press)

root.mainloop()
