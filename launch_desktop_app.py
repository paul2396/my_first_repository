#!/usr/bin/env python3
"""
Recipe Generator Desktop App Launcher
Simple launcher for the desktop version of the recipe generator
"""

import subprocess
import sys
import os

def main():
    """Launch the desktop recipe app"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_script = os.path.join(script_dir, 'recipe_desktop_app.py')
    
    print("🍳 Launching Recipe Generator Desktop App...")
    print("   Close the window or press Ctrl+C to exit.")
    
    try:
        subprocess.run([sys.executable, app_script])
    except KeyboardInterrupt:
        print("\n👋 Desktop app closed by user.")
    except FileNotFoundError:
        print("❌ Error: recipe_desktop_app.py not found!")
        print("   Make sure you're running this from the correct directory.")
    except Exception as e:
        print(f"❌ Error launching app: {e}")

if __name__ == "__main__":
    main()