from app.core.mongo import db

async def create_post(post: dict):
    result = await db['Posts'].insert_one(post)
    return str(result.inserted_id)

async def get_post_by_id(post_id: str):
    post = await db['Posts'].find_one({'id': post_id})
    if post:
        post['_id'] = post_id
    return post