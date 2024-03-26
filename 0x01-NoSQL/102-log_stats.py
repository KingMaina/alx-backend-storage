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
        num_method_logs = logs_nginx_collection.find(
            {'method': {'$eq': method}}).count()
        print('\tmethod {}: {}'.format(method, num_method_logs))

    # Count number of GET requests
    num_get_requests = logs_nginx_collection.find(
        {'method': 'GET', 'path': PATH}).count()
    print('{} status check'.format(num_get_requests))

    # Log IPs
    top_10_present_ips = logs_nginx_collection.aggregate([
       {
           '$group': {
                '_id': '$ip',
                'ipCount': {'$sum': '$ip'}
            }
        },
       {'$sort': {'ipCount': -1}}
    ])
    print('IPs:')
    for ip in top_10_present_ips:
        print('\t{}: {}'.format(ip.get('ip'), ip.get('ipCount')))
    # Close database connection
    client.close()
