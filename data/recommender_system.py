from data.inference_engine import InferenceEngine


class RecipeRecommender:
    def __init__(self, recipes, rules):
        self.inference_engine = InferenceEngine(recipes, rules)

    def recommend(self, preferences):
        results = self.inference_engine.infer(preferences)

        return [
            {
                "recipe": result["recipe"],
                "match_percent": result["score"] * 20,
                "reasons": result["reasons"],
            }
            for result in results
        ]

    def recommend_by_ingredients(self, available_ingredients, n=5):
        preferences = {"available_ingredients": available_ingredients}
        results = self.inference_engine.infer(preferences)
        return [
            {
                "recipe": result["recipe"],
                "match_percent": result["score"] * 20,
                "missing_ingredients": [
                    ing
                    for ing in result["recipe"]["ingredients"]
                    if ing not in available_ingredients
                ],
                "reasons": result["reasons"],
            }
            for result in results[:n]
        ]
