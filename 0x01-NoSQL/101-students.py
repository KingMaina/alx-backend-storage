#!/usr/bin/env python3

"""Returns all students sorted by average score"""
from typing import List, Any


def top_students(mongo_collection) -> List[Any]:
    """Returns all students sorted by average score

        Parameters
        ----------
        mongo_collection: str
            Mongo collection

        Returns
        -------
        List: List of Students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': "$topics.score"}
            }
        },
        {'$sort': {'averageScore': -1}}
    ])
