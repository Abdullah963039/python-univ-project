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

    def recommend_by_ingredients(self, available_ingredients):

        results = self.inference_engine.infer_by_ingredients(available_ingredients)

        return [
            {
                "recipe": result["recipe"],
                "missing_ingredients": result["missing_ingredients"],
                "excess_ingredients": result["excess_ingredients"],
            }
            for result in results
        ]
