#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.
    """
    cursor = mongo_collection.find()
    documents = list(cursor)
    return documents
