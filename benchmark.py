import sys
import sysconfig
import platform
import psutil
from argparse import ArgumentParser
from memory_profiler import profile as memory_profile
from time import perf_counter_ns
from typing import Callable


def cpu_profile(fn):
    """Decorator to print cummulative CPU time costs for a function to stdout."""
    import cProfile
    import io
    import pstats
    from pstats import SortKey

    def inner(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = fn(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        ps = pstats.Stats(profiler, stream=stream).sort_stats(SortKey.CUMULATIVE)
        ps.print_stats()
        print(stream.getvalue())
        return result

    return inner


class Benchmark:

    def __init__(self,
                 name: str,
                 serialization_fn: Callable[[], bytes],
                 deserialization_fn: Callable[[bytes], None],
                 show_serialized: bool = False):
        self._name = name
        self._count = 10000
        self._serialization_fn = serialization_fn
        self._deserialization_fn = deserialization_fn
        self._serialized = bytes()
        self.show_serialized = show_serialized

    def warm_up(self):
        self._serialized = self._serialization_fn()
        self._deserialization_fn(self._serialized)
        assert len(self._serialized) > 0

    def serialization(self) -> float:
        start = perf_counter_ns()
        i = 0
        while i < self._count:
            self._serialization_fn()
            i += 1
        elapsed = (perf_counter_ns() - start) / 1000000
        return elapsed

    def deserialization(self) -> float:
        start = perf_counter_ns()
        i = 0
        while i < self._count:
            self._deserialization_fn(self._serialized)
            i += 1
        elapsed = (perf_counter_ns() - start) / 1000000
        return elapsed

    @cpu_profile
    def serialization_cpu(self):
        """Serialization benchmark with CPU cummulative time cost profiling."""
        return self.serialization()

    @cpu_profile
    def deserialization_cpu(self):
        """Deserialization benchmark with CPU cummulative time cost profiling."""
        return self.deserialization()

    @memory_profile
    def serialization_memory(self):
        """Serialization benchmark with memory profiling."""
        return self.serialization()

    @memory_profile
    def deserialization_memory(self):
        """Deserialization benchmark with memory profiling."""
        return self.deserialization()

    @classmethod
    def get_host_info(cls) -> str:
        ghz = psutil.cpu_freq().max / 1000
        return "\n".join([
            f"CPU: {platform.processor()}, {psutil.cpu_count()} cpu, {ghz:.1f} GHz",
            f"OS: {sysconfig.get_platform()}",
            f"Python: {platform.python_version()}, {platform.python_implementation()}, {platform.python_revision()}",
        ])

    def run(self):
        ap = ArgumentParser(description="")
        ap.add_argument("-s", "--skip_serialization", action="store_true",
                        help="")
        ap.add_argument("-d", "--skip_deserialization", action="store_true",
                        help="")
        ap.add_argument("-c", "--cpu_profile", action="store_true",
                        help="")
        ap.add_argument("-m", "--memory_profile", action="store_true",
                        help="")
        args = ap.parse_args()

        self.warm_up()

        if not args.skip_serialization:
            if args.cpu_profile:
                elapsed = self.serialization_cpu()
            else:
                elapsed = self.serialization()
            if args.memory_profile:
                self.serialization_memory()
            print(f"{self._name} serialization [{self._count}]: {elapsed:.2f} ms")

        if not args.skip_deserialization:
            if args.cpu_profile:
                elapsed = self.deserialization_cpu()
            else:
                elapsed = self.deserialization()
            if args.memory_profile:
                self.deserialization_memory()
            print(f"{self._name} deserialization [{self._count}]: {elapsed:.2f} ms")

        if self.show_serialized:
            print()
            print(f"_serialized [{len(self._serialized)}]: {self._serialized.hex()}")

        print()
        print(Benchmark.get_host_info())