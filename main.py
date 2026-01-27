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
        self.file_path = Path(file_name)
        if not self.file_path.exists():
            self.save_all([])

    def read_all(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_all(self, data_list):
        with open(self.file_path, 'w') as file:
            json.dump(data_list, file, indent=4)

    def add_single_entry(self, user_entry):
        current_data = self.read_all()
        current_data.append(user_entry)
        self.save_all(current_data)
      
    
# To do list
class Storage:
  
  def __init__(self, db: Database):
    self.db = db
    
  def create_task(self):
    
    task_id = int(input('Task ID: '))
    task_title = input('Title: ')
    task_desc = input('Description: ')
    
    new_task = Task(task_id, task_title, task_desc)
  
    new_entry = new_task.transform_task()
    
    self.db.create_task(new_entry)
    
    #Save to JSON file

test_db = Database('tasks.json')
storage_test = Storage(test_db)
storage_test.create_task()

  
  
  '''  
  def read_task(self):
    self.db.read_file()
    
  def update_task(self):
  
  def delete_task(self)
  


def UserInteratction:
'''
  




