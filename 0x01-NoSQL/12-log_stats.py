#!/usr/bin/env python3

"""Provides some stats about Nginx logs stored"""
from pymongo import MongoClient


if __name__ == '__main__':
    DB = 'mongodb://127.0.0.1:27017'
    METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    PATH = '/status'

    # Connect to the database
    client = MongoClient(DB)
    logs_nginx_collection = client.logs.nginx

    # Print total logs
    num_logs = logs_nginx_collection.estimated_document_count()
    print(num_logs, 'logs')

    # Print total number of request for each method
    print('Methods:')
    for method in METHODS:
        num_method_logs = logs_nginx_collection.count_documents(
            {'method': {'$eq': method}})
        print('\tmethod {}: {}'.format(method, num_method_logs))

    # Count number of GET requests
    num_get_requests = logs_nginx_collection.count_documents(
        {'method': 'GET', 'path': PATH})
    print('{} status check'.format(num_get_requests))

    # Close database connection
    client.close()
