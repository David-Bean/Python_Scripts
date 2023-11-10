#### Learning Scratch Chapter 2 ####
# The other learning scratch was getting way too long#






###################################################
##	List Comprehension		#######################
###################################################





# jet = [x for x in range(0,10000) if x % 10 == 0]
# print ('numbers: ',len(jet))

# if len(jet)<1000:
# 	for plane in jet:
# 		print (plane)

# jam = [jelly for jelly in jet if jelly % 1000 == 0]


# kylo = [wren for wren in jet if len(str(wren))<3]

# soot = [ash for ash in jam if len(str(ash))<3]


# kylo = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


# print(f'kylo : {kylo}')

# karpel = {}

# key = 0

# for wren in kylo:

# 	james = int(str(wren)[0])

# 	if james % 2 != 0:


# 		karpel.update({key:wren})

# 		key += 1
		
# print (karpel)

# print (list(karpel.values()))

# jan = [lim for lim in list(karpel.values()) if int(str(lim)[0]) != 3]
# print(jan)


# # The way above does not work with else. There is another way though:

# my_list = [num if num > 10 else '<10' for num in range (0,100)]

# junk = [num if int(str(num)[0]) % 2 == 0 else 'odd number' for num in kylo]

# print ('junk =',junk)

# lep = [thing if isinstance(thing,int) == True  else 'string' for thing in junk]
# print (lep)


# # This way is really useful because it can be used to filter other lists



# inventory_names = ['Screws','Wheels','Metal parts','Rubber bits','Screwdrivers','Wood']
# inventory_numbers = [43,12,95,421,23,43]

# replenish_list = [(name,number) for name,number in zip(inventory_names,inventory_numbers) if number < 25]
# print (replenish_list)





# you can combine list comprehension

# combined_comp = [[x for x in range(5)] for y in range(5)]
# for ylist in combined_comp:
# 	print (ylist)

# What happened here? We did the same thing twice. What the inner comprehension list did to x,
# the outer list comprehension did to the inner. 

# you can put the y for the thing into the inner thing.... umm yeah. like this..

# combined_comp = [[(x,y) for x in range(5)] for y in range(5)]
# for ylist in combined_comp:
# 	print (ylist)

# with this system you can create incredibly complex data structures. I see a coordinate plane here potentially.

# Exercise:
# Create the fields for a chess board
# abcdefgh
#fields 12345678

# my solution (no good)
# alphabet = ['a','b','c','d','e','f','g','h']
# numbers = [1,2,3,4,5,6,7,8]
# chess_fields = [[(x,numb) for x in reversed(alphabet)] for numb in reversed(numbers)]
# print (chess_fields)



#Clearcode's solution

# chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]

# for row in chess_board:
# 	print(row)














######################################
##	Other types of comprehensions	##
######################################

# 	Besides list comprehension, you can alseo create dict and set comprehension

#	dict_comp = {num: num for num in range(10)}
#		
#		for dictionary, you need key value pairs. It's not ultra useful I guess

#	set_comp = {num for num in range(10)}

#	tuple_comp = tuple(num for num in range(10))



# set_comp = {num for num in range(100)}
# print (set_comp)

# dict_comp = {num : num**2 for num in range(10)}
# print (dict_comp)

# tuple_comp =  tuple(num for num in range(100))




# exercise:
# create a dictionary with the keys 'A', 'B','C','D','E'
# each key should have a list as value with the values [1,2,3,4,5]

# chessboard = [[f'{letter}{num}' for num in range(1,6)] for letter in 'ABCDEFGH'[::-1]]
# for row in chessboard:
# 	print(row)

# dictthing = {num : [letter for letter in 'ABCDEFGH'] for num in range(1,6)}
# print(dictthing) #( I did it backwards here )


# Seems like you have to have the values in the inner bracket and the key in the outer bracket.
# I also discovered that you can do list comprehension inside dictionary comprehension. Potentiallh
# Extremely valuable.
















##################################################
##	Sorting Data	##############################
##################################################

# You can pass a function into another function as an argument.
# The sorted function is the best example.

#sorted(iterable,function) # Write a function to tell how to sort the iterable



# list1 = [4,2,3,1,5]

# print(sorted(list1))

# # list even has a sort method that sorts it.


# print(sorted(list1,reverse = True))

# list2 = [('a',3),('b',10),('c',6),('d',5)]

# # to sort this list by the intigers in the tuples, we have to tell python how to sort the list
# # with a function

# def sort_function(item):
# 	return item[1]




# # DO NOT CALL THE FUNCTION in the sorted. no sort_function() nonsense.

# print(sorted(list2, key = sort_function))





# # Because these functions are usually very simple, this is usually done
# # with lambdas

# print(sorted(list2, key = lambda item: item[1]))

# # Need to review lambda functions!




# excersise

# inventory_names = ['Screws','Wheels','Metal parts','Rubber bits','Screwdrivers','Wood']
# inventory_numbers = [43,12,95,421,23,42]
# combined_list = list(zip(inventory_names,inventory_numbers))
# print(combined_list)

# # 1- sort this list by inventory numbers

# def sort_numb(tuples):
# 	return tuples[1]

# print(sorted(combined_list,key = sort_numb))




# print(sorted(combined_list,key = lambda inv_tuple: inv_tuple[1]))



# # 2- sort this list by length of inventory name

# print(sorted(combined_list, key = lambda tuples: len(tuples[0])))









###########################################################
##	other functions that take functions as arguments	###
###########################################################

# Map and Filter

# These have more or less been replaced by list comprehension

# map changes values with a function inside of and iterable

# list1 = [1,2,3,4,5]

# def power_function(num):
# 	return num**2

# print (list(map(power_function,list1)))


