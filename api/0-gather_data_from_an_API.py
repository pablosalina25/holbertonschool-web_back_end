#!/usr/bin/python3
"""
This module retrieves info about the progress of a given employee's TODO list
using a REST API.
"""

import requests
import sys


def main():
    """
    Retrieve employee's TODO list progress and display it.
    """
    done_tasks_count = 0
    task_titles = []

    employee_id = sys.argv[1]
    employee_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(employee_id)).json()
    employee_name = employee_info.get("name")
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(employee_id)).json()

    for task in tasks:
        if task.get("completed"):
            task_titles.append(task.get("title"))
            done_tasks_count += 1

    total_tasks_count = len(tasks)

    print("Employee {} has completed tasks ({}/{}):".
          format(employee_name, done_tasks_count, total_tasks_count))

    for title in task_titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
