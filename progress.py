import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    def progbar():
        prog = tk.Tk()
        prog.title("Progress")
        prog.resizable(False, False)
        prog.geometry("800x50")
        progress = ttk.Progressbar(prog, orient='horizontal', mode='indeterminate', length='750')
        text = tk.Text(width=11, height=1)
        text.insert(tk.INSERT, "Please wait")
        text.pack()
        progress.start()
        progress.pack()
        prog.mainloop()


    progbar()