# # Can also be done with lambda function
# power_list = list(map(lambda x: x**2, list1))
# print (power_list)





# filter - filters out values from a condition

# def get_below_4(num):
# 	if num < 4:
# 		return True
# 	else:
# 		return False

# print(list(filter(get_below_4,list1)))

# if python gets True from key, filter function keeps the number in the list
# if it gets false, it deletes the value

# print(list(filter(lambda num: num < 4, list1)))





# exercise

# convert the power and filter function to list comprehension.

# power_list = [num**2 for num in list1]
# print(power_list)

# print([num**2 for num in list1])

# filter_list = [num for num in list1 if num < 4]
# filter_list2 = [num if num < 4 else 'poop' for num in list1]

# print(filter_list)
# print(filter_list2)




















######################################
##	File handling	##################
######################################

# Python can open simple files. .txt files for example.

# Python could in theory open any kind of file, but mostly external modules would be required.
# like in pygame




# Python file and target file must be in the same file.

# otherwise, you would have to specify folder.

# 2 ways to do this.

#1- open and close it manually

# file = open('openme.txt')
# print (list(file))

# # if not in same folder, open('folder/openme.txt')

# # you need to close the file after you're done with it, otherwise it will stay in memory
# file.close()


# you can outomaticcaly open and close it with the 'with' thing


# this opens the file and saves it as the 'file' variable. as soon as the indented code
# is read, the file is closed automatically. It's a little cleaner

# with open('openme.txt') as file:
# 	print(list(file))


# # file.read() gives a more readable result.

# with open('openme.txt') as file:
# 	print(file.read())




#	To write a file..

# use with open() after hou specify file, another argument is used/
# r stands for read
# a stands for append
# w stands for write


# with open('openme.txt','a') as file:
# 	file.write('\n\n****Write some more text*****')


# with open('openme.txt') as file:
# 	print(file.read())



# write completely rewrites the file. Any of these seem to create a new file if one isn't found



# with open('newtestfile.txt','w') as file:
# 	file.write('Boobs Boobs Boobs. And Butts. And Boobs.')

# with open('newtestfile.txt') as file:
# 	print(file.read())


#exercise: create a new text file and draw a tree in it

# tree = ''' 
# Don't forget about tripple quotation marks!!!

# 	 x
# 	xxx
#    xxxxx
#   xxxxxxx
#      x
#      x
#      x'''


# with open('tree.txt','w') as file:
# 	file.write(tree)

# with open('tree.txt') as file:
# 	print(file.read())


















###########################
##	Deleting stuff	#######
###########################

# Python can delete things. with del.

# you hardly ever need to delete variables (you can tho)

# in most cases you only need to delete values in a list by index


# a = [1,2,3]

# del a[1]

# print (a)


#you can remove an item by value as well

# a.remove(3)
# print (a)

# This can be used in 2048

# Eggs = [1,0,0,0,3,4,5,6,0,4,3]


# # can also use pop method. removes value by index, the default is -1

# # the difference between pop is that pop is taken off the end.

# print(Eggs.pop(-1))
# print (Eggs)

# Eggs.clear()
# print(Eggs)










#########################################################		#########################################################
#########################################################		#########################################################
##							#############################		#########################################################
##	OBJECTS AND CLASSES		#############################		#########################################################
##							#############################		#########################################################
#########################################################		#########################################################
#########################################################		#########################################################


## What are objects?	##

# 	an object is a container for variables and functions.

# 	for example, a monster object might contain variables for 
# 	health, energy, stanima, damage
# 	and functions for attack, movement, animations.


# 	variables inside objects are called attributes
# 	functions in object are called methods.




# Object-oriented programming (OOP)
#	means you are organizing code via objects, objects interacting
#	with each other

# for larger bits of code, this approach is 'essentially manditory'




##	What are classes?


#	A class is the blueprint for an object. when creating an object, we first need a class.
#	A class also accepts arguments to customize the object

#	classes can also inherit from other classes. The resulting objects will have attributes and methods from both classes.
#	This allows us to reuse code very extensively. Changes in a parent class effect all objects.





#	Advantages of classes and objects

#	1- They organize complex code

#	2- They help create reusable code

#	3- They are used all over the place. You need to understand them to not be lost.

#	4- Classes make it much easier to work with scope.



#	as code complexity increases, need for classes increases.
#	don't be tempted to avoid using classes. It's an important thing to know how to use.





##################################
##	Creating and using objects	##
##################################


# Class names do not use snake_case by convention.

# They use CamelCase instead. Each new word is capitolized, no spaces.
# class Monster:

# 	# attributes
# 	health = 90
# 	energy = 40

# 	# methods
# 	def attack(monster,damage): # this 'monster is a refernce to the object, not the Monster class
# 		print(f'\nThe monster has attacked! {damage} damage was dealt.')
# 		monster.energy -= 20
# 		print ('monster energy:',monster.energy)

# 	def move(monster,speed): # the first parameter is ALWAYS a reference to the object. you can call it anything. It just has to be there
# 		# By convention, the first parameter is just called 'self' for future methods.
# 		print(f'\nThe monster has moved at a speed of {speed}')
# 		monster.energy -= 10
# 		print ('monster energy:',monster.energy)




# # now we turn the class into an object. we do that by calling it like a function
# # it returns the object, so we need to capture it in a variable.


# monster = Monster()


# print(monster.health)
# print(monster.energy)

# #health and energy only exist inside of the class.
# #print(health) #does not work

# monster.attack(10)

# monster.move(20)












##################################################################
##	__Dunder__methods	## dunder stands for double underscore	##
##################################################################


# A dunder method is a method that is not called by the user.

# Instead, it is called by python when something happens.

# example:	__len__ is called when the object is passed into len()

