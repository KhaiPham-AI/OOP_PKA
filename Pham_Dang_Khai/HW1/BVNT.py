class Shop:
	def __init__(self, name, items):
		self.name = name
		self.items = items
	def get_items_count(self):
		return len(self.items)

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def defend(self, damage):
        self.health -= damage
        if(self.health <= 0):
            self.health = 0
            return "{} was defeated".format(self.name)
    def heal(self, amount):
        self.health += amount


class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_annual_salary(self):
        return 12 * self.salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self,milliliters):
        if(self.status() >= milliliters):
            self.quantity += milliliters

class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if(quantity >= self.water_requirements):
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return "{} is happy".format(self.name)
        else:
            return "{} is not happy".format(self.name)

class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return "{} has {} games. Total play time: {}".format(self.username,len(self.games),self.played_hours)

class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_need):
        if self.skills >= skills_need:
            if self.language != new_language:
                pre = self.language
                self.language = new_language
                self.skills -= skills_need
                return f"{self.name} switched from {pre} to {self.language}"
            else:
                return f"{self.name} already knows {self.language}"
        else:
            return f"{self.name} needs {skills_need - self.skills} more skills"
