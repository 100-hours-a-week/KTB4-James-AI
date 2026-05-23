from fastapi import FastAPI
from routes.post_routes import router as post_router
app=FastAPI(title="Community API Step 2-4")
app.include_router(post_router)
