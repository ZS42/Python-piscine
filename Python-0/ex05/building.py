import sys
import string
import unicodedata  # For normalization

def main():
    # your tests and your error handling
    # If there's more than one argument, raise an error
    if len(sys.argv) == 1:
        print("What is the text to count?")
        try:
            text = sys.stdin.readline()
        except EOFError:
            text = ""
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        text = sys.argv[1]
        # Check if the argument is a string
    if not isinstance(text, str):
        raise AssertionError("Argument must be a string")
    # Normalize to NFKD form, which decomposes characters into ASCII-friendly versions
    text = unicodedata.normalize("NFKD", text)

    upper = lower = digits = spaces = punctuation = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punctuation += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    
# Standard Python entry point
if __name__ == "__main__":
    main()

# expected output:
# $>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digits
# $>

# $>python building.py
# What is the text to count?
# Hello World!
# The text contains 13 characters:
# 2 upper letters
# 8 lower letters
# 1 punctuation marks
# 2 spaces
# 0 digits
# $>