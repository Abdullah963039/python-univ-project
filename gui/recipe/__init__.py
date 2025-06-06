import tkinter as tk



class RecipeGui(tk.Frame):
    def __init__(self, parent: "tk.Frame", controller):
        from gui.main_screen import MainMenuScreen
        
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f5f5f5")
        label = tk.Label(
            self,
            text="This is Screen Two",
            font=("Segoe UI", 18, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        )
        label.pack(pady=40)
        back_button = tk.Button(
            self,
            text="Back to Main Menu",
            font=("Segoe UI", 12),
            command=lambda: controller.show_frame(MainMenuScreen),
            bg="#7f8c8d",
            fg="white",
            activebackground="#606b6e",
            padx=15,
            pady=5,
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2"
        )
        back_button.pack()
    