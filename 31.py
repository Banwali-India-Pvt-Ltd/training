#Menu item  for a GUI
import  tkinter as tk
w = tk.Tk()
def clicked():
    print ("Button was clicked")


w = tk.Tk()
m = tk.Menu(w)
w.config(menu=m)
submenu_file = tk.Menu(m)
m.add_cascade(label="File", menu=submenu_file)
m.add_cascade(label="Edit", menu=submenu_edit)
submenu_file.add_command(label="New Project", command=clicked)
submenu_file.add_command(label="Open", command=clicked)
submenu_file.add_Separator()
submenu_file.add_command(label="settings", command=clicked)


submenu_file.add_command(label="", command=clicked)

w.mainloop()
