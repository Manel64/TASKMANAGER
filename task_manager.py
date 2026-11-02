import json
class Task:
    def __init__(self,id,description,completed  = False):
        self.id = id
        self.description = description
        self.completed = completed
    def __str__(self):
        status = "✓" if self.completed else "x"
        return f"[{status}] #{self.id}: {self.description}"
class TaskManager:
    FILE_NAME = "tasks.json"
    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {task}")
        self.save_tasks()
        return task

    def get_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        print(f"Task with ID {task_id} not found.")
        return None

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.completed = True
            print(f"Task completed: {task}")
            self.save_tasks()
            return task
        return None

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self._tasks.remove(task)
            print(f"Task deleted: {task}")
            self.save_tasks()
            return task
        return None

    def list_tasks(self):
        if not self._tasks:
            print("No tasks available.")
        else:
            for task in self._tasks:
                print(task)                         
        return self._tasks
    def save_tasks(self, filename = FILE_NAME):
        with open(filename, "w") as f:
            json.dump([task.__dict__ for task in self._tasks], f)

    def load_tasks(self, filename = FILE_NAME):
        try:
            with open(filename, "r") as f:
                tasks_data = json.load(f)
                self._tasks = [Task(**data) for data in tasks_data]
                if self._tasks:
                    self._next_id = max(task.id for task in self._tasks) + 1
        except FileNotFoundError:
            print(f"No se encontró el archivo {filename}.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {filename}.")