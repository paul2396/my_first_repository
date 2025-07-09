import random

# Expanded recipe database
recipes = {
    "potato": [
        "Mashed Potatoes", 
        "Fried Potatoes", 
        "Potato Salad",
        "Baked Potato",
        "Hash Browns"
    ],
    "egg": [
        "Scrambled Eggs",
        "Omelette", 
        "Egg Salad", 
        "Poached Eggs",
        "Fried Eggs",
        "Boiled Eggs"
    ],
    "cheese": [
        "Mac and Cheese", 
        "Grilled Cheese",
        "Cheese Sandwich",
        "Cheese Omelette",
        "Cheese Quesadilla"
    ],
    "chicken": [
        "Grilled Chicken",
        "Chicken Salad",
        "Chicken Soup",
        "Fried Chicken",
        "Chicken Stir Fry"
    ],
    "rice": [
        "Fried Rice",
        "Rice Pilaf",
        "Rice Bowl",
        "Rice Pudding"
    ],
    "tomato": [
        "Tomato Salad",
        "Tomato Soup",
        "Stuffed Tomatoes",
        "Tomato Pasta"
    ]
}

def find_recipe(ingredients):
    """
    Find recipes based on available ingredients.
    Returns a random recipe or appropriate message.
    """
    if not ingredients or all(not ingredient.strip() for ingredient in ingredients):
        return "Please enter at least one ingredient."
    
    available_recipes = []
    matched_ingredients = []
    
    for ingredient in ingredients:
        # Clean and normalize ingredient input
        ingredient = ingredient.strip().lower()
        
        if not ingredient:  # Skip empty ingredients
            continue
            
        if ingredient in recipes:
            available_recipes.extend(recipes[ingredient])
            matched_ingredients.append(ingredient.capitalize())
    
    if available_recipes:
        # Remove duplicates while preserving order
        unique_recipes = []
        for recipe in available_recipes:
            if recipe not in unique_recipes:
                unique_recipes.append(recipe)
        
        selected_recipe = random.choice(unique_recipes)
        matched_ingredients_str = ", ".join(matched_ingredients)
        return f"{selected_recipe} (using: {matched_ingredients_str})"
    else:
        return "No suitable recipe found for the ingredients. Try: potato, egg, cheese, chicken, rice, or tomato."

def show_available_ingredients():
    """Display all available ingredients."""
    print("\nAvailable ingredients:")
    for ingredient in sorted(recipes.keys()):
        print(f"- {ingredient.capitalize()}")

def show_recipes_for_ingredient(ingredient):
    """Show all recipes for a specific ingredient."""
    ingredient = ingredient.strip().lower()
    if ingredient in recipes:
        print(f"\nRecipes using {ingredient.capitalize()}:")
        for i, recipe in enumerate(recipes[ingredient], 1):
            print(f"{i}. {recipe}")
    else:
        print(f"No recipes found for '{ingredient}'.")

def main():
    """Main program loop with menu options."""
    print("=== Recipe Suggestion System ===")
    
    while True:
        print("\nOptions:")
        print("1. Get recipe suggestion")
        print("2. Show available ingredients")
        print("3. Show recipes for specific ingredient")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            user_input = input("\nEnter ingredients (separated by commas): ")
            
            # Handle different separator formats
            if ',' in user_input:
                user_ingredients = user_input.split(',')
            else:
                user_ingredients = user_input.split()
            
            result = find_recipe(user_ingredients)
            print(f"\nSuggested recipe: {result}")
            
        elif choice == "2":
            show_available_ingredients()
            
        elif choice == "3":
            ingredient = input("\nEnter ingredient name: ")
            show_recipes_for_ingredient(ingredient)
            
        elif choice == "4":
            print("Thanks for using Recipe Suggestion System!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Simple mode (original functionality)
def simple_mode():
    """Run the original simple version."""
    user_ingredients = input("Enter ingredients (separated by commas): ").split(",")
    user_ingredients = [ing.strip() for ing in user_ingredients]  # Clean whitespace
    print("Suggested recipe: " + find_recipe(user_ingredients))

if __name__ == "__main__":
    # Ask user which mode to run
    mode = input("Run in (1) Interactive mode or (2) Simple mode? Enter 1 or 2: ").strip()
    
if mode == "1":
    main()
else:
    simple_mode()
