class Team:
   def __init__(self, name):
       self.name = name

class Match:
   def __init__(self, team1, team2):
       self.team1 = team1
       self.team2 = team2
       self.winner = None

   def declare_winner(self, winning_team):
       if winning_team == self.team1 or winning_team == self.team2:
           self.winner = winning_team
       else:
           print("Invalid winner declared.")

class Tournament:
   def __init__(self):
       self.matches = []
       self.teams = []

   def add_match(self, match):
       self.matches.append(match)

   def add_team(self, team):
       self.teams.append(team)

   def declare_winner(self, winning_team):
       for match in self.matches:
           print("Out of", match.team1.name,"and", match.team2.name,",", match.winner.name,"wins the game")
               


team1 = Team('Team1')
team2 = Team('Team2')

match1 = Match(team1, team2)

tournament = Tournament()

tournament.add_team(team1)
tournament.add_team(team2)
tournament.add_match(match1)

match1.declare_winner(team1)
tournament.declare_winner(team1)
