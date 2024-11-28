import new_file as nf

def is_string(value):
    """Determines if the given value is a string that is not purely
    numeric."""
    # Check if the value is not empty and contains non-numeric
    # characters.
    return not value.isdigit() and len(value) > 0

# def question():
#     name = input("What is your name? ")
#     return name

# while True:
#     name = input("What is your name? ")

#     while not is_string(name):
#         name = input("What is your name? ")

#         if is_string(name):
#             print(f"Hello, {name}!")

# def ask_question(question: str, valid_responses=is_string()) -> str:
#     """Asks the user their name, validates the input, and returns it."""
#     while True:
#         name = input(question)
#         if is_string():
#             return name

# user_input = ask_question("What is your name? ",
# valid_responses=is_string())

def ask_question(question: str) -> str:
    """Prompts the user with a question and ensures the input is a
    string with at least one character. Keeps asking until a valid input
    is provided."""
    while True:
        answer = input(question).strip() # Remove extra whitespace.
        if is_string(answer):
            return answer
        print("Invalid input. Please enter a name.")

name = ask_question("What is your name? ")
print(f"Hello, {name}!")

nf.greet()
nf.greet()