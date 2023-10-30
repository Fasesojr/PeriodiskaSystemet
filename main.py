import tkinter as tk

class PeriodicTableGUI(tk.Tk):


class MenuGUI(tk.Tk):
    """GUI class"""
    def __init__():
        super().__init__()

        #  Menu Lable
        self.MenuLabel = tk.Label(text = "- - - - - - Menu - - - - - -")
        self.MenuLabel.grid(row =0, column=0)

        #  Choice Number 1
        self.Choice1 = tk.Button(text="Show All Atoms",
                                 command = self.ShowAtoms)
        self.Choice1.grid(row=1, column=1)

        #  Choice Number 2
        self.Choice2 = tk.Button(text = "Excersice Atomic numbers",
                                 command = self.AtomNumbers)
        self.Choice2.grid(row=2, column =1)

        #  Choice Number 3
        





def main():
    """Main program"""

    
if name == "__main__":
    main()