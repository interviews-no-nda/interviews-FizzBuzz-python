import pytest

from fizzbuzz import fizzbuzz, main


@pytest.mark.parametrize("args, expected", [
    (
        (range(1, 11),),
        (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz')
    ),
    (
        (range(1, 16),),
        (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz')
    ),
    (
        (range(5, 16),),
        ('Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz')
    ),
    (
        (range(10, 11), {3: "Fizz", 10: "Tenzz"}),
        ("Tenzz",)
    ),
    (
        (range(1, 11), {3: "Fizz", 5: "Buzz", 10: "Tenzz"}),
        (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', "BuzzTenzz")
    ),
    (
        (range(110, 121), {3: "Fizz", 5: "Buzz", 10: "Tenzz"}),
        ('BuzzTenzz', 'Fizz', 112, 113, 'Fizz', 'Buzz', 116, 'Fizz', 118, 119, 'FizzBuzzTenzz')
    ),

])
def test_generator(args, expected):
    gen = fizzbuzz(*args)
    actual = tuple(value for value in gen)
    assert actual == expected


@pytest.mark.parametrize("args, expected", [
    (
        ["-e", "24"],
        "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\n",  # noqa: E501 (suppress flake8 E501)
    ),
    (
        ["-s", "10", "-e24"],
        "Buzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\n",  # noqa: E501 (suppress flake8 E501)
    ),
    (
        ["-s12", "-e", "100", "-t4"],
        "Fizz\n16\nBuzz\nFizz\n28\n32\nFizz\nBuzz\n44\nFizz\n52\n56\nFizzBuzz\n64\n68\nFizz\n76\nBuzz\nFizz\n88\n92\nFizz\nBuzz\n",  # noqa: E501 (suppress flake8 E501)
    ),
    (
        ["-s", "12", "-e", "100", "-t4", "--conf", "7=TEST"],
        "12\n16\n20\n24\nTEST\n32\n36\n40\n44\n48\n52\nTEST\n60\n64\n68\n72\n76\n80\nTEST\n88\n92\n96\n100\n",  # noqa: E501 (suppress flake8 E501)
    ),

])
def test_main(args, expected, capsys):
    main(args)
    out, err = capsys.readouterr()
    assert out == expected
