#!/usr/bin/python
import random
import string
from functools import reduce
from operator import add

import click


@click.command()
@click.option(
        "--length",
        "-l",
        type=int,
        default=16,
        help="Set the string length. Default '16'.")
@click.option(
        "--charclass",
        "-c",
        multiple=True,
        type=click.Choice([
            "alnum",
            "alpha",
            "digit",
            "hex",
            "lower",
            "print",
            "punct",
            "upper",
            ]),
        default=["alnum"],
        help="Set the character map. Default 'alnum'.")
def main(length, charclass):
    """
    Genrates a cryptographic save random string.
    """
    charmap = generate_charmap(charclass)
    randstr = generate_randstr(length, charmap)
    print(randstr)


def generate_randstr(length: int, charmap: str) -> str:
    """
    Generates a random string of ``length``. Choosen characters from
    ``charmap``.
    """
    srand = random.SystemRandom()
    #return "".join([srand.choice(charmap) for _ in range(length)])
    return "".join(list(map(lambda _: srand.choice(charmap), range(length))))


def generate_charmap(chrcls_tup: tuple) -> str:
    """
    Returns a string which includes all selected characters choosen by one or
    more charclass names.
    """
    return "".join(set(reduce(add, map(convert_charclass, chrcls_tup))))


def convert_charclass(chrcls: str) -> str:
    """
    Convert a charclass name to a charmap. A charmap is a ordanary string,
    which is used as array of chars. Following charclasses are valid: 'alnum',
    'alpha', 'digit', 'hex', 'lower', 'print', 'punct', 'upper'.
    """
    if chrcls == "alpha":
        return string.ascii_letters
    if chrcls == "alnum":
        return string.ascii_letters + string.digits
    if chrcls == "print":
        return string.ascii_letters + string.digits + string.punctuation
    if chrcls == "digit":
        return string.digits
    if chrcls == "hex":
        return string.hexdigits
    if chrcls == "lower":
        return string.ascii_lowercase
    if chrcls == "punct":
        return string.punctuation
    if chrcls == "upper":
        return string.ascii_uppercase
    raise ValueError


if __name__ == "__main__":
    main()
