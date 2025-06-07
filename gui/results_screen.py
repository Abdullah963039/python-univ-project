import tkinter as tk
from tkinter import ttk
from typing import List


class ResultsScreen(tk.Frame):
    def __init__(self, parent: "tk.Frame", controller, recipes: List[dict] = []):
        super().__init__(parent)
        self.controller = controller
        self.recipes = recipes
        self.configure(bg="#f5f5f5")

        # Create a scrollable frame
        self.scrollable_frame = ttk.Frame(self)
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scrollable_frame)
        self.scrollbar = ttk.Scrollbar(
            self.scrollable_frame, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_content = ttk.Frame(self.canvas)

        self.scrollable_content.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_content, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Display the recipes
        self.display_recipes()

    def display_recipes(self):
        from gui.main_screen import MainMenuScreen

        if len(self.recipes) == 0:
            return None

        for recipe in self.recipes:
            tk.Label(
                self.scrollable_content,
                text=f"Name: {recipe['name']}",
                font=("Segoe UI", 18, "bold"),
                bg="#f5f5f5",
            ).pack(pady=10)
            tk.Label(
                self.scrollable_content,
                text=f"Cuisine: {recipe['cuisine']}",
                font=("Segoe UI", 14),
                bg="#f5f5f5",
            ).pack(pady=5)
            tk.Label(
                self.scrollable_content,
                text=f"Ingredients: {', '.join(recipe['ingredients'])}",
                font=("Segoe UI", 14),
                bg="#f5f5f5",
            ).pack(pady=5)
            tk.Label(
                self.scrollable_content,
                text=f"Diet Tags: {', '.join(recipe['diet_tags'])}",
                font=("Segoe UI", 14),
                bg="#f5f5f5",
            ).pack(pady=5)
            tk.Label(
                self.scrollable_content,
                text=f"Cook Time: {recipe['cook_time']} minutes",
                font=("Segoe UI", 14),
                bg="#f5f5f5",
            ).pack(pady=5)
            tk.Label(
                self.scrollable_content,
                text=f"Nutrition: {recipe['nutrition']}",
                font=("Segoe UI", 14),
                bg="#f5f5f5",
            ).pack(pady=5)
            tk.Label(
                self.scrollable_content,
                text="-----------------------------------",
                bg="#f5f5f5",
            ).pack(pady=5)

        # Back button to return to the main menu
        back_button = tk.Button(
            self.scrollable_content,
            text="Back to Main Menu",
            command=lambda: self.controller.show_frame(MainMenuScreen),
            bg="#7f8c8d",
            fg="white",
            padx=15,
            pady=5,
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
        )
        back_button.pack(pady=20)
