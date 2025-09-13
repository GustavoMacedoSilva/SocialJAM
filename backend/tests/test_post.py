import pytest
from app.repositories import posts_repository

@pytest.mark.asyncio
async def test_mongo_connection(mongo_client):
    collections = await mongo_client.list_collection_names()
    assert isinstance(collections, list)

@pytest.mark.asyncio
async def test_create_post(mongo_client, monkeypatch):
    monkeypatch.setattr(posts_repository, 'db', mongo_client)

    post_data = {
        'id': '0', 
        'Author': 'test_user',
        'Content': 'test_content',
        'Comments': []
    }

    post_id = await posts_repository.create_post(post_data)

    assert isinstance(post_id, str)
    assert len(post_id) > 0

@pytest.mark.asyncio
async def test_get_post(mongo_client, monkeypatch):
    monkeypatch.setattr(posts_repository, 'db', mongo_client)

    post_data = {
        'id': '0', 
        'Author': 'test_user',
        'Content': 'test_content',
        'Comments': []
    }

    post_id = await posts_repository.create_post(post_data)

    post = await posts_repository.get_post_by_id(post_id)

    assert post['_id'] == post_id
    assert post['Author'] == post_data['Author']
    assert post['Content'] == post_data['Content']