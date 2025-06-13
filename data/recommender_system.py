from data.inference_engine import InferenceEngine


class RecipeRecommender:
    def __init__(self, recipes, rules):
        self.inference_engine = InferenceEngine(recipes, rules)

    def recommend(self, preferences):
        return self.inference_engine.infer(preferences)
