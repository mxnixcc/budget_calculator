import tkinter as tk

window = tk.Tk()
window.title("Test")
window.geometry("300x200")

label = tk.Label(window, text="Tkinter works!")
label.pack(pady=50)

window.mainloop()