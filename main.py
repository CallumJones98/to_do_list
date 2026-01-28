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
              print(f"\n Current Task Details ")
              print(f"ID: {t['id']}")
              print(f"Title: {t['title']}")
              print(f"Description: {t['description']}")
              
              if new_title:
                  t['title'] = new_title
              if new_description:
                  t['description'] = new_description
              
              task_found = True
              break 
      
      if task_found:
          if new_title or new_description:
              self.db.write_file(self.current_data)
              print(f"Task {self.task_identification} updated successfully.")
      else:
          print(f"No task with ID {self.task_identification} found.")
    
  def remove_task(self, task_identification: int):
      task_to_remove = None
    
      for t in self.current_data:
          if t['id'] == task_identification:
              task_to_remove = t
              break
              
      if task_to_remove:
          print(f"\nRemoving Task: {task_to_remove['title']}")
          self.current_data.remove(task_to_remove)
          
          self.db.write_file(self.current_data)
          print(f"Task {task_identification} deleted successfully.")
          return True
      else:
          print(f"Error: Task with ID {task_identification} not found.")
          return False


class UserInteraction:
  
  def __init__(self, main_storage: Storage):
    self.main_storage = main_storage
  
  def user_workflow(self):
    
    print('Welcome to your to-do list: ')
    
    menu = ('[0] - Quit \n [1] - See All Tasks \n [2] - See Task \n [3] - Add Task \n [4] - Update Task \n [5] - Delete Task')
    print(menu)
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
        self.main_storage.add_task(new_task)
      
      elif user_inp == 4:
        user_task_id = int(input("Enter ID to change: "))
    
        self.main_storage.update_task(user_task_id) 
        change_title = input("Enter new title (or press Enter to keep current): ")
        change_desc = input("Enter new description (or press Enter to keep current): ")
        
        self.main_storage.update_task(
            user_task_id, 
            new_title=change_title if change_title else None, 
            new_description=change_desc if change_desc else None
        )
        
      elif user_inp == 5:
        delete_id = int(input("Enter ID to delete: "))
        self.main_storage.remove_task(delete_id)
      
      #End of while loop
      print("\n" + menu)
      user_inp = int(input('Please enter choice: '))
  
  print('Thank you - tasks closed and saved')  
        

if __name__ == "__main__":

    my_db = Database("tasks.json")
    
    my_storage = Storage(my_db)
    
    ui = UserInteraction(my_storage)
    
    try:
        ui.user_workflow()
    except ValueError:
        print("\n[Error]: Please enter numbers only for menu choices and IDs.")
    except KeyboardInterrupt:
        print("\n\nProgram closed manually. Goodbye!")
        
