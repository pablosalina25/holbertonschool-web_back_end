#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def logs_stat(filter=None):
    """Function to retrieve statistics about 'nginx' collection."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    return collection.count_documents(filter)

def main():
    """Main function to print statistics."""
    print(f"{logs_stat()} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: {logs_stat({'method': method})}")
    print(f"{logs_stat({'method': 'GET', 'path': '/status'})} status check")

if __name__ == "__main__":
    main()
