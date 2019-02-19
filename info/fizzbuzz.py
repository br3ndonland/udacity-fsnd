"""
FizzBuzz
https://medium.freecodecamp.org/a-software-engineering-survival-guide-fe3eafb47166
https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b
This solution uses the following syntax features:
Modulo (%, remainder)
Strict equality (==)
Addition assignment (+=)
"""


def fizzbuzz():
    """Print 1-100
    Multiples of 3: Fizz
    Multiples of 5: Buzz
    Multiples of 3 and 5: FizzBuzz
    """
    for i in range(1, 101):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        print(out or i)


if __name__ == "__main__":
    fizzbuzz()
