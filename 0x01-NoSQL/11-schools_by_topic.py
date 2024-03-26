#!/usr/bin/env python3

"""Returns the list of school having a specific topic"""
from typing import List, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Any]:
    """Changes all topics of a school document

        Changes based on the name

        Parameters
        ----------
        mongo_collection: str
            Mongo collection
        topics: str
            Topic to search for

        Returns
        -------
        List of schools with the specified topic
    """
    return mongo_collection.find({
        'topics': {'$eq': topic},
    })
