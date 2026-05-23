from fastapi import APIRouter
from ..schemas.post import PostCreate
from ..controllers.post_controller import create_post, list_posts
router=APIRouter(prefix="/posts", tags=["posts"])
@router.post("")
def post_create(data:PostCreate): return create_post(data)
@router.get("")
def post_list(): return list_posts()
