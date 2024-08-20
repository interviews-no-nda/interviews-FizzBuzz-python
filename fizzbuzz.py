from typing import Generator, Sequence
import argparse

RULES_DEFAULT = {3: "Fizz", 5: "Buzz"}


def fizzbuzz(rng: range, rules: dict[int, str] | None = None) -> Generator[int | str, None, None]:
    if not rules:
        rules = RULES_DEFAULT

    yield from ("".join((value for key, value in rules.items() if idx % key == 0))
                or idx for idx in rng)


def main(argv: Sequence | None = None) -> int:
    def from_pairs(in_value) -> tuple[int, str]:
        try:
            key, value = in_value.split('=')
        except ValueError:
            raise argparse.ArgumentTypeError(f"argument -c/--conf must be a KEY=VALUE string, not {in_value}")
        return int(key), value

    parser = argparse.ArgumentParser(
        prog="python "+__file__, description="pyhton implemnetation of FizzBuzz"
    )
    parser.add_argument("-s", "--start", default=1, type=int, help="range lower boundary. Default is 1")
    parser.add_argument("-e", "--end", default=50, type=int, help="range upper boundary. Default is 50")
    parser.add_argument("-t", "--step", default=1, type=int, help="increment step boundary. Default is 1")

    parser.add_argument("-c", "--conf", type=from_pairs, nargs='+', metavar='INT=STR', help=f"Custom FizzBuzz rule.\
                        Default is '{" ".join(('='.join((str(key), value)) for key, value in RULES_DEFAULT.items()))}")

    args = parser.parse_args(argv)
    rules = None
    if args.conf:
        rules = dict(args.conf)

    fixx_buzz_gen = fizzbuzz(range(args.start, args.end+1, args.step), rules=rules)
    print(*(value for value in fixx_buzz_gen), sep="\n")

    return 0


if __name__ == "__main__":
    exit(main())
