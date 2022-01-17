import tkinter as tk




def search(item):
  if item not in sample:
    return ("{} not in dictionary".format(item))
  else:
    return (sample[item])

 
root = tk.Tk()
 
w = tk.Label(root, text = search())
w.pack()
 
root.mainloop()


sample = {"property_1":"item_1"}

