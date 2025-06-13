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
