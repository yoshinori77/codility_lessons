import logging
import time

from contextlib import contextmanager


@contextmanager
def timer(name: str):
    t0 = time.time()
    msg = f"[{name}] start"
    print(msg)
    yield
    msg = f"[{name}] done in {time.time() - t0:.2f} s"
    print(msg)