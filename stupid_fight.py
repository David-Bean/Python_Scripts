
# Classes and inheritence practice.

# you can choose between Mike, Gum, and Silty. They attack each other...
# ex: mike.attack(silty)

# that's pretty much it.

class Entity:
	def __init__(self,health = 1, name = 'Entity',**kwargs):
		self.health = health
		self.name = name
		self.alive = True
		super().__init__(**kwargs)

	def death_check(self):
		if self.health <= 0:
			self.alive = False
			return False


class Fighter():
	def __init__(self,speed = 8,damage = 14,energy = 6,**kwargs):
		#super().__init__(**kwargs)
		self.speed = speed
		self.damage = damage
		self.energy = energy
		super().__init__(**kwargs)

	def attack(self,enemy):
		if self.alive == False:
			print (f'\n{self.name} is dead and can no longer do things.')
		else:
			if enemy.alive == False:
				print (f"\n{self.name} pointlessly attacked {enemy.name}'s corpse")
			else:
				enemy.health -= self.damage
				print (f"\n{self.name} dealt {enemy.name} {self.damage} points of damage!")
				print (f"{enemy.name} now has {enemy.health} health points")

				if enemy.death_check() == False:
					print (f"\n{self.name} has killed {enemy.name}")



class Human(Fighter,Entity):
	def __init__(self,type, health = 80,**kwargs):
		super().__init__(**kwargs)
		self.type = type
		self.health = health


class Monster(Fighter,Entity):

	def __init__(self,size = False,health = 100,**kwargs):
		super().__init__(**kwargs)
		self.health = health
		self.size = size
		

		if size == 'large':
			self.damage*=3
	


#Mike
human = Human(
	type = 'soldier'
	)

#Gum
big_monster = Monster(
	health = 150,
	size = 'large',
	)

#Silty
little_monster = Monster(
	health = 40,
	damage = 7)

#Easter
god = Human(
	name = 'god',
	type = 'diety',
	health = 250,
	damage = 149
)

def startup():
	global human
	global big_monster
	global little_monster

	human.name = input("\n\n\n\n\n\nWhat is the Human's name?: ").lower()
	big_monster.name = input("\nWhat is the big Monster's name?: ").lower()
	little_monster.name = input("\nWhat is the little monster's name?: ").lower()


def remind_names():
	print(f'''
                        Character names:
                        
			Human: {human.name}
			Big Monster: {big_monster.name}
			Little Monsster: {little_monster.name}
			''')

def run_game():

	while human.alive == True or big_monster.alive == True or little_monster.alive == True:
		attacker =input('\n\nAttacker: ').lower()
		victim = input('\nVictim: ').lower()

		if attacker == human.name:
			attacker = human
		elif attacker == big_monster.name:
			attacker = big_monster
		elif attacker == little_monster.name:
			attacker = little_monster
		elif attacker == god.name:
			attacker = god
		else:
			print('\n\nYou should get your fingers checked. You really suck at typing.')
			print('Try again, I guess...')
			remind_names()
			run_game()

		if victim == human.name:
			victim = human
		elif victim == big_monster.name:
			victim = big_monster
		elif victim == little_monster.name:
			victim = little_monster
		elif victim == god.name:
			victim = god
		else:
			print('\n\nWhat is even wrong with you? Be a better typer next time.')
			print('Just... can you actually try this time?')
			remind_names()
			run_game()
		
		attacker.attack(victim)

def new_game():
	print('\n\n\nEveryone is dead. Congradulations.')
	print("\n\n\n GAME OVER")

	if input("\n\nPlay again?:").lower() == 'yes':

		main()

def main():

	startup()

	run_game()

	new_game()

main()
