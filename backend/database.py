from motor import motor_asyncio
from model import Todo

client = motor_asyncio.AsyncIOMotorClient('mongodb+srv://sidchan:sidchandani755@cluster0.beq76ug.mongodb.net/')
database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = dict(todo)
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"desc": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True