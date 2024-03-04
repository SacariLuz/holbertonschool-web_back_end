#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds collection, based in the schools

    mongo_collection: pymongo collection object

    returns: the list of school having a specific topic
    """
     school_lists = mongo_collection.find({"topics": topic})
     return school_lists