# __init__ is called when the object is created. It is the most important, you
# will be using it the most




# class Monster:

# 	# attributes
# 	health = 90
# 	energy = 40
# 	name = 'frank'

# 	def __init__(self,health,energy):
# 		print(f'The monster was created')

# 		self.health = health

# 		#	self.health referres to the attribute of health
# 		#	health refers to the parameter in the dunder method

# 		self.energy = energy

# 	#methods
# 	def attack(self,ammount):
# 		print('The monster has attacked!')
# 		print(f'{amount} damage was dealt')
# 		monster.energy -= 20
# 		print (f'energy: {monster.energy}')

# 	def move(self,speed):
# 		print ('The monster has moved')
# 		print(f'It has a speed of {speed}')
# 		monster.energy -= 10
# 		print (f'energy: {monster.energy}')



# monster1 = Monster(20,10)
# monster2 = Monster(health = 50, energy = 100)

# print(monster1.health)
# print(monster2.health)


# __init__ methods are activated any time a new object is created
# with the class.

# Most of the time, the class does not have any attributes by default. We create them when we use
# the __init__ method like so:


# class Monster:



# 	def __init__(self,health,energy,name):

# 		self.health = health
# 		self.energy = energy
# 		self.name = name

# 	#methods
# 	def attack(self,ammount):
# 		print(f'{self.name} has attacked!')
# 		print(f'{ammount} damage was dealt')
# 		self.energy -= 5
# 		print ("monster's energy:",self.energy)

# 	def move(self,speed):
# 		print (f'{self.name()} has moved')
# 		print(f'It has a speed of {speed}')
# 		self.energy -= 10
# 		print ("monster's energy:",self.energy)



# monster1 = Monster(20,10,'Frank')
# monster2 = Monster(health = 50, energy = 100,name ='Lary')

# # print(monster1.health)
# # print(monster2.health)

# monster1.attack(13)







#___len__() Dunder method


# class Monster:



# 	def __init__(self,health,energy,name):

# 		self.health = health
# 		self.energy = energy
# 		self.name = name

# 	def __len__(self):
# 		return self.health


# 	def __abs__(self):
# 		return self.energy

# 	#methods
# 	def attack(self,ammount):
# 		print(f'{self.name} has attacked!')
# 		print(f'{ammount} damage was dealt')
# 		self.energy -= 5
# 		print ("monster's energy:",self.energy)

# 	def move(self,speed):
# 		print (f'{self.name()} has moved')
# 		print(f'It has a speed of {speed}')
# 		self.energy -= 10
# 		print ("monster's energy:",self.energy)



# monster1 = Monster(20,10,'Frank')

# print (len(monster1))


# len dunder method needs only self parameter. It just returns something.

# It just returns whatever you have under dunder len when you use len(monster1)

# same for dunder abs. Regardless of whatever it is usually used for, it can be repurpoused with dunder.


# dir:
# print(dir(monster1))

# you pass in an object, and print your result. You get all of the dunder methods, and normal methods ect.
# These extra things are things that python automatically adds to your new class when you make it.




# print(monster1.__dict__) # tells you attributes of the object

# print(vars(monster1)) # does the same thing









# there are some other more advanced dunder methods...

# __call__(self): essentially turns the object into a function. You have to print whatever you get.

# __add__(self,other): adds things and returns a 

# __str__(): returns the string representation of the object. This method is called
# when print() or str() function is invoked on an object.

# class Kite:
# 	def __init__(self,height):
# 		self.height = height

# 	def __str__(self):
# 		return f'A beautiful kite soars in the sky at an altitude of {self.height} feet.'

# 	def __add__(self,other):
# 		return self.height + other

# kite = Kite(20)

# print("kite's height:", kite + 12)

# Again, these dunder methods can be incredibly useful, although __init__() is critical to understand.
# Will probably be doing this the most.


# print (kite)












##############################
## Python and classes	######
##############################


# Everry single thing in python is an object, including strings, integers, ect.

# Even functions are objects!

# A function and a method both execute a block of code. They are functionally the same.
# the difference is that the method ALWAYS belongs to an object, no matter if we made the object,
# or it came with python.

# in python, a function is essentially an object with the __call__ method. Essentially, that's all.
# so when we make a method inside a class, we could add a dunder method. I guess.


# functions or methods can be passed into other objects.

# def add(a,b):
# 	return a + b

# class Test:
# 	def __init__(self,add_function):
# 		self.add_function = add_function

# test = Test(add_function = add)

# # DOn't add brackets. We don't want to call the function,
# # we want to bring in the function itself.

# print(test.add_function(1,2))

# you really want to practice this because passing around functions is a really important thing to understand.






# excersise: 
#
# create a monster class with a parameter called func, store this func as a parameter

# create another class, called attacks, that has 4 methods:
# bite, strike, slash, kick (each method just prints some text.)

# create a monster object and give it one of the attack methods form the attack class.

# class Attacks:

# 	def bite(self):
# 		print ('bite')

# 	def strike(self):
# 		print ('strike')

# 	def slash(self):
# 		print ('slash')

# 	def kick(self):
# 		print ('kick')


# class Monster:

# 	def __init__(self,func):
# 		self.func = func

# attacks = Attacks()
# monster = Monster(func = attacks.bite)

# print (monster.func())












###########################
## Classes and scope	###
###########################

# Since every method has a reference to the class it is easy to get and change class attributes

# Because of this, methods rely much less on parameters, global and return

# Objects can be influenced from the outside and from local scope of function.






# Scope problem


# Not great. Let's do this with classes

# def update_health(ammount):
# 	health += ammount

# health = 10


# print (health)
# update_health(20)
# print(health)



