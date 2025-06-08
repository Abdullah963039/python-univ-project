import tkinter as tk
from tkinter import ttk


class RecipeGui(tk.Frame):
    def __init__(self, parent: "tk.Frame", controller):
        from data.recommender_system import RecipeRecommender
        from data.constants import RECIPES, RULES

        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f5f5f5")
        self.recommender = RecipeRecommender(RECIPES, RULES)

        # Title label
        label = tk.Label(
            self,
            text="Recipe Recommendation Form",
            font=("Segoe UI", 18, "bold"),
            bg="#f5f5f5",
            fg="#333333",
        )
        label.pack(pady=20)

        self.init_form()

        self.__render_action_btns()

    def init_form(self):
        self.__prefered_cuisines_ui()

        # Maximum cooking time
        self.cook_time_entry = self.__create_input("Maximum cooking time in minutes:")

        # Dietary preferences
        self.__dietary_ui()
        # Minimum protein content
        self.min_protein_entry = self.__create_input("Minimum protein content (grams):")
        # Maximum calories
        self.max_calories_entry = self.__create_input("Maximum calories:")

    def __prefered_cuisines_ui(self):
        from data.constants import CUISINES

        tk.Label(
            self, text="Preferred Cuisine:", bg="#f5f5f5", font=("Segoe UI", 12)
        ).pack(pady=(10, 0))

        # Create a StringVar to store the selected cuisine
        self.selected_cuisine = tk.StringVar()
        self.selected_cuisine.set("Select a cuisine")  # default value

        # Create the combobox
        self.cuisine_combobox = ttk.Combobox(
            self,
            textvariable=self.selected_cuisine,
            values=CUISINES,
            state="readonly",  # makes it non-editable
            font=("Segoe UI", 11),
            width=43,
            justify="center",
        )
        self.cuisine_combobox.pack(pady=(0, 20), ipady=7)

    def __dietary_ui(self):
        from data.constants import DIETARY_TAGS
        

        tk.Label(
            self, text="Dietary preferences", bg="#f5f5f5", font=("Segoe UI", 12)
        ).pack(pady=(10, 0))

        # Create a StringVar to store the selected cuisine
        self.selected_diet = tk.StringVar()
        self.selected_diet.set("Select a dietary")

        # Create the combobox
        self.diet_combobox = ttk.Combobox(
            self,
            textvariable=self.selected_diet,
            values=DIETARY_TAGS,
            state="readonly",  # makes it non-editable
            font=("Segoe UI", 11),
            width=43,
            justify="center",
        )
        self.diet_combobox.pack(pady=(0, 20), ipady=7)

    def __validate_form(self):
        """Validate form inputs and show warning messages for invalid entries"""
        warnings = []

        # Validate cuisine selection
        selected_cuisine = self.selected_cuisine.get()
        if selected_cuisine == "Select a cuisine" or not selected_cuisine:
            warnings.append("Please select a preferred cuisine")

        # Validate cooking time
        max_cooking_time = self.cook_time_entry.get()
        try:
            cooking_time = int(max_cooking_time)
            if cooking_time <= 0 or cooking_time > (60 * 24):
                warnings.append(
                    "Cooking time must be between 1 and 1440 minutes (24 hours)"
                )
        except ValueError:
            warnings.append("Please enter a valid number for cooking time")

        # Validate dietary preferences
        dietary_preferences = self.selected_diet.get()
        if not dietary_preferences.strip():
            warnings.append("Please enter at least one dietary preference")

        # Validate protein content
        min_protein_content = self.min_protein_entry.get()
        try:
            protein = int(min_protein_content)
            if protein <= 0 or protein >= 500:
                warnings.append("Protein content must be between 1 and 499 grams")
        except ValueError:
            warnings.append("Please enter a valid number for protein content")

        # Validate calories
        max_calories = self.max_calories_entry.get()
        try:
            calories = int(max_calories)
            if calories <= 1 or calories > 2000:
                warnings.append("Calories must be between 1 and 2000")
        except ValueError:
            warnings.append("Please enter a valid number for maximum calories")

        # Show warnings if any exist
        if warnings:
            self.__show_warnings(warnings)
            return False

        return True

    def __show_warnings(self, warnings):
        warning_window = tk.Toplevel(self)
        warning_window.title("Invalid Credientials")
        warning_window.geometry("400x300")
        warning_window.resizable(False, False)
        warning_window.configure(bg="#f5f5f5")

        # Warning icon
        warning_icon = tk.Label(
            warning_window, text="⚠️", font=("Segoe UI", 24), bg="#f5f5f5"
        )
        warning_icon.pack(pady=(10, 5))

        # Title
        title = tk.Label(
            warning_window,
            text="Please fix the following issues:",
            font=("Segoe UI", 12, "bold"),
            bg="#f5f5f5",
            fg="#333333",
        )
        title.pack(pady=(0, 10))

        # Warning messages
        for warning in warnings:
            message = tk.Label(
                warning_window,
                text=f"• {warning}",
                font=("Segoe UI", 10),
                bg="#f5f5f5",
                fg="#e74c3c",
                anchor="w",
                justify="left",
            )
            message.pack(fill="x", padx=20, pady=2)

        # OK button
        ok_button = tk.Button(
            warning_window,
            text="OK",
            command=warning_window.destroy,
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            relief=tk.FLAT,
            padx=15,
        )
        ok_button.pack(pady=15)

    def __create_input(self, label: "str"):
        tk_label = tk.Label(self, text=label, bg="#f5f5f5")
        tk_label.pack(pady=(10, 0))
        entry = tk.Entry(self, width=52, justify="center", font=("Segoe UI", 10))
        entry.pack(pady=(0, 10), ipady=7)

        return entry

    def __render_action_btns(self):
        from gui.main_screen import MainMenuScreen

        button_frame = tk.Frame(self, bg="#f5f5f5")
        button_frame.pack(pady=(20, 30))

        # Back button
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

        # Submit button
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
            pady=8,  # Increased padding for better proportions
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
        )
        submit_button.pack(side=tk.LEFT, padx=(20, 0))  # Right margin between buttons

    def submit_form(self):
        """Handle form submission with validation"""

        if not self.__validate_form():
            return  # Don't proceed if validation fails

        # Retrieve valid user input
        preferences = {
            "cuisine": self.selected_cuisine.get().lower().strip(),
            "diet_tag": self.selected_diet.get().lower().strip(),
            "max_cook_time": int(self.cook_time_entry.get()),
            "min_protein": int(self.min_protein_entry.get()),
            "max_calories": int(self.max_calories_entry.get()),
        }

        recommender = self.recommender
        results = recommender.recommend(preferences)

        print(f"{results = }")
