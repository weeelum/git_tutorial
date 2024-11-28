def is_string(value):
    """Determines if the given value is a string that is not purely
    numeric."""
    # Check if the value is not empty and contains non-numeric
    # characters.
    return not value.isdigit() and len(value) > 0

def question():
    name = input("What is your name? ")
    return name

while not is_string(question()):
    name = question()

    if is_string(name):
        print(f"Hello, {name}!")