# def update_health(object_,ammount):
# 	object_.health += ammount

# class Monster:
# 	def __init__(self,health,energy):
# 		self.health = health
# 		self.energy = energy

# monster = Monster(health = 100, energy = 50)

# update_health(monster,11)

# print (monster.health)









# def update_health(object_,ammount):
# 	object_.health += ammount

# class Monster:
# 	def __init__(self,health,energy):
# 		self.health = health
# 		self.energy = energy

# 	def update_energy(self,ammount):
# 		self.energy += ammount

# monster = Monster(health = 100, energy = 50)

# monster.update_energy(10)

# print (monster.energy)












# # exercise:

# # create a hero class with 2 parameters: damage, monster

# class Monster:
# 	def __init__(self,health):
# 		self.health = health


# class Hero:

# 	def __init__(self,damage):
# 		self.damage = damage

# 	def attack(self,enemy):
# 		enemy.health -= self.damage

# monster1 = Monster(20)

# hero1 = Hero(damage = 5)

# print(monster1.health)

# hero1.attack(monster1)

# print(monster1.health)

# hero1.attack(monster1)

# print(monster1.health)

# # exercise:

# # 1. create a hero class with 2 parameters: damage, monster

# # 2. the monster class should have a method that lowers the health -> get_damage(amount)

# # 3. the hero class should have an attack method that calls the get_damage method from the monster.
# #	 the amount of damage is hero.damage



























########################################
##	Simple Inheritance	################
########################################

# you will use this kind of inheritance fairly often, and will need to practice it.
# Inheritance means that 1 class gets attributes and methods from another class (or classes)


# basically an object can be created from multiple parent classes. unlimited parent classes.



# class Monster:

# 	health = 50
# 	energy = 100

# 	# def __init__(self,health,energy):
# 	# 	self.health = health
# 	# 	self.energy = energy

# 	def attack(self,amount):
# 		print('The monster has attacked!')
# 		print(f'{amount} of damage was dealt')
# 		self.energy -= 20

# 	def move(self,speed):
# 		print(f'The monster has moved at a speed of {speed}')



# # We want to get all of the info from the monster class to the shark.
# # passing in the methods is very simple, but getting health and energy from __init__() is more complicated.
# # we are skipping that for now.

# # to get inheritance, just add parenthesis after name of sub-class. identify monster.

# class Shark(Monster):


# # Shark only:

# 	def __init__(self,speed):
# 		self.speed = speed

# 	def bite(self):
# 		print ('the shark has bitten!')

# # to override a method for the parent class, just do one with the same name in the child class.

# 	def move(self):
# 		print(f'the shark swam at a speed of {self.speed}')



# shark = Shark(120)


# print (shark.health)

# shark.bite()

# shark.attack(20)

# shark.move()







# to inheret stuff from the parent's __init__() method


# class Monster:

# 	def __init__(self,health,energy):
# 		self.health = health
# 		self.energy = energy

# 	def attack(self,enemy):
# 		enemy.health -= 2
# 		print (f'The monster has dealt {enemy.name} 2 points of nibble damage')
# 		enemy.death_check()

# 	def move(self,speed):
# 		print(f'The monster has moved at a speed of {speed}')




# class Shark(Monster):

# 	# calling the parent's __init__() method has to come from the child's init method.
# 	# two ways.
# 	# old way, call parent class then dunder init method.


# 	def __init__(self,speed,health,energy):
# 		self.speed = speed

# 	#	Older way:
# 		# Monster.__init__(self,health,energy) # <--- need to pass these in as arguments when you make the shark.
		

# 	# #	Newer way	
# 		super().__init__(health,energy)

# 	#	Just checks whatver the parent one is. Don't need self, just need health and energy.
# 	#	for multiple inheritance and more complex inheretance, super() is the much better method


# 	def bite(self):
# 		print ('the shark has bitten!')

# 	def move(self):
# 		print(f'the shark swam at a speed of {self.speed}')



# shark = Shark(120,110,100)





# exercise:

# create a scorpion class that inherets from monster.

# gets health and energy from parent

# there should be a poison_damage attribute

# overwrite the damage method to show poison damage.



# class Hero:

# 	def __init__(self,health,name):
# 		self.name = name
# 		self.health = health

# 	def death_check(self):
# 		if self.health <= 0:
# 			print (f'{self.name} has died. RIP')
# 		else:
# 			print (f"{self.name}'s health is now {self.health}\n")




# class Scorpion(Monster):

# 	def __init__(self,scorpion_health,scorpion_energy):
# 		super().__init__(health = scorpion_health,energy = scorpion_energy)

# 	def attack(self,enemy,attack_type):

# 		if attack_type == 'sting':
# 			enemy.health -= 5
# 			print (f'\nThe scorpion has dealt {enemy.name} 5 points of poison damage')
# 		elif attack_type == 'pinch':
# 			enemy.health -= 8
# 			print (f'\nThe scorpion has pinched {enemy.name} in the face, dealing 8 points of damage')
# 		enemy.death_check()


# class TinyMonster(Monster):

# 	def __init__(self,tiny_monster_health,tiny_monster_energy):
# 		super().__init__(health = tiny_monster_health, energy = tiny_monster_energy)

# 	def attack(self,enemy,attack_type):

# 		if attack_type == 'nibble':
# 			enemy.health -= 2
# 			print (f"\nThe tiny monster nibbled {enemy.name}'s acheles tendon, dealing 2 points of damage")

# 		if attack_type == 'punch':
# 			enemy.health -= 1
# 			print (f"\nThe tiny monster punched {enemy.name} in the pinky toe, dealing 1 point of damage")

# 		enemy.death_check()

		


# scorpion = Scorpion(10,10)

# tiny_monster = TinyMonster(3,3)

