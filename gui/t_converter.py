from tkinter import *

class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        Label(frame, text="deg C").grid(row=0, column=0)
        Button(frame, text="변환").grid(row=1, columnspan=2)

    def convert(self):
        c = self.c.get()
        con_f = "{0:  .2f}F".format(self.con.convert(c))
        self.f.set(con_f)

root = Tk()
root.title("Temp Converter")
root.geometry("250x60+200+200")
app = App(root)

root.mainloop()
