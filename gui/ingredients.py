import tkinter as tk


class IngredientsGui(tk.Frame):
    def __init__(self, parent: "tk.Frame", controller):
        from data.recommender_system import RecipeRecommender
        from data.constants import RECIPES, RULES

        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f5f5f5")
        self.recommender = RecipeRecommender(RECIPES, RULES)

        label = tk.Label(
            self,
            text="Recipe Recommendation by Ingredients",
            font=("Segoe UI", 18, "bold"),
            bg="#f5f5f5",
            fg="#333333",
        )
        label.pack(pady=40)

        self.__render_ingredients_input()

        self.__render_action_btns()

    def __render_action_btns(self):
        from gui.main_screen import MainMenuScreen

        button_frame = tk.Frame(self, bg="#f5f5f5")
        button_frame.pack(pady=(20, 30))

        back_button = tk.Button(
            button_frame,
            text="Back",
            font=("Segoe UI", 12),
            command=lambda: self.controller.show_frame(MainMenuScreen),
            bg="#e1e1e1",
            fg="black",
            padx=15,
            pady=8,
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
        )
        back_button.pack(side=tk.LEFT)

        submit_button = tk.Button(
            button_frame,
            text="Submit",
            font=("Segoe UI", 12),
            command=self.submit_form,
            bg="#3498db",
            fg="white",
            activeforeground="white",
            activebackground="#2980b9",
            padx=15,
            pady=8,
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
        )
        submit_button.pack(side=tk.LEFT, padx=(20, 0))

    def __render_ingredients_input(self):
        input_label = tk.Label(self, text="Enter ingredients you have: ", bg="#f5f5f5")
        input_label.pack(pady=(10, 0))
        self.ingredients_entry = tk.Entry(
            self, width=52, justify="left", font=("Segoe UI", 11)
        )
        self.ingredients_entry.pack(pady=(10, 5), ipady=7)
        description_label = tk.Label(
            self,
            text="Ex: tomato, onion, eggs",
            bg="#f5f5f5",
            fg="#4a4a4a",
            font=("Segoe UI", 10),
        )
        description_label.pack(pady=(0, 0))

    def submit_form(self):
        from gui.results import ResultsScreen

        inp_value = self.ingredients_entry.get()
        ingredients = [ing.lower().strip() for ing in inp_value.split(",")]

        results = self.recommender.recommend_by_ingredients(ingredients)
        results_instance = self.controller.frames[ResultsScreen]

        self.controller.show_frame(ResultsScreen)
        results_instance.set_results(results, "ingredients")
