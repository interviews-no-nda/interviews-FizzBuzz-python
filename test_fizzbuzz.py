import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("args, expected", [
    (
        (1, 10),
        (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz')
    ),
    (
        (1, 15),
        (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz')
    ),
    (
        (5, 15),
        ('Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz')
    ),
    (
        (10, 10, {3: "Fizz", 5: "Buzz", 10: "Tenzz"}),
        ("Tenzz",)
    ),
    (
        (1, 10, {3: "Fizz", 5: "Buzz", 10: "Tenzz"}),
        (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', "BuzzTenzz")
    ),
    (
        (100, 110, {3: "Fizz", 5: "Buzz", 10: "Tenzz"}),
        ('BuzzTenzz', 101, 'Fizz', 103, 104, 'FizzBuzz', 106, 107, 'Fizz', 109, 'BuzzTenzz')
    ),

])
def test_generator_default(args, expected):
    gen = fizzbuzz(*args)
    actual = tuple(value for value in gen)
    assert actual == expected
