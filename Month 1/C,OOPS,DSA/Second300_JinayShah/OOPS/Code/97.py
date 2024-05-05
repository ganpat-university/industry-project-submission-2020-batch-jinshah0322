class User:
   def __init__(self, name):
       self.name = name
       self.messages = []

   def send_message(self, message):
       self.messages.append(message)

   def view_message_history(self):
       return self.messages

class Message:
   def __init__(self, sender, content):
       self.sender = sender
       self.content = content

class ChatRoom:
   def __init__(self):
       self.users = []
       self.messages = []

   def add_user(self, user):
       self.users.append(user)

   def remove_user(self, user):
       self.users.remove(user)

   def broadcast_message(self, message):
       for user in self.users:
           user.send_message(message)

room = ChatRoom()

user1 = User('Alice')
user2 = User('Bob')

room.add_user(user1)
room.add_user(user2)

message = Message(user1, 'Hello!')
room.broadcast_message(message)

message = Message(user1, 'How are you!')
room.broadcast_message(message)

message = Message(user2, 'Hii')
room.broadcast_message(message)

message = Message(user1, 'I am fine')
room.broadcast_message(message)

message = Message(user1, 'What are you doing?')
room.broadcast_message(message)

print(user1.view_message_history()[0].sender.name,":",user1.view_message_history()[0].content)
print(user1.view_message_history()[1].sender.name,":",user1.view_message_history()[1].content)
print(user1.view_message_history()[2].sender.name,":",user1.view_message_history()[2].content)
print(user2.view_message_history()[3].sender.name,":",user1.view_message_history()[3].content)
print(user2.view_message_history()[4].sender.name,":",user1.view_message_history()[4].content)
