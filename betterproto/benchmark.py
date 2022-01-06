from time import perf_counter_ns
from sample import Feature, Person, PersonGender


COUNT = 100000
_token = bytes()
_serialized = bytes()


def serialization() -> None:
    global _serialized, _token

    p = Person(name="John Doe",
               age=45,
               gender=PersonGender.MALE,
               token=_token,
               alive=True)
    p.features.extend((Feature("height", 187.5),
                       Feature("weight", 94.0)))
    p.extra["facebook"] = "never"

    _serialized = bytes(p)


def deserialization() -> None:
    global _serialized
    p = Person().parse(_serialized)


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
print(f"betterproto serialization ({COUNT}): {elapsed:.2f} ms")

start = perf_counter_ns()
i = 0
while i < COUNT:
    deserialization()
    i += 1
elapsed = (perf_counter_ns() - start) / 1000000
print(f"betterproto deserialization ({COUNT}): {elapsed:.2f} ms")

print(f"_serialized:{len(_serialized)} = {_serialized.hex()}")
