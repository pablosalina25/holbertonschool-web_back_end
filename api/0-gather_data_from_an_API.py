#!/usr/bin/python3
"""This script fetches and displays an employee's task progress."""

import requests
import sys

def fetch_and_display_employee_progress(employee_id):
    """Fetches and displays an employee's task progress."""
    try:
        # Convertir el ID del empleado a entero
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        return

    employee_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
    
    employee_info = requests.get(employee_info_url).json()
    todo_list = requests.get(todos_url).json()

    employee_name = employee_info.get('name')
    completed_tasks = [task.get('title') for task in todo_list if task.get('completed')]
    total_tasks = len(todo_list)

    print(f'Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t{task}')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fetch_and_display_employee_progress(sys.argv[1])
    else:
        print("Usage: python3 script.py <employee_id>")

