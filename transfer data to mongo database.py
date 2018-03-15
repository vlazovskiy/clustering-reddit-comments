from pymongo import MongoClient
import lzma
import json

client = MongoClient()
db = client.reddit_comments

with lzma.open('reddit_comments.xz') as f:
    for line in f:
        d = json.loads(line)
        db.reddit_comments.insert_one(d)
