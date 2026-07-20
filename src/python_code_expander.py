from pathlib import Path


examples = [

"""
def add(a, b):

    result = a + b

    return result
""",

"""
def subtract(a, b):

    result = a - b

    return result
""",

"""
def multiply(a, b):

    result = a * b

    return result
""",

"""
def divide(a, b):

    if b == 0:

        return None

    result = a / b

    return result
""",

"""
def reverse_string(text):

    result = ""

    for char in text:

        result = char + result

    return result
""",

"""
def count_vowels(text):

    vowels = "aeiou"

    count = 0

    for char in text:

        if char in vowels:

            count += 1

    return count
""",

"""
def calculate_average(numbers):

    total = 0

    for number in numbers:

        total += number

    return total / len(numbers)
""",

"""
def read_file(path):

    with open(path, "r") as file:

        content = file.read()

    return content
""",

"""
def save_file(path, text):

    with open(path, "w") as file:

        file.write(text)
""",

"""
class User:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def introduce(self):

        return self.name
""",

"""
class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height


    def area(self):

        return self.width * self.height
"""
]


def expand(
    output="data/raw/python_expanded.txt",
    repeat=1000
):

    Path(output).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    data = []

    for i in range(repeat):

        code = examples[i % len(examples)]

        data.append(
            "<python>\n\n"
            + code.strip()
            + "\n\n</python>"
        )

    Path(output).write_text(
        "\n\n".join(data),
        encoding="utf-8"
    )

    print("Generated:", len(data))


if __name__ == "__main__":
    expand()