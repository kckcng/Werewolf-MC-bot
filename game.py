import random

class Character:
	def __init__(self, ids, char):
		self.id = ids
		self.name = char
		self.alive = True

class Witch(Character):
	def __init__(self, ids):
		super().__init__(ids, "Witch")
		self.save_potion = True
		self.kill_potion = True

class Game:
	def __init__(self, players_num, characters):
		self.players_num = players_num
		self.werewolf_num = characters[0]
		self.king_num = characters[1]
		self.prophet_num = characters[2]
		self.witch_num = characters[3]
		self.hunter_num = characters[4]
		self.civil_num = characters[5]

		self.bad_count = self.werewolf_num + self.king_num
		self.god_count = self.prophet_num + self.witch_num + self.hunter_num
		self.civil_count = self.civil_num

		self.players = {} # id: Chracter object
		self.newly_killed = [] # ids

		self.status = ""
		
	def assign(self,ids):
		werewolf_left = self.werewolf_num
		king_left = self.king_num
		prophet_left = self.prophet_num
		witch_left = self.witch_num
		hunter_left = self.hunter_num
		civil_left = self.civil_num
		to_be_assgined = self.players_num
		while to_be_assgined != 0:
			r = random.randint(0,5)

			if r == 0 and werewolf_left != 0:
				c = Character(ids[to_be_assgined-1], "Werewolf")
				self.players[ids[to_be_assgined-1]] = c
				to_be_assgined -= 1
				werewolf_left -= 1

			elif r == 1 and king_left != 0:
				c = Character(ids[to_be_assgined-1], "Werewolf King")
				self.players[ids[to_be_assgined-1]] = c
				to_be_assgined -= 1
				king_left -= 1

			elif r == 2 and prophet_left != 0:
				c = Character(ids[to_be_assgined-1], "Prophet")
				self.players[ids[to_be_assgined-1]] = c
				to_be_assgined -= 1
				prophet_left -= 1

			elif r == 3 and witch_left != 0:
				c = Witch(ids[to_be_assgined-1])
				self.players[ids[to_be_assgined-1]] = c
				to_be_assgined -= 1
				witch_left -= 1

			elif r == 4 and hunter_left != 0:
				c = Character(ids[to_be_assgined-1], "Hunter")
				self.players[ids[to_be_assgined-1]] = c
				to_be_assgined -= 1
				hunter_left -= 1

			elif r == 5 and civil_left != 0:
				c = Character(ids[to_be_assgined-1], "Civilian")
				self.players[ids[to_be_assgined-1]] = c
				to_be_assgined -= 1
				civil_left -= 1