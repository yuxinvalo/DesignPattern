from time import sleep

class Ubisoft(object):
    def __init__(self):
        self.games = dict()

    def get(self, key):
        return self.games.get(key)

    def set(self, key, game):
        self.games[key] = game

class Game(object):
    def __init__(self, name):
        self.name = name

    @property
    def url(self):
        sleep(3)
        return ("Prince of Persia URL")

ubisoft = Ubisoft()
class ScanGames(object):
    def __init__(self, game):
        self.game = game

    def show(self):
        print(self.game.url)

class Fnac(object):
    def __init__(self, game):
        self.game = game

    @property
    def url(self):
        gameName = ubisoft.get(self.game.name)
        if not gameName:
            gameName = self.game.url
            print("Set game in Fnac store.")
            ubisoft.set(self.game.name, gameName)
        else:
            print("already have this game.")
        return gameName

g = Game(name = "prince of persia")
proxy = Fnac(g)
print("first visit")
scan = ScanGames(proxy)
scan.show()
print("second visit")
scan.show()
