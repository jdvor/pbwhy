from time import perf_counter_ns
from sample_pb2 import Feature, Person
from google.protobuf.internal import api_implementation


COUNT = 100000
_token = bytes('Hello world', 'ascii')
_serialized = bytes()

print(f"implementation: {api_implementation.Type()}")


def serialization() -> None:
    global _serialized, _token

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
    p.token = _token
    p.alive = True
    p.features.extend((f1, f2))
    p.extra["facebook"] = "never"

    _serialized = p.SerializeToString()


def deserialization() -> None:
    global _serialized
    p = Person()
    p.ParseFromString(_serialized)


# warm-up
serialization()
deserialization()
assert len(_serialized) > 0

# benchmark
start = perf_counter_ns()
i = 0
while i < COUNT:
    serialization()
    i += 1
elapsed = (perf_counter_ns() - start) / 1000000
print(f"protobuf serialization ({COUNT}): {elapsed:.2f} ms")

start = perf_counter_ns()
i = 0
while i < COUNT:
    deserialization()
    i += 1
elapsed = (perf_counter_ns() - start) / 1000000
print(f"protobuf deserialization ({COUNT}): {elapsed:.2f} ms")

print(f"_serialized:{len(_serialized)} = {_serialized.hex()}")
