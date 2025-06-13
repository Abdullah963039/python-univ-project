import tkinter as tk
from tkinter import ttk
from typing import List, Literal


test_ingre = [
    {
        "recipe": {
            "name": "Quiche Lorraine",
            "ingredients": [
                "pie crust",
                "eggs",
                "bacon",
                "heavy cream",
                "gruyere cheese",
            ],
            "cuisine": "french",
            "diet_tags": ["high-protein", "non-vegan"],
            "cook_time": 50,
            "nutrition": {"calories": 680, "protein": 25},
        },
        "missing_ingredients": ["bacon", "pie crust", "heavy cream", "gruyere cheese"],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Pad Thai",
            "ingredients": [
                "rice noodles",
                "chicken",
                "eggs",
                "bean sprouts",
                "peanuts",
                "tamarind sauce",
            ],
            "cuisine": "thai",
            "diet_tags": ["high-protein", "non-vegan"],
            "cook_time": 35,
            "nutrition": {"calories": 620, "protein": 38},
        },
        "missing_ingredients": [
            "tamarind sauce",
            "chicken",
            "rice noodles",
            "peanuts",
            "bean sprouts",
        ],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Egg Fried Rice",
            "ingredients": [
                "rice",
                "eggs",
                "peas",
                "carrots",
                "soy sauce",
                "sesame oil",
            ],
            "cuisine": "chinese",
            "diet_tags": ["vegetarian", "quick-meal", "non-vegan"],
            "cook_time": 20,
            "nutrition": {"calories": 380, "protein": 15},
        },
        "missing_ingredients": ["sesame oil", "rice", "carrots", "soy sauce", "peas"],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Scrambled Eggs",
            "ingredients": ["eggs", "butter", "milk", "salt", "pepper", "chives"],
            "cuisine": "american",
            "diet_tags": ["vegetarian", "non-vegan", "quick-meal"],
            "cook_time": 10,
            "nutrition": {"calories": 250, "protein": 18},
        },
        "missing_ingredients": ["butter", "pepper", "milk", "salt", "chives"],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Bibimbap",
            "ingredients": ["rice", "beef", "eggs", "spinach", "carrots", "gochujang"],
            "cuisine": "korean",
            "diet_tags": ["high-protein", "non-vegan"],
            "cook_time": 40,
            "nutrition": {"calories": 650, "protein": 35},
        },
        "missing_ingredients": ["spinach", "gochujang", "rice", "carrots", "beef"],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Cobb Salad",
            "ingredients": [
                "lettuce",
                "chicken",
                "bacon",
                "eggs",
                "avocado",
                "blue cheese",
            ],
            "cuisine": "american",
            "diet_tags": ["high-protein", "non-vegan"],
            "cook_time": 25,
            "nutrition": {"calories": 580, "protein": 42},
        },
        "missing_ingredients": [
            "bacon",
            "avocado",
            "lettuce",
            "chicken",
            "blue cheese",
        ],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Eggs Benedict",
            "ingredients": [
                "english muffins",
                "eggs",
                "canadian bacon",
                "hollandaise sauce",
                "butter",
            ],
            "cuisine": "american",
            "diet_tags": ["non-vegan"],
            "cook_time": 30,
            "nutrition": {"calories": 650, "protein": 28},
        },
        "missing_ingredients": [
            "hollandaise sauce",
            "english muffins",
            "butter",
            "canadian bacon",
        ],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Meatloaf",
            "ingredients": [
                "ground beef",
                "breadcrumbs",
                "eggs",
                "ketchup",
                "onion",
                "garlic",
            ],
            "cuisine": "american",
            "diet_tags": ["high-protein", "non-vegan"],
            "cook_time": 75,
            "nutrition": {"calories": 450, "protein": 35},
        },
        "missing_ingredients": [
            "ground beef",
            "garlic",
            "breadcrumbs",
            "onion",
            "ketchup",
        ],
        "excess_ingredients": [],
    },
    {
        "recipe": {
            "name": "Crab Cakes",
            "ingredients": [
                "crab meat",
                "breadcrumbs",
                "mayonnaise",
                "eggs",
                "mustard",
                "old bay seasoning",
            ],
            "cuisine": "american",
            "diet_tags": ["pescatarian", "non-vegan"],
            "cook_time": 30,
            "nutrition": {"calories": 380, "protein": 28},
        },
        "missing_ingredients": [
            "mustard",
            "crab meat",
            "breadcrumbs",
            "old bay seasoning",
            "mayonnaise",
        ],
        "excess_ingredients": [],
    },
]


class ResultsScreen(tk.Frame):
    def __init__(
        self,
        parent: "tk.Frame",
        controller,
    ):
        super().__init__(parent)
        self.controller = controller
        self.__results: List[dict] = []
        self.__results_type: Literal["recipe", "ingredients"] = "recipe"
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

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.bind("<Configure>", lambda e: self._update_scrollregion())
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.empty_label = tk.Label(
            self.scrollable_frame,
            text="No results to display",
            font=("Segoe UI", 14),
            bg="#f5f5f5",
            fg="#7f8c8d",
        )

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _update_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def display_recipes(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not self.__results:
            self.empty_label.pack(pady=50)
            return

        self.empty_label.pack_forget()

        if self.__results_type == "recipe":
            self.__display_by_recipe_results()
        else:
            self.__display_by_ingredients_results()

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

    def __display_by_ingredients_results(self):
        rows = []
        current_row = None

        for i, result in enumerate(self.__results):
            if i % 2 == 0:
                current_row = tk.Frame(self.scrollable_frame, bg="#f5f5f5")
                current_row.pack(fill=tk.X, padx=20, pady=10)
                rows.append(current_row)

            self.__create_ingredient_card(current_row, result)

    def __create_ingredient_card(self, parent, result):
        screen_width = self.winfo_screenwidth()
        card_width = int(screen_width * 0.8)

        recipe = result["recipe"]

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
        card.configure(width=card_width, height=280)

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

        if len(result["missing_ingredients"]) > 0:
            self.__create_detail_row(
                details_frame,
                "Missing Ingredients: ",
                ", ".join(result["missing_ingredients"]),
            )
        if len(result["excess_ingredients"]) > 0:
            self.__create_detail_row(
                details_frame,
                "Excess Ingredients: ",
                ", ".join(result["excess_ingredients"]),
            )

        if (
            len(result["missing_ingredients"]) == 0
            and len(result["excess_ingredients"]) == 0
        ):
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

    def set_results(
        self, results: List[dict], typ: Literal["recipe", "ingredients"] = "recipe"
    ):
        self.__results = results
        self.__results_type = typ
        self.display_recipes()
