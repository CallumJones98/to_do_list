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
    for t in self.current_data:
      if t['id'] == task_identification:
        print(t)

  
  def update_task(self, task_identification: int, new_title=None, new_description=None):
      self.task_identification = task_identification
      task_found = False

      for t in self.current_data:
        if t['id'] == self.task_identification:
          if new_title:
            t['title'] = new_title
          if new_description:
            t['description'] = new_description
          
          task_found = True
          break 
        
      if task_found:
        self.db.write_file(self.current_data)
        print(f"Task {self.task_identification} updated successfully.")
      else:
        print(f"No task with ID {self.task_identification} found.")
          
  def remove_task(self, task_identification: int):
    for t in self.current_data:
      if t['id'] == task_identification:
        del t


def UserInteratction:
  
  def __init__(self, main_storage: Storage):
    self.main_storage = main_storage
  
  def user_workflow(self):
    
    print('Welcome to your to-do list: ')
    
    print('[0] - Quit \n [1] - See All Tasks \n [2] - See Task \n [3] - Add Task \n [4] - Update Task \n [5] - Delete Task')
    user_inp = int(input('Please enter: '))
  
    while user_inp != 0:
      
      if user_inp == 1:
        self.main_storage.get_all_tasks()
      
      elif user_inp == 2:
        get_task_id = int(input('Enter Task ID: '))
        self.main_storage.get_task(get_task_id)
      
      elif user_inp == 3:
        enter_id = int(input('Enter Task ID: '))
        enter_title = str(input('Enter Title: '))
        enter_desc = str(input('Enter Task Description: '))
        new_task = Task(enter_id, enter_title, enter_desc)
        main_storage.add_task(new_task)
      
      elif user_inp == 4:
        # To finish
