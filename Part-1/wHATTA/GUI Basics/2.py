import tkinter
window = tkinter.Tk()
window.title("2")
window.geometry('1920x1080')

l1 = tkinter.Label(window, text="Hello")
l1.grid(column=0, row=0)

txt = tkinter.Entry(window, width = 10)
txt.grid(column= 1, row= 0)

def clicked():
    res = "Welcome to " + txt.get()
    l1.configure(text = res)

window.mainloop()