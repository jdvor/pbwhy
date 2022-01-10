# pbwhy

Testing Google's [protobuf](https://github.com/protocolbuffers/protobuf) solution
vs [betterproto](https://github.com/danielgtaylor/python-betterproto)

## protobuf cpp
https://github.com/protocolbuffers/protobuf
```
cd protobuf_cpp
pipenv install --dev
[ pipenv run codegen ]
pipenv run all
```

=>

```
protobuf_cpp serialization [10000]: 145.17 ms
protobuf_cpp deserialization [10000]: 36.95 ms

CPU: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel, 8 cpu, 2.0 GHz
OS: win-amd64
Python: 3.8.10, CPython, 3d8993a
```


## protobuf python

```
cd protobuf_python
pipenv install --dev
[ pipenv run codegen ]
pipenv run all
```

=>

```
Loading .env environment variables...
protobuf_python serialization [10000]: 590.71 ms
protobuf_python deserialization [10000]: 348.48 ms

CPU: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel, 8 cpu, 2.0 GHz
OS: win-amd64
Python: 3.8.10, CPython, 3d8993a
```


## betterproto
https://github.com/danielgtaylor/python-betterproto
```
cd betterproto
pipenv install --dev
[ pipenv run codegen ]
pipenv run all
```

=>

```
betterproto serialization [10000]: 613.47 ms
betterproto deserialization [10000]: 962.49 ms

CPU: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel, 8 cpu, 2.0 GHz
OS: win-amd64
Python: 3.8.10, CPython, 3d8993a
```

## Benchmark execution with profiling

Run both serialization & deserialization benchmark optionally with CPU and memory profiling:
```shell
pipenv run all [ -c, --cpu_profile ] [ -m, --memory_profile ]
```

Run both serialization benchmark optionally with CPU and memory profiling:
```shell
pipenv run serialization [ -c, --cpu_profile ] [ -m, --memory_profile ]
```

Run both deserialization benchmark optionally with CPU and memory profiling:
```shell
pipenv run deserialization [ -c, --cpu_profile ] [ -m, --memory_profile ]
```