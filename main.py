import datasource
import tkinter as tk
from tkinter import ttk

sbi_numbers = 3
bemp_numbers = 3

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # add menubar that contains a menu
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=30,pady=50)
        
        top_wrapperFrame = ttk.Frame(mainFrame)
        top_wrapperFrame.pack(fill=tk.X)

        topFrame = ttk.LabelFrame(top_wrapperFrame,text="台北市AQI")
        length = len(datasource.sarea_list)
        self.radioStringVar = tk.StringVar()
        for i in range(length):
            cols = i % 3
            rows = i // 3
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.radioStringVar,command=self.radio_Event).grid(column=cols,row=rows,sticky=tk.W,padx=10,pady=10)




def main():
    window = Window()
    window.title("AQI")
    window.mainloop()

if __name__ == "__main__":
    main()