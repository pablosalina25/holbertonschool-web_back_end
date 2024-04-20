#!/usr/bin/env python3
"""
List all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    cursor = mongo_collection.find()
    documents = list(cursor)
    return documents