# kenny = Hero(name = 'Kenny', health = 20)



# scorpion.attack(kenny,'pinch')

# scorpion.attack(kenny,'sting')

# tiny_monster.attack(kenny,'kick')

# tiny_monster.attack(kenny,'nibble')

# scorpion.attack(kenny,'pinch')

# tiny_monster.attack(kenny,'nibble')


# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')
# tiny_monster.attack(kenny,'nibble')

# I made some fun stuff. They killed Kenny... Bastards.


















###########################
##	Complex inheritence ###
###########################


#	Parent class 1 		Parent Class 2
#		   |______________________|
#					   |
#				  Child Class




# class Monster:

# 	def __init__(self,health,energy,**kwargs):
# 		print (f'kwargs left over from Monster: {kwargs}')
# 		self.health = health
# 		self.energy = energy
# 		super().__init__(**kwargs)

# 	def attack(self,ammount):
# 		print (f'The monster has dealt {ammount} points of nibble damage')

# 	def move(self,speed):
# 		print(f'The monster has moved at a speed of {speed}')


# class Fish:
# 	def __init__(self,speed,has_scales,**kwargs):
# 		print (f'kwargs left over from Fish: {kwargs}')
# 		self.speed = speed
# 		self.has_scales = has_scales
# 		super().__init__(**kwargs)

# 	def swim(self):
# 		print(f"The fish is swimming at a speed of {self.speed}mph")



# We want to create a shark monster that has both monster and fish parent classes!
# for multiple or complex inheretence, classes we want to inherit from should be in parentheses here:

# class Shark(Monster,Fish):

# 	def __init__(self,bite_strength,health,energy,speed,has_scales):
# 		self.bite_strength = bite_strength
# 		super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)




#	mro: method resolution order. What order are the parent indent methods being called in?
#	print(Shark.mro())
# 	it tells us it goes through Shark first, then Monster, then Fish, then generic object.

# 	in class, left-most Shark comes first, the last is the right-most.
# 	class Shark(Monster,Fish)

# the first super().__init__() refers to the first parent class, and the second 
# super().__init__() refers to the second and so on.


# shark = Shark(
# 	bite_strength = 50,
# 	health = 200, 
# 	energy = 55,
# 	speed = 120,
# 	has_scales = False)

# print (shark.has_scales)


# kwargs (keyword arguments) **kwargs makes a list of any arguments you put into the parent class that
# are not relavent to the class itself, but may be relevent to the next parent class the child inherits from.

# in the
#	 __init__(self,health,energy,**kwargs)
# any arguments that are passed on with keywords other than self, health, and energy
# are stored in a dictionary that can be accessed later by using **kwargs again.

# put it in the lower
#	super().__init__(**kwargs)
# to pass it on to the next parent in the mro (method resolution order).

# print(shark.speed)

# Summary of complex inheritence:

# class Shark was created. In the mro, shark came first. 
# next was Monster, next was Fish.

# this order was determined when the class name Shark(Monster,Fish) was written.
# the MRO for Shark(Fish,Monster) would have been Shark, Fish, Monster.
# there can be an unlimited number of parent classes in the MRO.

# The keyword arguments used when the object shark was created would cause the parent
# class to throw an error if the keywords were not used in the __init__() method.

# rather than typing out all of the keywords, use **kwargs as a paramiter in __init__()
# in order to pass them on for later.
# you pass them on with a super().__init__(**kwargs) at the end of your __init__() method.

# the next class in line in the MRO will use them up. 






# class Entity:
# 	def __init__(self,health = 1, name = 'Entity',**kwargs):
# 		self.health = health
# 		self.name = name
# 		self.alive = True
# 		super().__init__(**kwargs)

# 	def death_check(self):
# 		if self.health <= 0:
# 			self.alive = False
# 			return False


# class Fighter():
# 	def __init__(self,speed = 8,damage = 14,energy = 6,**kwargs):
# 		self.speed = speed
# 		self.damage = damage
# 		self.energy = energy
# 		super().__init__(**kwargs)

# 	def attack(self,enemy):
# 		if self.alive == False:
# 			print (f'\n{self.name} is dead and can no longer do things.')
# 		else:
# 			if enemy.alive == False:
# 				print (f"\n{self.name} pointlessly attacked {enemy.name}'s corpse")
# 			else:
# 				enemy.health -= self.damage
# 				print (f"\n{self.name} dealt {enemy.name} {self.damage} points of damage!")
# 				print (f"{enemy.name} now has {enemy.health} health points")

# 				if enemy.death_check() == False:
# 					print (f"{self.name} has killed {enemy.name}")


		


# class Human(Entity,Fighter):
# 	def __init__(self,type, health = 80,**kwargs):
# 		super().__init__(**kwargs)
# 		self.type = type
# 		self.health = health


# class Monster(Entity,Fighter):

# 	def __init__(self,size = False,health = 100,**kwargs):
# 		self.health = health
# 		self.size = size
# 		super().__init__(**kwargs)

# 		if size == 'large':
# 			self.damage*=3


# mike = Human(
# 	type = 'soldier',
# 	name = 'Mike',
# 	)

# gum = Monster(
# 	name = 'Gum',
# 	size = 'large',
# 	)

# silty = Monster(
# 	name = 'Silty',
# 	health = 40,
# 	damage = 7)














##############################
##	Classes Extra Parts 	##
##############################



# class Monster:
# 	'''A monster that has some attributes. Does not have boobs though. Never will'''
# 	def __init__(self,health,energy):
# 		self.health = health
# 		self.energy = energy

# 		# private attributes
# 		self._id = 5
# 		self._hasboobs = False

