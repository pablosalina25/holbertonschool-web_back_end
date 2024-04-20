#!/usr/bin/env python3

"""function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    inserted_document_id = result.inserted_id
    return inserted_document_id