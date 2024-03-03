#!/usr/bin/env python3

"""
Lists the documents
"""

import pymongo


def list_all(mongo_collection) -> list:
    """
    Lists all documents in a collection
    
    mongo_collection: pymongo collection object

    Return: empty list if no document in the collection
    """
    documents = []

    cursor = mongo_collection.find()

    for document in cursor:
        documents.append(document)

    return documents
