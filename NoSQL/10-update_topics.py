#!/usr/bin/env python3
"""
that changes all topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics in a collection
    name (str): Name of the school whose topics to update
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
