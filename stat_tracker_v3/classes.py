import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        # main setup
        super().__init__()
        self.title(title)
        # size variable should be a touple for ease
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        
        # widgets
        self.menu = Menu(self)
        
        # run 
        self.mainloop()
        
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background = 'black').pack(expand = True, fill = 'both')
        self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
        
        self.create_widgets()
    
    def create_widgets(self):
        menu_button1 = ttk.Button(self, text = 'Button 1')
        menu_button2 = ttk.Button(self, text = 'Button 2')
        menu_button3 = ttk.Button(self, text = 'Button 3')

        menu_slider1 = ttk.Scale(self, orient='vertical')
        menu_slider2 = ttk.Scale(self, orient='vertical')

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'check 2')
        
        entry = ttk.Entry(self)
        
App('D&D Tool', (600, 600))