class Task:
   def __init__(self, description, due_date):
       self.description = description
       self.due_date = due_date
       self.status = "Not Started"

   def start_task(self):
       self.status = "In Progress"

   def complete_task(self):
       self.status = "Completed"


class Project:
   def __init__(self, name):
       self.name = name
       self.tasks = []

   def add_task(self, task):
       self.tasks.append(task)


class TeamMember:
   def __init__(self, name):
       self.name = name
       self.projects = []

   def add_project(self, project):
       self.projects.append(project)

team_member1 = TeamMember('John')

project1 = Project('Project1')

team_member1.add_project(project1)

task1 = Task('Task1', '2024-01-20')

project1.add_task(task1)

task1.start_task()

task1.complete_task()

print(task1.status)
