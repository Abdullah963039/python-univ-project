def get_user_preferences():
    preferences = {}

    cuisines = input("Preferred cuisines (comma separated - french, italian, etc.): ")
    if cuisines.strip():
        preferences["cuisine"] = [c.strip().lower() for c in cuisines.split(",")]

    max_time = input("Maximum cooking time in minutes: ")
    if max_time.strip():
        preferences["max_cook_time"] = int(max_time)

    diets = input("Dietary preferences (comma separated - vegetarian, high-protein, etc.): ")
    if diets.strip():
        preferences["diet_tags"] = [d.strip().lower() for d in diets.split(",")]

    min_protein = input("Minimum protein content (grams): ")
    if min_protein.strip():
        preferences["min_protein"] = int(min_protein)

    max_cals = input("Maximum calories: ")
    if max_cals.strip():
        preferences["max_calories"] = int(max_cals)

    return preferences

def display_recipe(recipe):
    print(f"\n{recipe['name'].upper()}")
    print(f"Cuisine: {recipe['cuisine'].title()}")
    print(f"Cook Time: {recipe['cook_time']} minutes")
    print(f"Diet Tags: {', '.join(recipe['diet_tags'])}")
    print(f"Nutrition: {recipe['nutrition']['calories']} calories, {recipe['nutrition']['protein']}g protein")
    print("\nIngredients:")
    for ing in recipe["ingredients"]:
        print(f"- {ing}")

def display_recommendations(results):
    print(f"\nFound {len(results)} matching recipes:")
    for i, result in enumerate(results, 1):
        recipe = result["recipe"]
        print(f"\n{i}. {recipe['name']} ({recipe['cuisine']}, {recipe['cook_time']} min)")
        print(f"   Match Score: {result['match_percent']:.1f}%")
        if "reasons" in result and result["reasons"]:
            print("   Reasons:")
            for reason in result["reasons"]:
                print(f"   - {reason}")
        if "missing_ingredients" in result and result["missing_ingredients"]:
            print(f"   Missing: {', '.join(result['missing_ingredients'])}")