# 	def attack(self,amount):
# 		print('the monster has attacked!')
# 		print(f'{amount} damage was dealt')
# 		self.energy -= 20

# 	def move(self,speed):
# 		print('the monster has moved')
# 		print(f'it has a speed of {speed}')


# monster = Monster(20,10)

# private attributes:

#	an attribute inside of the class that cannot be 
#	influenced from outside of the class.

#	under __init__() method do self, name of attribute __id, value.
#	by convention, we do not change anything with an underscore in front. _id. We could, but we don't

#	It's a naming convention, really. you can do it to methods as well.


# Hasattr and setattr:
#	Checks to see if an object has an attribute
#	returns true or false boolean

# print(hasattr(monster,'health'))
# print(hasattr(monster,'weapon'))

# if hasattr(monster,'health'):
# 	print(f'The monster has {monster.health} health.')

#setattr(object,'attribute',value)
# setattr(monster,'weapon','sword')
# print (hasattr(monster,'weapon'))

# this allows us to efficiently create new attributes.
# new_attributes = (['weapon','axe'],['armor','shield'],['potion','mana'])
# for attr,value in new_attributes:
# 	setattr(monster,attr,value)

# # Now he is kitted out with three quick lines of code!

# print(vars(monster))


# doc

#object.__doc__ returns the docstring.

# print (monster.__doc__)

# print(help(monster))

















####################
## Modules	########
####################

# Modules are extra parts that we can attach to our programs

# for example, we could import random to work with random numbers.

# We can also create our own modules (across multiple files)
# to make code more organised


# Adding extra parts:

#	you can import from the python standard library, these are prinstalled with python
#	you can import additional modules made by other people that you need to install first.



## Python Standard Library	##

#import module_name

#once a module is imported, call a specific method from the module
# like:  module_name.method()

# import random

# random_number = random.randint(1,100)

# print (random_number)



# To see what else is in the module, usually just use google.
# there is often extensive information out there.

# test_list = [0,1,2,3,4,5,6]
# print (random.choice(test_list))

# Go check out the python standard python.


# import string,random

# print(string.ascii_lowercase)

# to be more specific, you can import only certain things.
# from math import floor
# print (floor(4.9))

# you can also change the name of the functions you import.
# from random import randint as rally_Car_go_fast
# print(rally_Car_go_fast(1,10))

#to get around having to type the module you are calling from everytime 
#ie

# import random

# random_num = random.randint(1,10)


#you can instead do this: 

# from random import *

# random_num = randint(1,10)

# it's kinda like saying from random import all methods and functions




# Exersise:
# Get current time from datetime module

# from datetime import datetime as dt

# current_time = dt.now()
# print (current_time)












##########################
##	External Modules	##
##########################


# External modules are made by other programmers
# They give us a huge amount of extra functionality

# for example, game development, data analysis, machine learning,
# gui, ect.

# These modules are imported like the standard modules,
# however, we first need to to install them. This usually
# happens in the powershell or terminal

# pip is the pythnon package manager.

#clear command resets terminal, cleans it up
# pip list has terminal list all the modules installed.

# I have to use pip3 tho!


# import pyautogui
# from time import sleep

# sleep(1)

# pyautogui.write('This is written by a computer',interval= .25)

#this is written by a computer



# Exercise:
# create a graph with pyplot

# import matplotlib.pyplot as plt

# l_range = -10
# h_range = 10

# x_values = [x for x in range(l_range,h_range+1)]

# def fcn(x):
# 	return x**2

# y_values = [fcn(x) for x in x_values]

# print (x_values)
# print (y_values)



# plt.plot(y_values)
# plt.show()


# plt.plot([1,2,3,4])
# plt.xlabel('Silly Face')
# plt.ylabel('Jeppy-poo')
# plt.show()













######################
## Custom Modules	##
######################

# We mainly do this for organization. It's a good idea for larger projects.

# from my_module import Boogie


# print(my_module.test_var)

# print(Boogie().boogie)

# Boogie().boogiedown()

# We are calling classes from other files now! WOWSA



# Exercise: create a sum calculator that takes unlimited arguments and returns the sum.
# create it in another file and run it here.



# import sum_calc

# sum = sum_calc.add(1,3,4,5,6,7,8)
# print (sum)

# from this exercise, I learned that you can take an unlimited amount
# of arguments by using *args (*the star can go on anything) as the parameter in the function.

# **kwargs works for keyword argments












##################
##	__main__()	##
##################


# When a python file is called it creats a few internalv ariables.
# The most used one is __name__

# The currently executed file
#	__name__ == '__main__'

# Any imported file
# __name__ == '__filename__'

# This is really useful to control which code is and isn't being executed.

# print (__name__)

# import sum_calc

# if __name__ == '__main__':
# 	print ('This can only be executed from the main file.')

# This makes sure that you are not executing code you don't want from a module.























######################################    	#####################################################
##	Extra Topics	#############    	#########################################################
#############################    	#############################################################

# That's it for the beginner stuff. This is stuff that isn't necessary until you're doing more advanced
# projects. However, the video is a good resource https://www.youtube.com/watch?v=mDKM-JtUhhc&list=PLT5nW8r--OGsAo1ZyjUK1Luh9PsAKlzCE

# This is the section that starts @ exactly 10 hours in.
# I'm going to watch it now to get a little bit of an idea







######################
## Pass and input	##
######################

# Pass tells python to not do anything.
# you can add this to a function if you don't have code yet.

# input is one way to get user input, although it is very rarely used (I'm already familiar with input)

def really_important_function():
	pass

# pass just tells python to not do anything. It's just a filler




# Input
# user_input = input('press a button')

# sublime does not support user input





######################################
##	Exceptions and Error handling	##
######################################


