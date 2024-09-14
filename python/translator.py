import sys

# Braille to English dictionary
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " ", ".O.OOO": "number follows", ".....O": "capital follows"
}

braille_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Expand English to Braille dictionary to include digits
english_to_braille = {v: k for k, v in braille_to_english.items()}
# Add missing digits to dictionary
english_to_braille.update({
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
})

def is_braille(s):
    # Determine if input is Braille based on the pattern (6 characters with . or O)
    return all(c in ".O" for c in s.replace(" ", "")) and len(s) % 6 == 0

def translate_braille_to_english(braille_string):
    braille_string = braille_string.replace(" ", "")  # Remove any spaces for easier processing
    result = []
    is_capital = False
    is_number = False
    
    # Handle Braille input in chunks of 6
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]
        
        if braille_char == ".O.OOO":  # number follows
            is_number = True
            continue
        elif braille_char == ".....O":  # capital follows
            is_capital = True
            continue
        elif braille_char == "......":  # space
            result.append(" ")
            is_number = False  # reset number mode after space
            continue
        
        # Translate the Braille character
        if is_number:
            translated_char = braille_numbers.get(braille_char, "")
        else:
            translated_char = braille_to_english.get(braille_char, "")
        
        if is_capital:
            result.append(translated_char.upper())
            is_capital = False
        else:
            result.append(translated_char)
        
        # Reset number mode if translated character is a space
        if translated_char == " ":
            is_number = False

    return "".join(result)

def translate_english_to_braille(english_string):
    result = []
    is_number = False
    
    for char in english_string:
        if char.isdigit():
            if not is_number:
                result.append(english_to_braille["number follows"])
                is_number = True
            result.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                result.append(english_to_braille["capital follows"])
            result.append(english_to_braille[char.lower()])
            is_number = False  # reset number mode after letters
        elif char == " ":
            result.append(english_to_braille[" "])
            is_number = False  # reset number mode after space

    return "".join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        sys.exit(1)
    
    input_string = " ".join(sys.argv[1:])
    
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()

