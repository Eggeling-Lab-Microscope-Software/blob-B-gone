import tkinter as tk
from tkinter import filedialog, ttk


class pyDialogue():
    
    @staticmethod
    def askDIR():
        root = tk.Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        DIR_path = filedialog.askdirectory()
        return DIR_path

    @staticmethod
    def askDIRS():
        import tkfilebrowser
        
        root = tk.Tk()
        root.geometry('200x200')
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        dirs = []

        def get_directories():
            dirs.append(tkfilebrowser.askopendirnames())
            return dirs

        b1 = tk.Button(root, text='select directories...', command=get_directories)
        b1.pack()

        root.mainloop()

    @staticmethod
    def askFILE():
        root = tk.Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        FILE_path = filedialog.askopenfilename()
        return FILE_path

    @staticmethod
    def askFILES():
        root = tk.Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        FILE_path = filedialog.askopenfilenames()
        return FILE_path