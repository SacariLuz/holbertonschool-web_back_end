#!/usr/bin/env python3

"""
Function inserts a school doc
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection
    mongo_collection: pymongo collection object

    return: a new _id generate for document
    """
    _id = mongo_collection.insert_one(kwargs).inserted_id
    
    return _id
