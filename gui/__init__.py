import tkinter as tk
from tkinter import font


class RecipeRecommendationApp:
    def __init__(self, root: "tk.Tk"):
        from gui.recipe import RecipeGui
        from gui.ingredients import IngredientsGui
        from gui.main_screen import MainMenuScreen

        self.root = root
        self.init_app()

        # Add a welcome label
        self.show_welcome_message()

        # Container for all frames
        self.container = tk.Frame(self.root, bg="#c2c2c2")  # TODO reset background
        self.container.pack(fill="both", expand=True)
        # Configure grid weight to make container expandable
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Initialize frames dict
        self.frames = {}
        for F in (MainMenuScreen, RecipeGui, IngredientsGui):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenuScreen)

    def show_frame(self, screen_class: "tk.Frame"):
        frame: "tk.Frame" = self.frames[screen_class]
        frame.tkraise()

    def show_welcome_message(self):
        welcome_label = tk.Label(
            self.root,
            text="Welcome to Recipe Recommendation App",
            font=("Segoe UI", 24, "bold"),
            bg="#f5f5f5",
            fg="#333333",
            pady=20,
        )
        welcome_label.pack()

    def init_app(self):
        self.root.title("Recipe Recommendation")
        self.root.geometry("800x700")
        self.root.minsize(800, 700)
        self.root.configure(bg="#f5f5f5")

        # Set a modern font for the app
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="Segoe UI", size=12)
