import random

# Generate five unique multiplication problems
def generate_multiplication_problems():
    problems = set()  # Use a set to store unique problems
    while len(problems) < 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
        x = random.randint(1, 15) / 10  # Generate a random number between 1 and 1.5
        y = random.randint(1, 15) / 10  # Generate another random number between 1 and 1.5
        if (x, y) not in problems and (y, x) not in problems:  # Check if the problem is unique
            problems.add((x, y))  # Add the unique problem to the set
    return problems

# Format and output the multiplication problems
def output_problems(problems):
    for problem in problems:
        x, y = problem
        print(f"{x} * {y} =")

# Generate and output the multiplication problems
problems = generate_multiplication_problems()
output_problems(problems)
