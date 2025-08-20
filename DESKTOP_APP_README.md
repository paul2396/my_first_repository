# Desktop Recipe Generator App

A user-friendly desktop application for generating recipe suggestions based on available ingredients.

## Features

🍳 **Recipe Suggestions**: Enter ingredients and get personalized recipe recommendations
📋 **Ingredient Browser**: View all available ingredients in the database  
📖 **Recipe Browser**: Browse recipes by specific ingredient
🖥️ **Desktop GUI**: Modern, easy-to-use graphical interface
⌨️ **Keyboard Shortcuts**: Press Enter in the ingredient field to get suggestions

## How to Use

### Method 1: Direct Launch
```bash
python3 recipe_desktop_app.py
```

### Method 2: Using the Launcher
```bash
python3 launch_desktop_app.py
```

## Application Interface

- **Ingredient Input**: Enter ingredients separated by commas (e.g., "potato, egg, cheese")
- **Get Recipe Suggestion**: Click to get a random recipe using your ingredients
- **Show Available Ingredients**: View all ingredients in the database
- **Browse Recipes**: Browse recipes organized by ingredient
- **Results Area**: Scrollable area showing recipe suggestions and information
- **Status Bar**: Helpful messages and current operation status

## Available Ingredients

The app includes recipes for:
- Potato (5 recipes)
- Egg (6 recipes) 
- Cheese (5 recipes)
- Chicken (5 recipes)
- Rice (4 recipes)
- Tomato (4 recipes)

## Examples

1. **Single ingredient**: Enter "potato" → Get recipes like "Mashed Potatoes" or "Baked Potato"
2. **Multiple ingredients**: Enter "egg, cheese" → Get recipes that use both ingredients
3. **Browse mode**: Click "Browse Recipes" to see all recipes for a specific ingredient

## Requirements

- Python 3.6+
- tkinter (usually included with Python)
- No additional dependencies required

## Testing

Run the comprehensive test suite:
```bash
python3 comprehensive_test.py
```

The app has been tested for:
- Recipe logic functionality
- GUI component behavior
- Error handling
- User input validation