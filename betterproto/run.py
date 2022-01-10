#!/usr/bin/env python3

from sample import Feature, Person, PersonGender

_TOKEN = bytes('Hello world', 'ascii')


def serialization() -> bytes:
    p = Person(name="John Doe",
               age=45,
               gender=PersonGender.MALE,
               token=_TOKEN,
               alive=True)
    p.features.extend((Feature("height", 187.5),
                       Feature("weight", 94.0)))
    p.extra["facebook"] = "never"

    return bytes(p)


def deserialization(serialized: bytes) -> None:
    p = Person().parse(serialized)


if __name__ == "__main__":
    import os
    import sys

    parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent not in sys.path:
        sys.path.append(parent)

    # noinspection PyPackages
    from benchmark import Benchmark

    benchmark = Benchmark("betterproto", serialization, deserialization)
    benchmark.run()
