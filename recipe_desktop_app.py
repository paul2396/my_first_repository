#!/usr/bin/env python3
"""
Desktop Recipe Generator App
A GUI version of the recipe suggestion system using tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

# Import the recipe database from the existing module
# Expanded recipe database (same as in recipe generator.py)
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


class RecipeDesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Generator - Desktop App")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🍳 Recipe Generator", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Ingredient input section
        ttk.Label(main_frame, text="Enter Ingredients:", 
                 font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        self.ingredient_entry = ttk.Entry(main_frame, font=('Arial', 10), width=40)
        self.ingredient_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 5))
        self.ingredient_entry.bind('<Return>', lambda e: self.get_recipe_suggestion())
        
        # Help text
        help_label = ttk.Label(main_frame, 
                              text="Enter ingredients separated by commas (e.g., potato, egg, cheese)",
                              font=('Arial', 8), foreground='gray')
        help_label.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        # Get Recipe button
        self.recipe_btn = ttk.Button(button_frame, text="🔍 Get Recipe Suggestion", 
                                    command=self.get_recipe_suggestion)
        self.recipe_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Show ingredients button
        ingredients_btn = ttk.Button(button_frame, text="📋 Show Available Ingredients", 
                                   command=self.show_available_ingredients)
        ingredients_btn.pack(side=tk.LEFT, padx=5)
        
        # Show recipes for ingredient button
        recipes_btn = ttk.Button(button_frame, text="📖 Browse Recipes", 
                               command=self.browse_recipes)
        recipes_btn.pack(side=tk.LEFT, padx=5)
        
        # Results section
        ttk.Label(main_frame, text="Recipe Suggestion:", 
                 font=('Arial', 10, 'bold')).grid(row=5, column=0, sticky=tk.W, pady=(20, 5))
        
        # Result text area with scrolling
        self.result_text = scrolledtext.ScrolledText(main_frame, height=15, width=70, 
                                                    font=('Arial', 10), wrap=tk.WORD)
        self.result_text.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), 
                             pady=(0, 10))
        
        # Configure grid weights for resizing
        main_frame.rowconfigure(6, weight=1)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter ingredients to get recipe suggestions!")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              font=('Arial', 9), foreground='blue')
        status_bar.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Set initial focus
        self.ingredient_entry.focus()
    
    def get_recipe_suggestion(self):
        """Get a recipe suggestion based on entered ingredients."""
        ingredient_input = self.ingredient_entry.get().strip()
        
        if not ingredient_input:
            self.status_var.set("Please enter at least one ingredient.")
            messagebox.showwarning("Input Required", "Please enter ingredients to get a recipe suggestion.")
            return
        
        # Parse ingredients
        if ',' in ingredient_input:
            ingredients = ingredient_input.split(',')
        else:
            ingredients = ingredient_input.split()
        
        # Clean ingredients
        ingredients = [ing.strip() for ing in ingredients if ing.strip()]
        
        # Get recipe suggestion
        suggestion = find_recipe(ingredients)
        
        # Display result
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"🍽️ Recipe Suggestion:\n\n{suggestion}\n\n")
        
        # Show matched ingredients if any
        matched = []
        for ingredient in ingredients:
            if ingredient.lower() in recipes:
                matched.append(ingredient.capitalize())
        
        if matched:
            self.result_text.insert(tk.END, f"✅ Matched ingredients: {', '.join(matched)}\n")
        
        self.status_var.set(f"Recipe suggestion generated for: {', '.join(ingredients)}")
    
    def show_available_ingredients(self):
        """Show all available ingredients."""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "🥗 Available Ingredients:\n\n")
        
        for ingredient in sorted(recipes.keys()):
            recipe_count = len(recipes[ingredient])
            self.result_text.insert(tk.END, f"• {ingredient.capitalize()} ({recipe_count} recipes)\n")
        
        self.result_text.insert(tk.END, f"\n📊 Total: {len(recipes)} ingredients available")
        self.status_var.set("Showing all available ingredients")
    
    def browse_recipes(self):
        """Open a dialog to browse recipes for a specific ingredient."""
        # Create a new window for ingredient selection
        browse_window = tk.Toplevel(self.root)
        browse_window.title("Browse Recipes by Ingredient")
        browse_window.geometry("400x300")
        browse_window.transient(self.root)
        browse_window.grab_set()
        
        # Center the window
        browse_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 100, 
                                          self.root.winfo_rooty() + 100))
        
        main_frame = ttk.Frame(browse_window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Select an ingredient to view recipes:",
                 font=('Arial', 10, 'bold')).pack(pady=(0, 10))
        
        # Listbox with ingredients
        listbox_frame = ttk.Frame(main_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        ingredient_listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set,
                                       font=('Arial', 10))
        ingredient_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=ingredient_listbox.yview)
        
        # Populate listbox
        for ingredient in sorted(recipes.keys()):
            ingredient_listbox.insert(tk.END, ingredient.capitalize())
        
        def show_recipes_for_selected():
            selection = ingredient_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select an ingredient first.")
                return
            
            selected_ingredient = ingredient_listbox.get(selection[0]).lower()
            
            # Show recipes in main window
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"🍳 Recipes using {selected_ingredient.capitalize()}:\n\n")
            
            for i, recipe in enumerate(recipes[selected_ingredient], 1):
                self.result_text.insert(tk.END, f"{i}. {recipe}\n")
            
            self.status_var.set(f"Showing {len(recipes[selected_ingredient])} recipes for {selected_ingredient}")
            browse_window.destroy()
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=(10, 0))
        
        ttk.Button(button_frame, text="Show Recipes", 
                  command=show_recipes_for_selected).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(button_frame, text="Cancel", 
                  command=browse_window.destroy).pack(side=tk.LEFT)
        
        # Double-click to show recipes
        ingredient_listbox.bind('<Double-1>', lambda e: show_recipes_for_selected())


def main():
    """Main function to run the desktop app."""
    root = tk.Tk()
    app = RecipeDesktopApp(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication closed by user.")


if __name__ == "__main__":
    main()