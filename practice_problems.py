"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    product_set = set()
    for product_id in product_ids:
        if product_id in product_set:
            print(f"Duplicate found: {product_id}")
            return True
        product_set.add(product_id)
    else:
        print("No duplicates found.")
        return False

#has_duplicates([1, 2, 3, 4, 5])  # Output: True


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.queue = []
        

    def add_task(self, task):
        self.queue.append(task)
        print(f"Task added: {task}")

    def remove_oldest_task(self):
        if self.queue:
            oldest_task = self.queue.pop(0)
            print(f"Removed oldest task: {oldest_task}")
        else:
            print("No tasks to remove.")
            return None

    def print_tasks(self):
        print("Tasks in the queue:")
        if not self.queue:
            print("No tasks in the queue.")
        else:
            for task in self.queue:
                print(task)

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task()
task_queue.print_tasks()





"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""


class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)
        #holy crow I overthought this one

    def get_unique_count(self):
        self.unique_count = len(self.unique_values)
        print(f"Values: {self.unique_values}")
        print(f"Unique count: {self.unique_count}")

#call the class function

Tracker = UniqueTracker()
Tracker.add(10)
Tracker.add(20)
Tracker.add(10)
Tracker.get_unique_count()


# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/trypython.asp?filename=demo_dsa_queues_class
# https://www.w3schools.com/python/python_dsa_queues.asp