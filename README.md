# pbwhy

Testing Google's [protobuf](https://github.com/protocolbuffers/protobuf) solution
vs [betterproto](https://github.com/danielgtaylor/python-betterproto)

## protobuf
https://github.com/protocolbuffers/protobuf
```
cd protobuf
pipenv install --dev
pipenv run codegen
pipenv run benchmark
```

=>

```
protobuf serialization (100000): 1445.62 ms
protobuf deserialization (100000): 325.87 ms
_serialized:73 = 0a084a6f686e20446f65102d180122110a0668656967687411000000000070674022110a067765696768741100000000008057402a110a0866616365626f6f6b12056e657665723801
```
[Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz, 1992 Mhz, 4 Core(s), 8 Logical Processor(s), Win 10 64bit, Python 3.8.10]





## betterproto
https://github.com/danielgtaylor/python-betterproto
```
cd betterproto
pipenv install --dev
pipenv run codegen
pipenv run benchmark
```

=>

```
betterproto serialization (100000): 6530.80 ms
betterproto deserialization (100000): 8243.70 ms
_serialized:73 = 0a084a6f686e20446f65102d180122110a0668656967687411000000000070674022110a067765696768741100000000008057402a110a0866616365626f6f6b12056e657665723801
```
[Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz, 1992 Mhz, 4 Core(s), 8 Logical Processor(s), Win 10 64bit, Python 3.8.10]