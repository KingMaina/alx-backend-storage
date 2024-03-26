#!/usr/bin/env python3

"""Inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in the school collection

        Parameters
        ----------
        mongo_collection: str
            Mongo collection
        kwargs: dict
            Dictionary of key-value pairs

        Returns
        -------
        ID of the added document
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
