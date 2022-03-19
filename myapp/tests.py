import json
import orjson  # pip install orjson
import time
from datetime import datetime
from functools import partial


example = {
    "timestamp": 1556283673.1523004,
    "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
    "task_level": [1, 2, 1],
    "action_status": "started",
    "action_type": "main",
    "key": "value",
    "another_key": 123,
    "and_another": ["a", "b"],
    "now": datetime(2022, 3, 19, 12, 3, 44, 673881),
}


def default(obj):
    # json.dumps가 datetime.datetime을 deserialize하지못해서 추가
    if isinstance(obj, datetime):
        return str(obj)


def benchmark(name, dumps):
    start = time.time()
    for _ in range(1000000):
        dumps(example)
    print(name, time.time() - start)


if __name__ == "__main__":
    json_dumps = partial(json.dumps, default=default)
    benchmark("python built-in json", json_dumps)

    orjson_dumps = lambda x: orjson.dumps(x).decode("utf-8")
    benchmark("orjson", orjson_dumps)
