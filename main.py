import tkinter as tk

class MainGUI(tk.Tk):
    """Main GUI for the application"""
    def __init__(self):
        super().__init__()

        #  Title
        self.TitleLabel = tk.Label(text = "- - - - - - Menu - - - - - -")
        self.TitleLabel.grid(row = 0, column = 1)

        #  Option 1
        self.Option1 = tk.Button(text = "1. Show the Periodic Table")
        self.Option1.grid(row = 1, column=1)

        #  Option 2 
        self.Option2 = tk.Button(text = "2. Excersize the Atomic Symbols")
        self.Option2.grid(row = 2, column = 1)

        #  Option 3
        self.Option3 = tk.Button(text = "3. Excersize the Atomic numbers")
        self.Option3.grid(row = 3, column = 1)

        #  Option 4
        self.Option4 = tk.Button(text = "4. Close the program")
        self.Option4.grid(row = 4, column = 1)

        

def main():
    """Main program"""
    window = MainGUI()
    window.mainloop()

if __name__ == "__main__":
    main()