# Your code should obviously not contain errors, however they happen.
# you need to be able to anticipate errors and deal with them without crashing the program

# try:
# 	print (1/0)
# except:
# 	print('something else')


# try:
# 	print (a)
# 	print (1/0)# <-------- AS SOON AS try encounters an error, it jumps to the exceptions. It doesn't even look at this line
# except ZeroDivisionError:
# 	print('something else')
# except NameError:
# 	print('does not exist')

# he terminal can tell you what type of error is causing the crash and you can
# handle it with except

# With try and except, if the code causes a crash, you can easily add an alternate option.
# I did some of this inadvertantly with some of my other programs just using if statements.

# You can find all of the types of errors in python (Built in exceptions)



# anticipating errors / exceptions
# try:
# 	print ('try')
# 	# print (1/0)# <-------- AS SOON AS try encounters an error, it jumps to the exceptions. It doesn't even look at this line
# 	# print (1/10)
# except ZeroDivisionError:
# 	print('you cannot divide by zero')
# except NameError:
# 	print('variable does not exist')
# else:
# 	print('the else statement is triggered if there are no exceptions') # <---- if there are no found exceptions, else can be printed
# finally:
# 	print('finally runs wether there are exceptions or not')


# raising exceptions

# var_must_be_string = ['Test string']

# if isinstance(var_must_be_string,str):
# 	print(var_must_be_string)
# else:
# 	raise TypeError('Must be a string')

# you can create your own crash messages! Choose what type of error it is,
# write a little note.


# assert

# it's like a stronger if statement. if it's not, the entire code won't run.
# a = 4
# assert a == 5


# Sometimes in your code, you really want to make sure a certain condition is true.




# Exercise:
#	create a list and try to raise an Index error.
#	also add else and finally to handle the error

# test_list = [1,2,3,4,5,6,7,4]

# def i6_times_two(list_):
# 	try:
# 		return list_[6]*2
# 	except:
# 		'list does not have value with index 6'
# 	else:
# 		'Something is funky with that list. Check it again'
# 	finally:
# 		print ('function complete')

# print(i6_times_two(test_list))











########################
##	Decorators	########
########################

# Decorators are functions that 'decorate' other functions
# we essentially wrap a function around another function

# allows us to run code before and after the function without changing the function in question.
# all of the actual logic happens inside of the decorator

# This way we can give extra functionality to a function without changing it.




# The cases you might need to use decorators:

#		Working on a team project and want to avoid unnecessary code changes.

#		Wanting to test code without changing it

#		Decorators in classes allow you to run code when an attribute is accessed or changed



#	Decorators are quite difficult for beginners. It is recommended that I try to 
#	follow along anyway because it is good practice to understand how to pass functions around
#	via the return statement.

#	Functions recap:

#	func() with parentheses calls and executes the function.
#	func   without parentheses simply returns the function as an object that
#		   can be used by other functions/objects

# def func():
# 	print('function')

# print (func)# <--- returns function object.

#	this func object can be passed around like any other object.


# def wrapper(func):		# So this here is basically the main idea of a decorator.
# 	print('hello')		# Calling a function within another function, while executing some code
# 	func()				# Before and after it.
# 	print('goodbye')	# I suppose in this case, the decorator would be the wrapper function

# wrapper(func)



# You can also create a whole new function inside of another function

# def function_generator():
# 	def new_function():
# 		print('New function')
# 	return new_function

# new_func= function_generator()

# new_func()



# def decorator(func):
# 	def wrapper():
# 		print('decoration begins...')
# 		func()
# 		print('decoration ends.')
# 	return wrapper

# def func():
# 	print('Function')

# new_func = decorator(func)
# new_func()

# func()

#Here we are officially adding new functionality to the function...
#LATER down in the code!

# func = decorator(func)
# func()

#I am seeing how you could layer in new functionalities as the function is 
#executed down the line...

#We can have really complex code and still check our function without making any
#changes to the code whatsoever



# Since this is reasonably common, there is shorthand for it in python





# def decorator(func):
# 	def wrapper():
# 		print('decoration begins...')
# 		func()
# 		print('decoration ends.')
# 	return wrapper

 
# # @ decorator   #.  <----- This is essentially doing the same thing as the statement above
# # def func():
# # 	print('Function')

# # func()



# import time


# def duration_decorator(func):
# 	def wrapper():
# 		start_time = time.time()
# 		func()
# 		duration = time.time() - start_time
# 		print (f'duration: {duration}')
# 	return wrapper

# #@decorator #<---- you can add multiple decorators!
# @duration_decorator


# def func():
# 	print('Function executed')
# 	time.sleep(1)

# func = duration_decorator(func)

# func()

# This could be great for debugging. You could do this if your code
# is running very slow and you want to identify what is slowing it down

# In a game, I could see this being useful for something like... weapon enchantments? maybe?





# Exercise:
#		Create a decorator that exicutes a function twice.
#		should be called with the other two previously made decorators. Three decorators in total.

# import time

# def status_decorator(func):
# 	def wrapper(x):
# 		print('executing function')
# 		func(x)
# 		print('function executed')
# 	return wrapper

# def timer_decorator(func):
# 	def wrapper(x):
# 		time_start = time.time()
# 		func(x)
# 		duration = time.time() - time_start
# 		print (f'duration: {duration}')
# 	return wrapper

# def string_check_decorator(func):

# 	def wrapper(x):
# 		try:
# 			print (f"The string being converted into a list is '{x}'")
# 			func(x)
# 		except:
# 			print (f'\n---input {x} is not a string---\n')
# 	return wrapper

# def double_decorator(func):
# 	def wrapper(x):
# 		print ('\nfirst function call:')
# 		func(x)
# 		print ('\nsecond function call:')
# 		func(x)
# 	return wrapper

