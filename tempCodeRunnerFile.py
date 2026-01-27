import json 
from pathlib import Path

# item
class Task:
  
  def __init__(self, task_id: int, title: str, description: str):
    self.id = task_id
    self.title = title
    self.desc = description
    
  def transform_task(self):
    return {'id': self.id, 'title': self.title, 'description': self.desc}
    # 'deadline': self.deadline, 'date created': self.date_created,
    # 'is_complete': self.is_complete

# Json file - open, close 
class Database:
    def __init__(self, file_name: str):
        self.json_file = Path(file_name)
        if not self.json_file.exists():
            self.write_file([])
      
    def read_file(self):
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def write_file(self, all_data):
        with open(self.json_file, 'w') as file: 
            json.dump(all_data, file, indent=4)


# To do list
class Storage:
  
  def __init__(self, db: Database):
    self.db = db
    self.current_data = self.db.read_file()
    
  def add_task(self, task: Task):
    transformed_task = task.transform_task()
    self.current_data.append(transformed_task)
    self.db.write_file(self.current_data)
    
  def get_all_tasks(self):
    for row in self.current_data:
      print(row)
  
  def get_task(self, task_identification: int):
    self.task_identification = task_identification
    for t in self.current_data:
      if t['id'] == self.task_identification:
        print(t)
  
test_db = Database('tasks.json')
test_storage = Storage(test_db)
task_one = Task(1, 'test', 'this is a massive test')
test_storage.add_task(task_one)
task_two = Task(2, 'second_test', 'this is a second test')
test_storage.add_task(task_two)
test_storage.get_all_tasks()