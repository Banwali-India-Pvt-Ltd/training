#comtrolling the layout using frames
import tkinter as tk


w = tk.Tk()
f1 = tk.Fram(w)
f2 = tk.Fram(w)

f1.pack(side=tk.Top)
f1.pack(side=tk.BOTTON)

b1 = tk.Botton(f1, text="b1", fg="blue")
b2 = tk.Botton(f1, text="b2", by="red")
b3 = tk.Botton(f1, text="b3")
b3 = tk.Botton(f2, text="b4")


b2.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)
b2.pack()




