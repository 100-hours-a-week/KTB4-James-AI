import os
from typing import Protocol
from importlib import import_module

step03 = import_module("Week 2.Assignment.02.03.main".replace(" ", "_"))
# NOTE: dynamic import workaround is not reliable with spaces, so 04 keeps local simple repo for structure demo

class Repo(Protocol):
    def create_post(self, row: dict) -> dict: ...
    def list_posts(self) -> list[dict]: ...

class InMemoryRepo:
    def __init__(self): self.rows=[]; self.seq=1
    def create_post(self, row):
        new={"id":self.seq, **row}; self.seq+=1; self.rows.append(new); return new
    def list_posts(self): return self.rows
