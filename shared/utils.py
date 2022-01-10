import time
from contextlib import contextmanager
from typing import Generator

@contextmanager
def time_attack() -> Generator[None, None, None]:
    print("Starting time measurement... ")
    start = time.monotonic() 
    try:
        yield 
    finally:
        end = time.monotonic()
        print(f"Code within 'with' block took {end - start:.5e}")
