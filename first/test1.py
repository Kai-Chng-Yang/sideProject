import test_ds
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self,text="AQI")
        topFrame.pack()

def main():
    window = Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()
    

if __name__ == "__main__":
    main()