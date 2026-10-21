class Task:
    def __init__(self,id,description,completed  = False):
        self.id = id
        self.description = description
        self.completed = completed
    def __str__(self):
        status = "✓" if self.completed else "x"
        return f"[{status}] #{self.id}: {self.description}"
class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {task}")
        return task

    def get_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return task
        return None

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self._tasks.remove(task)
            return task
        return None

    def list_tasks(self):
        if not self._tasks:
            print("No tasks available.")
        else:
            for task in self._tasks:
                print(task)                         
        return self._tasks