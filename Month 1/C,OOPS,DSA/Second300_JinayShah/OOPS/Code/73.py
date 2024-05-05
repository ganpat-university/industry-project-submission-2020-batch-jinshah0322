class Game:
  def __init__(self, title, stats):
      self.title = title
      self.stats = stats

class Player:
  def __init__(self, name):
      self.name = name
      self.inventory = Inventory()

  def add_game(self, game):
      self.inventory.add_game(game)

  def remove_game(self, title):
      return self.inventory.remove_game(title)

  def get_game_statistics(self, title):
      return self.inventory.get_game_statistics(title)

class Inventory:
  def __init__(self):
      self.games = []

  def add_game(self, game):
      self.games.append(game)

  def remove_game(self, title):
      for game in self.games:
          if game.title == title:
              self.games.remove(game)
              return f"Removed {title} from inventory."
      return "Game not found in inventory."

  def get_game_statistics(self, title):
      for game in self.games:
          if game.title == title:
              return game.stats
      return "Game not found in inventory."

game1 = Game("Game1", {"level": 10})
game2 = Game("Game2", {"level": 20})

player = Player("Alice")

player.add_game(game1)
player.add_game(game2)

print(player.remove_game("Game1"))

print(player.get_game_statistics("Game2"))