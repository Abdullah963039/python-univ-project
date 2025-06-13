import tkinter as tk


class MainMenuScreen(tk.Frame):
    def __init__(self, parent: "tk.Frame", controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f5f5f5")

        self.render_link_btns(controller)

    def render_link_btns(self, controller):
        from gui.recipe import RecipeGui

        button_frame = tk.Frame(self, bg="#f5f5f5")
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

        recipe_btn = tk.Button(
            button_frame,
            text="Search by Recipe",
            font=("Segoe UI", 14),
            command=lambda: controller.show_frame(RecipeGui),
            bg="#3498db",
            fg="white",
            activeforeground="white",
            activebackground="#2980b9",
            padx=20,
            pady=10,
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
            width=35
        )
        recipe_btn.grid(row=0, column=0)
