import new_file as nf
def is_string(value):
    """Determines if the given value is a string that is not purely
    numeric."""
    # Check if the value is not empty and contains non-numeric
    # characters.
    return not value.isdigit() and len(value) > 0

name = input("What is your name? ")

while not is_string(name):
    name = input("What is your name? ")

    if is_string(name):
        print(f"Hello, {name}!")

nf.greet()