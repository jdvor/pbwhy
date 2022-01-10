#!/usr/bin/env python3

from sample_pb2 import Feature, Person

_TOKEN = bytes('Hello world', 'ascii')


def serialization() -> bytes:
    f1 = Feature()
    f1.name = "height"
    f1.value = 187.5

    f2 = Feature()
    f2.name = "weight"
    f2.value = 94.0

    p = Person()
    p.name = "John Doe"
    p.age = 45
    p.gender = Person.Gender.MALE
    p.token = _TOKEN
    p.alive = True
    p.features.extend((f1, f2))
    p.extra["facebook"] = "never"
    return p.SerializeToString()


def deserialization(serialized: bytes) -> None:
    p = Person()
    p.ParseFromString(serialized)


if __name__ == "__main__":
    import os
    import sys
    from google.protobuf.internal import api_implementation

    parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent not in sys.path:
        sys.path.append(parent)

    # noinspection PyPackages
    from benchmark import Benchmark

    benchmark = Benchmark(f"protobuf_{api_implementation.Type()}", serialization, deserialization)
    benchmark.run()