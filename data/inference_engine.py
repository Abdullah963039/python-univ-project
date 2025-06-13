class InferenceEngine:
    def __init__(self, recipes, rules):
        self.recipes = recipes
        self.rules = rules

    def infer(self, preferences):
        scored_recipes = []

        for recipe in self.recipes:
            if "cuisine" in preferences:
                if recipe["cuisine"] != preferences["cuisine"]:
                    continue

            if (
                "max_cook_time" in preferences
                and recipe["cook_time"] > preferences["max_cook_time"]
            ):
                continue

            if (
                "min_protein" in preferences
                and recipe["nutrition"]["protein"] < preferences["min_protein"]
            ):
                continue

            if (
                "max_calories" in preferences
                and recipe["nutrition"]["calories"] > preferences["max_calories"]
            ):
                continue

            if "diet_tag" in preferences and (
                preferences["diet_tag"] not in recipe["diet_tags"]
            ):
                continue

            scored_recipes.append(recipe)

        return scored_recipes

    def infer_by_ingredients(self, inp_ingredients):
        matched_recipes = []

        input_ingredients = {
            ingredient.lower().strip() for ingredient in inp_ingredients
        }

        for recipe in self.recipes:
            recipe_ingredients = {
                ingredient.lower().strip() for ingredient in recipe["ingredients"]
            }

            if all(
                any(
                    inp in recipe_ingredient for recipe_ingredient in recipe_ingredients
                )
                for inp in input_ingredients
            ):
                excess_ingredients = [
                    ingredient
                    for ingredient in input_ingredients
                    if not any(
                        ingredient in recipe_ingredient
                        for recipe_ingredient in recipe_ingredients
                    )
                ]

                missing_ingredients = [
                    recipe_ingredient
                    for recipe_ingredient in recipe_ingredients
                    if not any(
                        recipe_ingredient in ingredient
                        for ingredient in input_ingredients
                    )
                ]

                matched_recipes.append(
                    {
                        "recipe": recipe,
                        "missing_ingredients": missing_ingredients,
                        "excess_ingredients": excess_ingredients,
                    }
                )

        return matched_recipes
