class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def add_player(self, player):
        for p in self.__players:
            if p.get_name() == player.get_name():
                return f"Player {player.get_name()} has already joined"
        self.__players.append(player)
        return f"Player {player.get_name()} joined team {self.__name}"

    def remove_player(self, player_name):
        for i, p in enumerate(self.__players):
            if p.get_name() == player_name:
                self.__players.pop(i)
                return p
        return f"Player {player_name} not found"