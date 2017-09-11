#Binding funtion for actiuon
import tkinter as tk

w = tk.Tk()
def clicked(event):
    print ("Button was clicked")

b = tk.Button(w, text="click",)
b.bind("<Button-1>", clicked)

b.pack()
w.mainloop()