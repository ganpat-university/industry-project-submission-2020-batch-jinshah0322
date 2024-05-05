class User:
   def __init__(self, name):
       self.name = name
       self.activities = []
       self.goals = {}

   def add_activity(self, activity):
       self.activities.append(activity)

   def set_goal(self, goal_type, goal_value):
       self.goals[goal_type] = goal_value

   def generate_report(self):
       total_calories_burned = sum(a.calories_burned for a in self.activities)
       return f"Total Calories Burned: {total_calories_burned}"


class Activity:
   def __init__(self, type, duration, calories_burned):
       self.type = type
       self.duration = duration
       self.calories_burned = calories_burned


class Tracker:
   def __init__(self):
       self.users = {}

   def add_user(self, user):
       self.users[user.name] = user

tracker = Tracker()

user1 = User('John')

tracker.add_user(user1)

user1.set_goal('Calories Burned', 2000)

activity1 = Activity('Running', 60, 200)

user1.add_activity(activity1)

print(user1.generate_report())
