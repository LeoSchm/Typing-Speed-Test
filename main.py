from tkinter import *
text = "Na aber hallo wie geht es dir denn heuteaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
a = text

root = Tk()
root.title('Type Speed Test')
root.geometry('1000x700')
xpos = 1000/2.5

label = Label(root, text=text, font=("Cascadia Mono SemiLight", 30))
label.place(x=xpos, rely=0.35)  # Initial position

def on_key_press(event):
    global xpos
    global a
    print(a[0])
    if event.char == a[0]:
        xpos = xpos - (30*17/22)
        a = a[1:]
    label.place(x=xpos)
    print(event.keysym)

root.bind("<KeyPress>", on_key_press)

root.mainloop()
