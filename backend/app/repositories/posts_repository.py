from app.core.mongo import db
from bson import ObjectId

async def create_post(post: dict):
    result = await db['Posts'].insert_one(post)
    return str(result.inserted_id)

async def get_post_by_id(post_id: str):
    post = await db['Posts'].find_one({'_id': ObjectId(post_id)})
    if post:
        post['_id'] = str(post['_id'])
    return post