# @timer_decorator
# @double_decorator
# @string_check_decorator
# @status_decorator


# def string_to_list(string):
# 	print ([letter for letter in string])


# string_to_list('Jelly Beans')

# From this exercise I learned that if you want to pass a parameter down, it needs
# to travel through the wrappers in the decorators. That's why I put an 'x' inside all the wrappers
#
# I went off script and made a new function that requires an input. So i had to troublshoot on my own here...





# He covered the part I already figured out, about decorating functions that have parameters.
# He also says that decorators themselves can also have parameters.


#Common practice to pass arguments/parameters into a wrapper is to do it like this..


# def arg_count_decorator(fcn):

# 	def wrapper(*args):  # <---- Using * and ** so that wrapper can take any parameter.

		
# 		print (f'{len(args)} arguments were passed through the function.')
# 		return smoosh(args)

# 	return wrapper

# @ arg_count_decorator

# def smoosh(*args):
# 	smooshed = ''
# 	#print (args) # <---- used this to find out that the arguments were stored inside of a tuple inside of a tuple when using *args
# 	for tuple_ in args:
# 		for string in tuple_:
# 			smooshed += string
# 	return smooshed



# smoosh('donkey','chicken','bunny')

# COuld not get this thingy to work. I don't know why.




#	Extra fancy decorators	######


# def repetition_decorator(repetitions):
# 	def decorator(func):
# 		def wrapper():
# 			for r in range(repetitions):
# 				func()
# 		return wrapper
# 	return decorator

# @repetition_decorator(20)

# def func():
# 	print('function')

# func()







######################################
## Decorators inside of classes		##
######################################

#	@ property is used inside of classes to turn methods into attributes.
#	Comes from the property function.


#	The goal here is to observe x. Whenever it is looked at or changed, we run some other code.

# class GenericClass:
# 	def __init__(self):
# 		self.x = 10


# generic_object = GenericClass()

# print(generic_object.x)



#	#	#	#	#	#	#	#	#

# The property() function has three attributes. Getter, Setter, Deleter.
# We can set each of them to different methods inside the class.

# we turn the original x into a private method, and work with it's property substitute

# class GenericClass:
# 	def __init__(self):
# 		self._x = 10

# 	def getter(self):
# 		print('got x')
# 		return self._x #	<----- so we called generic x and showed the private _x
# 					   #		
# 					   #	The point is that outside of the class we are using the property substitute x		
# 					   #	and inside we are using self._x

# 	def setter(self,value):
# 		print(f'set x to {value}')
# 		self._x = value

# 	def deleter(self):
# 		print('deleted x')
# 		del self._x

# 	x = property(getter,setter,deleter)


# generic_object = GenericClass()

# print (generic_object.x)

# generic_object.x = 4

# print(generic_object.x)

# del generic_object.x

# try:
# 	print(generic_object.x)
# except:
# 	print('Tried to print x, could not find x')




#	#	#	#	#	#		


#	So with this, whenever we get, set, or delete x, we can also run whatever code we like.
#	example:

# from datetime import datetime

# class GenericClass:


# 	def __init__(self):
# 		self._x = 10
# 		self.x_log_ = []

# 	def getter(self):
# 		print('got x')
# 		self.x_log_.append(datetime.now())
# 		return self._x 

# 	def setter(self,value):
# 		print(f'set x to {value}')
# 		self._x = value

# 	def deleter(self):
# 		print('deleted x')
# 		del self._x

# 	def x_log(self):
# 		print ('x was accessed at these times:')
# 		for time in self.x_log_:
# 			print (time)

# 	x = property(getter,setter,deleter) #	<-- Turns x into a property. From outside of the class,
# 										#		whenever we access x, store the value in self._x
# 										#
# 										#		That way, when we access, change or delete a value we can run
# 										#		whatever other code we want :)


# generic_object = GenericClass()


# print (generic_object.x)	#	<--- Getting x 3 times...

# print (generic_object.x)

# print (generic_object.x)

# generic_object.x_log()		#	<--- Seeing at what times was got x	




#	#	#	#	#	#

#	The above is cumborsome so there is another built in way to do this.
#	with the @property decorator.




# from datetime import datetime

# class GenericClass:

# 	def __init__(self):
# 		self._x = 10
# 		self.x_log_ = []



# 	@property #	<---	the next one is automatically declared the getter.
# 			  #			for the setter and deleter, use the same name used for the getter function.
# 	def x(self):
# 		print('got x')
# 		self.x_log_.append(datetime.now())
# 		return self._x 

# 	@x.setter
# 	def x(self,value):
# 		print(f'set x to {value}')
# 		self.x_log_.append(datetime.now())
# 		self._x = value

# 	@x.deleter
# 	def x(self):
# 		print('deleted x')
# 		self.x_log_.append(datetime.now())
# 		del self._x

# 	def x_log(self):
# 		print ('x was accessed at these times:')
# 		for time in self.x_log_:
# 			print (time)


# generic_object = GenericClass()

# generic_object.x = 4

# generic_object.x_log()

















##################################
##	Eval and Exec 	##############
##################################


# Eval and exec are special functions that translate strings into
# python code.

# you can even use it to create new variables.
# This can give you a ton of flexibility, but be careful.

# if handled badly, it allows users to run their own code inside of your code.


# eval('print(5+10)')

# print(eval ('"test".upper()'))

# # eval cant do for loops, if statements ect. exec can

# exec('if True:print("test")')

# exec('a =10')

# print(a)

# #These are pretty advanced, you probably won't use them much.




# Here is a cool example though

my_string = 'test'

functions = ['.upper','.title','.lower','.casefold']

for function in functions:
	print (eval(f'my_string{function}()'))



