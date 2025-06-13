import tkinter as tk
from tkinter import ttk
from typing import List


class ResultsScreen(tk.Frame):
    def __init__(
        self,
        parent: "tk.Frame",
        controller,
    ):
        super().__init__(parent)
        self.controller = controller
        self.__results: List[dict] = []
        self.configure(bg="#f5f5f5")

        header_frame = tk.Frame(self, bg="#f5f5f5")
        header_frame.pack(fill=tk.X, pady=(10, 20), padx=20)

        tk.Label(
            header_frame,
            text="Recommendation Results",
            font=("Segoe UI", 20, "bold"),
            bg="#f5f5f5",
            fg="#333333",
        ).pack(side=tk.LEFT)

        from gui.main_screen import MainMenuScreen

        back_button = tk.Button(
            header_frame,
            text="← Back to Main Menu",
            command=lambda: self.controller.show_frame(MainMenuScreen),
            bg="#e74c3c",
            fg="white",
            font=("Segoe UI", 10),
            padx=15,
            pady=5,
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
            activebackground="#c0392b",
        )
        back_button.pack(side=tk.RIGHT)

        self.main_frame = tk.Frame(self, bg="#f5f5f5")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, bg="#f5f5f5", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(
            self.main_frame, orient="vertical", command=self.canvas.yview
        )

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollable_frame = tk.Frame(self.canvas, bg="#f5f5f5")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.empty_label = tk.Label(
            self.scrollable_frame,
            text="No results to display",
            font=("Segoe UI", 14),
            bg="#f5f5f5",
            fg="#7f8c8d",
            justify="center",
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.bind("<Configure>", lambda e: self._update_scrollregion())
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _update_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def display_recipes(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not self.__results:
            self.pack_empty_label()

            return

        self.empty_label.pack_forget()

        self.__display_by_recipe_results()

        self._update_scrollregion()

    def __display_by_recipe_results(self):
        inner_frame = tk.Frame(self.scrollable_frame, bg="#f5f5f5")
        inner_frame.pack(pady=20, fill="x")

        for recipe in self.__results:
            self.__create_recipe_card(inner_frame, recipe)

    def __create_recipe_card(self, parent, recipe):
        screen_width = self.winfo_screenwidth()
        card_width = int(screen_width * 0.8)

        card = tk.Frame(
            parent,
            bg="white",
            padx=15,
            pady=15,
            relief=tk.RAISED,
            borderwidth=1,
            highlightbackground="#e0e0e0",
            highlightthickness=1,
        )
        card.pack(side=tk.TOP, fill=tk.X, padx=(screen_width * 0.1), pady=10)
        card.pack_propagate(False)
        card.configure(width=card_width, height=250)

        name_label = tk.Label(
            card,
            text=recipe["name"],
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg="#2c3e50",
            wraplength=card_width - 30,
            justify="left",
        )
        name_label.pack(fill=tk.X, pady=(0, 5))

        details_frame = tk.Frame(card, bg="white")
        details_frame.pack(fill=tk.X, pady=5)

        self.__create_detail_row(
            details_frame, "Cuisine:", recipe["cuisine"].capitalize()
        )

        self.__create_detail_row(
            details_frame, "Cook Time:", f"{recipe['cook_time']} min"
        )

        self.__create_detail_row(details_frame, "Diet:", ", ".join(recipe["diet_tags"]))

        self.__create_detail_row(
            details_frame, "Ingredients:", ", ".join(recipe["ingredients"])
        )

        if "nutrition" in recipe:
            self.__create_detail_row(
                details_frame, "Protien:", f"{recipe['nutrition']['protein']}g"
            )
            self.__create_detail_row(
                details_frame, "Calories:", f"{recipe['nutrition']['calories']}kcal"
            )

    def __create_detail_row(self, parent, label, value):
        row = tk.Frame(parent, bg="white")
        row.pack(fill=tk.X)

        label_widget = tk.Label(
            row,
            text=label,
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#7f8c8d",
            width=18,
            anchor="w",
        )
        label_widget.pack(side=tk.LEFT)

        value_widget = tk.Label(
            row,
            text=value,
            font=("Segoe UI", 11),
            bg="white",
            fg="#34495e",
            anchor="w",
        )
        value_widget.pack(side=tk.LEFT)

    def set_results(self, results: List[dict]):
        self.__results = results
        self.display_recipes()

    def pack_empty_label(self):
        if not hasattr(self, 'empty_label') or not self.empty_label.winfo_exists():
            self.empty_label = tk.Label(
                self.scrollable_frame,
                text="No results to display",
                font=("Segoe UI", 14),
                bg="#f5f5f5",
                fg="#7f8c8d",
                justify="center",
            )
        self.empty_label.pack(pady=50, padx=80)

