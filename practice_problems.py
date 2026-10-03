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

# has_duplicates([1, 2, 3, 4, 5])  # Output: True


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
    def __init__(self, value):
        self.front = None
        self.rear = None
        self.value = value
        self.next = None


    def add_task(self, task):
        new_task = self.__init__(task)
        if not self.front:
            self.front = new_task
            self.rear = new_task
        else:
            self.rear.next = new_task
            self.rear = new_task

    def remove_oldest_task(self):
        if not self.front:
            return None
        oldest_task = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return oldest_task

    def print_tasks(self):
        current = self.front
        if not current:
            print("No tasks in the queue.")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

while True: 
    
    task = input("Enter a task to add ( type 1), see all tasks (type 2), or type exit to stop (type 3): ")
    task_queue = TaskQueue(task)

    if task.lower() == '3':
        break
    elif task.lower() == '2':
        task_queue.print_tasks()
    elif task.lower() == '1':
        task = input("Enter the task to add: ")
        task_queue.add_task(task)


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
        pass

    def add(self, value):
        pass

    def get_unique_count(self):
        pass


# https://www.w3schools.com/python/python_sets.asp
# 