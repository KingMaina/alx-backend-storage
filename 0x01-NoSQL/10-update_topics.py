#!/usr/bin/env python3

"""Changes all topics of a school document based on the name:"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Changes all topics of a school document

        Changes based on the name

        Parameters
        ----------
        mongo_collection: str
            Mongo collection
        name: str
            School name to update
        topics: List(str)
            List of topics

        Returns
        -------
        None
    """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
    return None
