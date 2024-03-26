#!/usr/bin/env python3

"""Contains a function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Lists all the documents in a collection

        Parameters
        ----------
        mongo_collection: str
            Mongo collection

        Returns
        -------
        Documents from the given mongo collection
    """
    return mongo_collection.find()
