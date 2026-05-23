from ..models.repository import InMemoryRepo
repo=InMemoryRepo()
def create_post(data): return repo.create_post(data.model_dump())
def list_posts(): return repo.list_posts()
