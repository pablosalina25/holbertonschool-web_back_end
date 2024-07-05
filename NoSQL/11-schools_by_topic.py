#!/usr/bin/env python3
"""Function that retrieves the list of schools focusing on a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection represents the pymongo collection object
    topic (string) denotes the topic being queried
    """
    schlist = mongo_collection.find({"topics": topic})
    return (list(schlist))