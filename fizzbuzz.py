import types
from typing import Callable, Generator, Sequence
import argparse

RULES_DEFAULT = {3: "Fizz", 5: "Buzz"}


def fizzbuzz(start: int = 1, end: int = 50, rules: dict[int, str] | None = None) -> Generator[int | str, None, None]:
    if not rules:
        rules = RULES_DEFAULT

    if start < 0:
        raise ValueError(f"Range lower bound can not be negative: '{start=}'")

    if start > end:
        raise ValueError(f"Range lower bound can not be larger than the upper bound: '{start=}, {end=}'")

    yield from ("".join((value for key, value in rules.items() if idx % key == 0)) or idx for idx in range(start, end+1))


def main(argv: Sequence | None = None) -> int:
    def from_pairs(string) -> tuple[int, str]:
        try:
            key, value = string.split('=')
        except Exception:
            raise ValueError("argument must be a KEY=VALUE string")
        return int(key), value

    def gen_custom_error(f: Callable):
        def custom_error(self, message):
            if 'from_pairs' in message:
                message = "argument -c/--conf must be a KEY=VALUE string, not"
            f(message)
        return custom_error

    parser = argparse.ArgumentParser(
        prog="python "+__file__, description="pyhton implemnetation of FizzBuzz"
    )
    parser.error = types.MethodType(gen_custom_error(parser.error), parser)
    parser.add_argument("-s", "--start", default=1, type=int, help="range lower boundary. Default is 1")
    parser.add_argument("-e", "--end", default=50, type=int, help="range upper boundary. Default is 50")
    parser.add_argument("-c", "--conf", type=from_pairs, nargs='+', metavar='INT=STR', help=f"Custom FizzBuzz rule.\
                        Default is '{" ".join(('='.join((str(key), value)) for key, value in RULES_DEFAULT.items()))}")

    args = parser.parse_args()
    rules = None
    if args.conf:
        rules = dict(args.conf)

    f = fizzbuzz(start=args.start, end=args.end, rules=rules)
    print(*(value for value in f), sep="\n")

    return 0


if __name__ == "__main__":
    exit(main())
