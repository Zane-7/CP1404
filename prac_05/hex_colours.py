COLOUR_CODES = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}


colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").title()