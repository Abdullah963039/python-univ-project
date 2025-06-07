class InferenceEngine:
    def __init__(self, recipes, rules):
        self.recipes = recipes
        self.rules = rules

    def infer(self, preferences):
        scored_recipes = []

        for recipe in self.recipes:
            # Strict cuisine filter first
            if "cuisine" in preferences:
                if recipe["cuisine"] != preferences["cuisine"]:
                    # preferences["cuisine"] -> is Single value
                    continue  # Skip recipes not matching preferred cuisine

            score = 1.0
            reasons = []

            for rule in self.rules:
                if rule["condition"](preferences, recipe):
                    result = rule["action"](preferences, recipe)
                    score *= result["score_boost"]
                    reasons.append(result["reason"])

            # Apply other basic filters
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

            if "diet_tag" in preferences and (preferences["diet_tag"] not in recipe['diet_tags']):
                continue

            scored_recipes.append(
                {"recipe": recipe, "score": score, "reasons": reasons}
            )

        scored_recipes.sort(key=lambda x: x["score"], reverse=True)

        return scored_recipes
