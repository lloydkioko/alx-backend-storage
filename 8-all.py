#!/usr/bin/env python3

"""
contains function def list_all(mongo_collection)
"""


def list_all(mongo_collection):
    """
    List all documents in the given collection.

    Args:
        mongo_collection: The collection object.

    Returns:
        list: A list containing all the documents in the collection.
              Returns an empty list if there are no documents in collection.
    """
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
