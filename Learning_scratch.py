


#########################
## Program ideas ########
#########################

## Spiderweb building game ###
# based on pezza's cloth simulation https://www.youtube.com/watch?v=KpJzoFzDDMw

# start with nothing as  a spider and build the best spiderweb you can.
# building web costs energy. Bugs fly into your web and you need to catch them, wrap them up,

# and eat them.

# Maybe pure survival, but maybe survival/bridge builder. With different kinds and strengths of webs.
# I imagine that instead of strong load bearing webs, the spider could prop twigs up and web them to the ground at specific angles.
# You could hold sticks together with web joints.

# if you did want special webs, you could make expanding/contracting webs. Maybe a nonsticky web on a little motor thing to lift a bridge?

#Perhapse open world, need to solve puzzles with your web and build webs in unique locations.

# example: you need to put a coin in a vending machine. A coin can fall off the table, but you have to build
# a web that directs the coin into the vending machine.



########################
#	Fun Functions I made
########################



####	QUICK CALC 	####### July 27 2022 ###

# also sums numbers w/out sum() function. I think this
# might be what the sum() function looks like, but I don't know.

# example: calc(1,22,5)

# calc() prints: 'calc = 28'


# def calc(*numbers):
# 	result = 0
# 	for arguments in numbers:
# 		result += arguments

# 	print (f'calc =',result)
# 	if len(numbers) > 1:
# 		print ('total values summed:',len(numbers))






# #### EVEN ODD SORTER ###### July 27 2022 ###

# def even_odd(maxnumb, even_odd = False):
# 	instructions = "Instructions:\n\nTo use even_odd(),\
# enter parameters (max number, 'even')\
# or (max number, 'odd')\n\n\
# example: even_odd(5,'odd')\n\n\
# Additionally, you can leave out the even/odd\n\
# parameter to list both evens and odds."

# 	if maxnumb == 'help':
# 		print (instructions)

# 	else:

# 		listeven = []
# 		listodd = []

# 		counter = 0

# 		while counter <= maxnumb:

# 			counter+=1

# 			if counter > maxnumb:

# 				break

# 			if counter % 2 == 0:
# 				listeven.append(counter)
# 			else:
# 				listodd.append(counter)

# 		if even_odd == 'even': 
# 			print ('evens: ',' '.join(map(str, listeven)))

# 		elif even_odd == 'odd':
# 			print ('odds: ',' '.join(map(str, listodd)))

# 		else:
# 			print ('evens: ',' '.join(map(str, listeven)))
# 			print ('odds: ',' '.join(map(str, listodd)))







##	Lists to dictionary 	######### July 29, 2022 #


# an actually useful function that easily turns two lists into a dictionary

def lists_to_dict(list1,list2):
	zip_ = zip(list1,list2)
	zip_list = list(zip_)
	dictionary = dict(zip_list)
	return dictionary



# example

list_a = ['pink','rat','faces']
list_b = ['key1','key2','key3']

# print (lists_to_dict(list_a,list_b))


dict_a_b = lists_to_dict(list_b,list_a)

print (dict_a_b['key2'])
























##################################
## 	VIDEO SCRATCH STARTS HERE	##
##################################

# test_var1 = 'test 1'
# test_var2 = "test 2"
# print (test_var1)
# print (test_var2)

# print ( 'even not "this was great"') # an escape character is a foreward slash\
# print ('\"\'')








# ####################
# # ESCAPE CHARACTERS
# ####################

# test_var5 = 'Line 1: some text \nLine 2: some more text' # \n creates a linebreak within a single string
# print (test_var5)

# # multiple lines
# test_var6 = '''A comment
# #Write some more text
# #Write on another line'''

# #print (test_var6)


# #using '''preserves line breaks.'''

# tree = '''
# 	xxx
#   xxxxxxx
#   xxxxxxx
#     xxx
#      x
#      x
#      x	'''

# print (tree)

# #print ('copy'*10)
















# ##############################
# How to get values into strings
# ##############################


# name = 'Mikey'
# age = 22
# feeling = 'want to eat'


# greetings_string1 = 'Hello {}, you are {} years old.\n'.format(name,age)


# greetings_string2 = 'Hello {one}, you are {two} years old. And I {three} you'.format(one = name, two = age, three = feeling)

# print (greetings_string1)

# print (greetings_string2)





# name1 = 'Jeff'
# name1gender= 'he'#he/she
# object1 = 'pencil'
# object2 = 'screwdriver'
# animal = 'goat'

# story1 = "{one} was a very good magician. They could make anybody's weenie turn into a {two}. Everey thursday, {one}\
# would go to the mall and buy a {three} for their mom, who {one} knew would use it to its fullest and most unique\
# potential. But last Thursday when {one} was returning from the mall, he was suddenly attacked by a wild {four}. \nAnd they died.\n\n"\
# .format(one = name1, two = object1, three = object2, four = animal)

# print(story1)

# VS

# story2 = f"{name1} was a very good magician. {name1gender} could make anybody's weenie turn into a {object1}. Everey thursday {name1} \
# would go to the mall and buy a {object2} for their mom, who {name1} knew would use it to its fullest and most unique \
# potential. But last Thursday when {name1} was returning from the mall, {name1gender} was suddenly attacked by a wild {animal}. And {name1gender} died.\n\n"

# print (story2)







# #	Input current age, and a number of years from now to see what your age will be.

# age = 24
# years= 45

# ageteller = f'You are currently {age} years old. \nIn {years} years, you will be {age+years} years old.'

# print(ageteller)




















# ##################
# #Lists and tuples
# ##################

# #Start With lists and tuples tomorrow. vid @ about 2:07
# # Lists vs tuples: lists can be changed, tuples cannot!

# mylist = [1,2,'word']
# print (mylist)
# print(len(mylist))
# mylist.reverse()
# print (mylist)
# mylist.reverse()
# print(mylist)

# mylist.append(10)
# print(mylist)

# #tuple

# mytuple = [1,2,3,('list2', 12)]
# print (mytuple) #.reverse(), .append(), ect do not work on tuples.
# lists are used most of the time

# #How to pick elements from a tuple or list: Inexing or slicing
# #lists start at zero. index numbers. [0,1,2,3]

# #index number after a list picks a number in that list.

# list1 = ['A','B','C',(0,1,2)]
# tuple1 = ('Dog','Cat','Gecko',['treefrog','mink',12])

# print(list1[2])

# print(list1[3][2])

# #To get to a specific item on in a list within a list (or a tuple within a list, ect),
# #use index number for the list, and ad another index number immediatley after for the internal list.

# print (tuple1[3][0])

# print (list1[3][2] + tuple1[3][2])

# #print(1+'seahorse') Doesn't work I guess. You can strings, but not strings+intigers.
# #print ('1'+'seahorse') #would work thought

# print (list1[0])
# print (list1[-1]) # use negative index values to go backwards on the list.

# exercise_list = ['first entry', [123,456, [0, 'hello :)']], 'bye']

# print (exercise_list[1][2][1])

# print (tuple1[2:4])









# ########################################
# 3 ways to insert variables into strings
# ########################################


# name0 = 'Mike'			#0
# name1 = 'Jennifer'		#1
# name2 = 'Cucumberbatch'	#2
# name3 = 'Zachary'			#3
# name4 = 'Elvis'			#4

# print (name1, 'is a great dude. He can catch all of the',name2,'s in the forest. And his mom eats', name2, 's, so its a good deal.\n\n','-'*100, '\n')

# print ('{X} is a great dude. He can catch all of the {Y}s in the forest. And his mom eats {Z}s, so its a good deal.\n\n'.format(X = name1, Y = name2, Z = name3),'-'*100, '\n')

# print (f'{name1} is a great dude. He can catch all of the {name2}s in the forest. And his mom eats {name2}s, so its a good deal.\n\n','-'*100, '\n')

# print ('{} is a great dude. He can catch all of the {}s in the forest. And his mom eats {}s, so its a good deal.\n\n'.format('Mike', 'Jennifer', 'Jennifer'),'-'*100, '\n\n')

# list1 = [name0,name1,name2,name3,name4]


# print(list1[0],list1[1])

# print (list1[0:5:2])

# print('o'*50)

# print(list1[0],list1[1],list1[3])






# test_list = [1,2,3,4,5,6,7,8,9,10]
# #Start from 8, go to 2. Pick every second element

# print (test_list[7:0:-2])

# namelist = ['Mike','Jennifer','Franky','Julia','Effy']

# name0,name1,name2,name3,name4 = ['Mike','Jennifer','Franky','Julia','Effy']

# print (name1)

# dictionary = {'key1': 'berb', 'b' : [1,2,3]}
# ###############key#####value key retrieves####

# print (len(dictionary))
# print (list(dictionary)) #Converts dictionary to list. Keys only I guess
# print (tuple(dictionary)) 



# #################################################################
# #Two ways of retrieving things from dictionarys by their keys.
# #################################################################

# dictionary.get('key1') #.get doesn't crash when can't find the key. returns "none"
# # and
# print (dictionary['key1']) #crashes the whole deal if it can't find the key



# #Adding things to dictionaries. 3 Ways

# dictionary.update({'key2' : 'KLAMPS'}) # You can add a new key/value pair with the .update method. .update({key:value})
# # here is another way
# dictionary.update(key3 = 'butts', key4 = 'boobs')
# # and one more way
# dictionary['key5'] = 'Vagana'

# print (dictionary)







# #######
# Sets
# #######

# 	looks like dictionaries, but only have values. No keys.
# 	Each value inside a set must be unique, duplicates deleted.

# set = {1,1,1,2,3,4,4,2,1,3,4}
# print(set)

# print(len(set)) #has only 4 unique values. Returns 4

# #adding and removing values from sets
# set.add(5)
# print(set)

# set.remove(5)
# print(set)

# #indexing and slicing does not work in sets.
# # set[1:2:1] would cause a crash

# #Retrieving values from set: pop method
# # .pop takes the first item out of the set. The purpose of sets isn't really to retrieve stuff I guess.

# #exercise: take set, get a value from it by index. Going to get 4.

# print (list(set)[3]) #set remains a set. We change the data type for one specific purpose.





# What sets are actually for: Comparison operators.

# Comparison Operators

# set1 = {1,2,3,4,4}

# set2 = {4,5,6,7}

# #.union() merges the two sets together

# print (set1.union(set2)) # OR print (set1 | set2)


# and .intersection() tells you which values are teh same between the sets.

# print (set1.intersection(set2)) # OR print (set1 & set2)


# # .difference() retrieves only the values that are not shared between the two sets.

# print (set1.difference(set2)) # OR print (set1 - set2)



# exercise: seeing if a list has duplicate values

# list1 = [1,1,2,3,4]

# print (len(list1)) # returns 5

# print (len(set(list1))) # returns 4

# # if length of set is shorter than list, there must be duplicates in the list.

# #fancier way

# print(len(list1) == len(set(list1))) # if false, there are duplicates because the comparrison operator gives back two different values

















# ############################
# Booleans###################
# ############################

# comparison operators.
# == 'is equal', checks if two numbers are the same 
# != 'not equal', checks of two numbers are different
# <, <= , checks if a number is smaller than another
# >, >=, checks if number is bigger than another
# not reverses any boolean

# print (1 == 1) #returns true
# print (1 != 10) #returns true

# print (1 == 10) #returns false
# print (1 != 1) #returns false

# print (1 == 1) #returns true
# print (1 != 10) #returns true

# print (1 == 10) #returns false
# print (1 != 1) #returns false

# print (10 <= 10) #returns true
# print (10 < 10) #returns false




# # Booleans and lists and stringss

# print (1 in [1,2,3]) # returns true (is 1 in this list?)
# print ('e' not in 'hello') # returns false




# #data conversion exercise

# #check if key 1 exists, check if value 4 exists in dictionary

# e_dict = {1:'one',2:'two',3:'three',4: 'four'}

# print (1 in e_dict)
# print ('four' in e_dict.values()) #need .values() or else it
# #will only check for 'four' in keys, and always return false.








# ####	Falsy vs Truthy		###########


# Falsy - values that will be converted to false

# 	0 or 0.0 	zero intigers and floats
# 	'' ""		Empty strings
# [], {}, ()	empty lists, tuples, sets, and dictionaries
# 	None		absense of a value



# Truthy - values that will be converted to true
# 	Anything not Falsy will be truthy.


# bool() determines if a value is truthy or falsy
# print(bool(1)) # returns true
# print(bool())  # returns false
# print(bool(0)) # returns false

# print(bool({1:0,2:'four'})) # checks the list for values and returns 'true'
# print(not bool({1:0,2:'five'})) # checks if it is not truthy. Since it is truthy, it returns false.
# print(not bool({})) # prints true

# print(bool(None)) # None is a data type. It is falsy. prints false



# ##		Other Data Types		####

# These are most of the data types you will be seeing.
# These Functions allow you to interconvert between them.

# ##	Freuently Used###

# 	Know these well!

# 	int()
	
# 	float()

# 	str()

# 	bool()

# 	list()

# 	dict()

# 	tuple()

# 	set()



# ##	Infrequently Used ###

# 	None- Absence of a value

# 	Sequence - To get a range of numbers

# 	Bytes, complex numbers, memoryview, frozensets.
# 	These are more specific types of data that you will
# 	only see in very specific circumstances.

# ##




















# #########################################
# ##	CODE FLOW	##########################
# #########################################


# Python groups chunks of code together by indentation.
# --->Anything that is indented once below an if condition belongs to the if condition.

# Things indented below an if statement only run if the if statement is true.


# If, elif, else - run code if conditions are true
# Match - If statements for more specific values
# While - Repeat code as long as condition is true
# For 0 Run code for every item in a container






# # Simple If statements #############################


# example: run some code if a value in a variable is greater than 10

# x = 11
 
# if x > 10: #think of : as 'then' maybe
# 	print (x,'is greater than 10')

# # if x < 10:
# # 	print (x,'is NOT greater than 10')

# #This bit of code would work, but instead we can use else

# else:
# 	print (x,' is NOT greater than 10')
# #
# # Else statements must always be connected to if statements.

# # elif statements run only if if statement is false, AND some other
# # statement it is dependant on is true.
# # elif statements must come between if and else statements, But you can
# # have as many elif statements as you want


# tells you if one number is larger than another.

# x = 2	# first number
# y = 6	# second number

# if x < y:
# 	print (x, 'is less than', y)

# elif x == y:
# 	print (x, 'equals', y)

# else:
# 	print (x, 'is greater than', y)




# exercise

# money = 14

# if money >= 80:
# 	print ('You can have a fancy dinner')

# elif money > 45:
# 	print ('You can go to a decent resturaunt')

# elif money > 15:
# 	print ('You should probably stay home and make dinner')

# else:
# 	print ('Boil your leather shoes for sustanance')






# ## Complex IF statements #########################

# Combining condions: And+or

# And : all parts must be true

# or : either condition could be true

# if True and True and True:
# 	print ('true')



# x=30
# if x>=10 and x<=20 or x == 30:
# 	print (f'{x} is between 10 and 20 (or {x} = 30)')

# elif x < 10:
# 	print (f'{x} is less than 10')

# else:
# 	print (f'{x} is greater than 20')


# #excersise###
# money = 100
# hungry = False
# bored = False

# if money >= 80 and hungry == True or bored == True:
# 	print ('eat something fancy')
# else:
# 	print ('eat in')





# Nesting if statements #

# x = 'z'

# if x in ['a','b','1']:
# 	print (x,'is in the list')
# 	if x.isalpha():
# 		print ('and it is a letter')
# 	else:
# 		print (x, 'is not a letter')
# else:
# 	print (x,'is not in list')


# exercise##

# money = 8
# hungry = False
# bored = False

# if money >= 80:
# 	print ('I have enough money')
# 	if hungry:
# 		print ('and I am Hungry')
# 		if bored:
# 			print ('I will eat out')
# 	else:
# 		print ('Im not hungry but Im bored. I will eat out.')
# else:
# 	print ('I wont eat out. I dont have enough money.')
# 	if hungry:
# 		print ('I guess I will eat in')






















###################################
#	Match Case Statement       ####
###################################

# Similar to if staements (you run code if condition is true)

# Difference is that match case is better to check for one value out of a long list
# of possible values



# Here is an example...

# With IF statements

#	if 'hungry'
#		run code
#	elif 'tired'
#		run another code
#	elif 'bored'
#		run some other code


#This kind of thing can be done more efficiently with Match case
#(really just more readable)

# mood = 'Bob'

# match mood:
# 	case 'hungry':
# 		print ('im hungry')
# 	case 'sad':
# 		print ('im sad')
# 	case _:
# 		print ('case _ is like else')

#Not really much different than elif, but definetly more readable



# exercise
#
# create a variable with an integer between 1 and 5, call it grade
# create a match case statement that writes 'very good' when grade is 1
# and very bad when grade is 5 (and all other cases in between)
# there should also be some default behavior if you get an unexpected value


# grade = 5	#1-5

# match grade:
# 	case 1:
# 		print ('very good')
# 	case 2:
# 		print ('decent')
# 	case 3:
# 		print ('fair')
# 	case 4:
# 		print ('poor')	
# 	case 5:
# 		print ('very bad')
# 	case _:
# 		print ('grade not in range 1-5')	

# if grade == 1:
# 	print ('very good')
# elif grade == 2:
# 	print ('decent')
# elif grade == 3:
# 	print ('fair')
# elif grade == 4:
# 	print ('poor')
# elif grade == 5:
# 	print ('very bad')
# else:
# 	print ('grade not in range 1-5')

# # Match case does the same thing, but is much more readable
# # if match does not find a value, you don't get an error. Just doesn't run.


























##########################
## 	While Loops	##########
##########################

#	

# x = 0

# while x < 1000:
# 	x += 1
# 	print ('This is being printed 1000 times')


# Now can only run 10 times. (DO NOT DO THIS without putting a stopper on it!
# I nearly crashed the program when I made an infinite loop like this. Remember that it can
# print thousands of times in 55 milliseconds)

# x = 0

# while x < 10:
# 	x += 1
# 	print (x)

# 	if x == 10:
# 		print ('tadaaa')


# # prints numbers from 1- 1,000,000

# # you can break and skip one iteration of the while loop
	
# 	if x == 9:
# 		break # ends the entire while loop. Cuts off at 9
# 	if x == 3:
# 		continue # skips to the next itteration of the while loop



# You can skip a value in a loop with continue. 
# If you print before continue it doesn't work though

# x = 0
# while x < 10:

# 	x += 1

# 	if x == 5:
# 		continue

# 	print (x)	


# exercise
# use while loop to create a list with only even values
# from 0-100 by creating an empty list first and then appending only even values
# Do not add value 58


# My attempt
# x = 0
# list = [0]

# while len(list) < 50:
# 	x += 1
# 	list.append(x)

# 	if len(list) == 50:
# 		print (list)


# Clear Code's answer

# my_list = []
# counter = 0

# while counter <=100:
# 	if counter % 2 == 0: # if % 2 == 0, we know we are only getting even numbers
# 		if counter != 58:
# 			my_list.append(counter)

# 	counter += 1


# print (my_list)

# Remember that % is the remainder operation.
# to get only odd values, use % 2 != 0 (if remainder when devided by two is different from 0) 
















########################
##	For Loops	########
########################

# For cycles overy every item in the container and then stores
# the value in in a pseudo variable.

# list = []
# x = 0

# while len(list) < 100:
# 	x += 1
# 	if x % 2 != 0:
# 		list.append (x)

# for item in list:
# 	print (item)



# for dictionaries, to use for on items, you need
# to use .items()
# dict = {1: 'one', 2: 'two', 3: 'three'}

# for keys in dict:
# 	print (keys)

# for values in dict.values():
# 	print (values)

# # to get both keys and values, use .items().
# # displays in tuple form

# for items in dict.items():
# 	print (items)


# this can also be done with strings.
# string = 'one two three'
# for x in string:
# 	print (x)

#This does not work on basic numbers. Intigers cannot be itterated over.
#instead use range function

# number = 10

# for x in range(number):
# 	print (x) # does not include 10

#range works kinda like slicing
#print(range(start,end,step))

# for x in range (10,21,1):
# 	print (x)

# for x in range (1,101,2):
# 	print (x)



#exercise

# practice_list = [[10,40,20,50],[2,42,10],[101,12,4,110]]

# use for loop to only print numbers below 50
# skip values below 10
# end the entire loop if value is above 100

# for nested_list in practice_list:
# 	for item in nested_list:

# 		if item > 100:
# 			break

# 		if item < 50:
# 			if item < 10:
# 				continue

# 		print (item)
			

# The order that the code is written in is very important. If I were to break
# the loop after I printed y, I would have also listed 101, because it would have broken
# on the next iteration after 100
# Now, it breaks before it has a chance to print 101
		








#############################################
#	 Flow and linebreaks, Ternary operators	#
#############################################

# you could just continue writing after the colon. You can even
# use a semicolon to add multiple lines of code.
# It works, It's just not very readable.


# x = 0
# while x < 10: x+=1 ;print (x)

# sometimes it makes more simple sense to have it on the same line

# x = 5

# color = 'blue' if x < 5 else 'red' # Ternary operator. Read it like a sentence
# #"The color" is blue if x is less then five. Otherwise it's red.

# print (color)






# This is much more readable without the line breaks

# grade = 55	#1-5

# match grade:
# 	case 1: print ('very good')
# 	case 2: print ('decent')
# 	case 3: print ('fair')
# 	case 4: print ('poor')	
# 	case 5: print ('very bad')
# 	case _: print ('grade not in range 1-5')


# if grade == 1: print ('very good')
# elif grade == 2: print ('decent')
# elif grade == 3: print ('fair')
# elif grade == 4: print ('poor')
# elif grade == 5: print ('very bad')
# else: print ('grade not in range 1-5')

# Ternary Operator
# x = 9
# color ='red' if x < 5 else 'blue'
# print (color)

# #True value if expression is true, else false.
# # works in a lot of different tools as well, like f strings and lists

# print (f"The color is {'red' if x < 5 else 'blue'}")






















################################################################
##	Functions	################################################
################################################################

# So far we have learned all the most basic parts of programming.
# Like a car, we have nuts and bolts and screws. We need to use them to make
# more complex systems (control system (steering wheel)), breaks, ect
# and combine these more complex systems to make a final product
# like a car


# In this analogy, a function is one of these more complex systems to build a complete car.
# Writing our own functions, I guess!


# A function is simply a block of code that can be reused.

# Steps for functions

#	1) Create function (where code is added)

#	2) Call the function (execuding code inside function)

# def = define

# def test_function():
# 	#any code within this indentation belongs to this funciton

# 	print('hello')
# 	test = 1+2
# 	print (test)


# test_function() # every time you add brackets behind name of function
# # you are calling it.

# test_function()

# brackets are for parameters. parameters are essentially variables that
# can only be used inside the function

# def calculator(num1,num2):
# 	result = num1 + num2
# 	print(result)

# x = 1
# y = 2

# calculator(x,y)


# exercise give the calculator an operation. + and minus operations
#
# def better_calculator(num1,fcn,num2):
# 	if fcn == '-':
# 		result = num1 - num2
# 	if fcn == '+':
# 		result = num1 + num2
# 	if fcn == '/':
# 		result = num1 / num2
# 	if fcn == '*':
# 		result = num1 * num2
# 	if fcn != '-' and fcn !='+' and fcn !='/' and fcn !='*':
# 		print ('error. use +,-,/, or *','\n'*80)

# 	print (f'{num1} {fcn} {num2} = {result}')


# better_calculator(3,'+',1)
	























##############################
## Functions and parameters	##
##############################

#	when a function is created we can set parameters (the things we put in the brackets)
#	parameters are like variables inside of the function
#	'slotform argument'
#	 arguments are assigned to parameters by their positions
#
#	but 'keyword arguments' can also be used.

# def test_function(arg1,arg2,arg3,arg4):
# 	print(arg1)
# 	print(arg2)
# 	print(arg3)
# 	print(arg4)

# test_function(1,'hello',True,'test')

# VS

# test_function(arg3 = True, arg1 = 1, arg4 = 'test', arg2 = 'hello')
# ###here we get the exact same result, except we didn't need to keep track of positions

# # This can also be done in a slightly cleaner format like so

# test_function(
# 	arg1 = 1,
# 	arg2 = 'hello',	#<---- don't forget these commas
# 	arg3 = True,
# 	arg4 = 'test')

# # positional arguments always have to come keyword arguments.
# test_function (1,'pippy',arg3 = 'benny',arg4 = ['zippo','frank'])
# #-------------^arg1--^arg2------


#default arguments can be added to the function, so you don't always have to keep adding them

# def test_function(arg1,arg2,arg3,arg4 = 'default argument 4'):
# 	print(arg1)
# 	print(arg2)
# 	print(arg3)
# 	print(arg4)

# test_function (1,'pippy',arg3 = 'benny')

# # but the default argument can be replaced

# test_function (1,'pippy',arg3 = 'benny',arg4="My landlord's goddamn dogs keep barking")






#exercise
# create greeter function with 3 arguments: person, greet, and weekday
# person and greet should have default arguments ('person' for person and 'hello' for greet)
# inside of the function use an f-string to print the greet and the person and also prent the weekday
# when calling the function, use at least one positional argument and 1 keyword argument

# def greeter(name = 'person', greeting = 'hello', weekday = 'unknonw weekday'):
# 	print (f"{greeting} {name}. Today is {weekday}.")

# greeter(
# 	'Kyler', 								#<-- position argument
# 	greeting = "Hello Mr. Badass AKA",		#<-- keyword arguments
# 	weekday = 'wednesday')


















#################################
## Parameters and arguments II ##
#################################



###	List Unpacking	######


# You can make functions even if you don't know how many arguments you will need

# Here is the way I did it for my even/odd number sorter (kinda)

# def print_all(arguments):

# 	for argument in arguments:
# 		print (argument)

# print_all(['Hello', 'buttface'])


# # instead we chan just add a star. No list necessary

# def print_all2(*arguments):
# 	for argument in arguments:
# 		print (argument)

# print_all2('Hello', 'Buttface')

# # '*' is the unpacking parameter

# #this is basically automatically converting any arguments you
# #put into the funcition into a tuple and looping through and printing


# def print_all (first, *arguments, extra):

# 	print(first) #prints first parameter

# 	for (argument) in arguments: # loops through *arguments
# 		print (argument)

# 	print (extra) # prints the specified extra (12)

# print_all('first', 1,2,3,4,5, extra = 12)

# #after unpacking parameter, keyword locators must be used



#Keyword unpacking#

#	'**'double star unpacking looks for keyword arguments and packs them
#	inside of a dictionary

# def print_more (**arguments):
# 	print(arguments)

# print_more(arg1 = 'murph', arg2 = 'lenny', arg3 = [1,2,3])


# 	This is appearantly really powerful stuff here
# def print_even_more (*args, **kwargs): #arguments and keyword arguments
# 	print(args)
# 	print(kwargs)

# print_even_more(1,2,3,'hello',True,True, Test = "22", Melt = 'Koopie')





#exercise
#create a calculator function that prints the sum of an unlimited amount of numbers


	# My way (which works perfectly fine)
# def calc(*numbers):
# 	result = 0
# 	for arguments in numbers:
# 		result += arguments
# 	print ('calc =',result)

# 
# I'm going to leave this function activated because it's handy

#	Clearcode's way: Uses sum() function (which may look exactly like mine)

# def cccalc(*args):
# 	result = sum(args)
# 	print('cccalc =',result)

# cccalc(1,2,3,3,344,44,4,3,2,12,1,2*100000,.5)





















###########################
## Functions and Scope	###
###########################

# Variables created inside of a function are only
# available inside of that funciton a 'local scope'

# Variables outside of function: 'global scope'



# 

#	The code below does not work because 'a' is a global
#	variable. 'a' inside of function has no value unless
# 	it is assigned within the function. We would need to
#	define a inside the function first

# def test_func():
# 	a += 2
# 	print(a)

# test_func()


# def test_func1():
# 	a = 0
# 	a += 2
# 	print(a)

# test_func1()

# # You can see that a = 10 was completely ignored by
# # test_func. It's only focused on variables within its local scope

# def test_func2(a):
# 	a += 2
# 	print (a)

# test_func2(a)

# # with the parameter we can bring the global value of a = 10
# # into the function. But the variable within the function could be anything

# def test_func3 (anything):
# 	anything += 2
# 	print (anything)

# # test_func3(a)


# # a global variable can be used inside a function so long as you're not trying to change it

# def test_func4():
# 	print(a)


# # Functions can be used inside other functions 

# def test_func5(x):
# 	test_func3(x)



# Functions are supposed to separate from the rest of the code

# Once the code becomes more complex it is really
# easy to run out of variable names

# For example, with the car, both the battery and the tank
# might have a 'capacity' variable

# local scopes inside of a function help to keep things
# organised.





##	Rules of scope 	###

# 1)	Every function has its own local scope and every local scope is separate

# 2)	Global variables can be accessed in the local scope but they can't be created
#		or changed

# 3)	You can move between scopes with paramteters 'global' and 'return'
#		'return is much better, global you generally want to avoid'


# global: make it global. just write global in front of your variable
# to tell python that a does not exist only inside function. It looks for a in
# the global scope. 

# global is not used often. It is bad practice i guess

# a = 10

# def test_func6():
# 	global a
# 	a += 2
# 	print (a)

# test_func6()

# instead do it like i did in test_func, and how test_fcn7()
# will do it. Call the function with the global variable a 
# as a parameter

# def test_fcn7(var):
# 	var += 2
# 	print (var)

# test_fcn7(a)


# to get the value out of a local scope use return.
# activate testfcn8 and then run printa(test_fcn8(a))


# def test_fcn8(var):
# 	var += 2
# 	return var

# print (test_fcn8(a))





### exercise ###

# create 2 global variables called 'multiplier' and has_calculated
# multiplier should have any integer and has_calculated should be set to the boolean False

# then create a function called multiply_calculator that takes one argument and calculates the multpilication
# of that number
# inside of the function multiply the parameter with the global variable multiplier
# store that new number in a variable called result and return it
# print the return value of the function


# multiplier = 5
# has_calculated = False

# def multiply_calculator(var):
# 	global has_calculated
# 	result = multiplier * var
# 	has_calculated = True
# 	return result

# # for some reason, changing the boolean value must
# #come before you return.

# # ^^^^^^^THIS IS BECAUSE RETURN ENDS THE FUNCTION

# #also don't forget to use global in order to call the global variable
# #has_calculated

# print (multiply_calculator(2))
# print(has_calculated)


















#######################
## LAMBDA FUNCTIONS	###
#######################

# lambdas are single line function. Returns automatically

#	lambda para: 

# x = 10

# var = lambda x: x + 1



# simple_calc = lambda a,b: a+b

# print(simple_calc(2,3))

# These aren't very useful to us right now, but some functions want
# other functions as arguments. We wills see this more later I guess

#	the sort funciton can be good to use with lambdas
#	sort(1,3,4,5,9),func()

# 	graphical user interfaces... like buttons use lambas.


##	excersise	###

# create a lambda function that accepts 1 intiger argument
# if intiger is > 5 return hello
# otherwise return bye

# hibye = lambda x: 'hello' if x>5 else 'bye'

# print(hibye(7))














##############################
##	Documenting Functions	##
##############################

# Functions get super complicated and you will probably forget
# how they work. It will be even worse for someone else that you're working with
# just add explainer text. this is called docstring

# you can also hint at what types of data you expect
#f for the parameters and the return value


# def test(a,b):
# 	'''docstring. You can write whatever explains your function the best here'''
# 	print (a)
# 	print (b)

# test (1,2)
# print (test.__doc__)


# print(map.__doc__)




# just trying and failing to figure out the map function

# numbers = [0,1,2]

# result = map(lambda x: x+2 ,numbers)
# print (list(result))






















#################################################################
## Advanced data operators	#####################################
#################################################################

# This section covers more advanced ways to loop over data
# covers sorting data
# list comprehension
# data handling







##################################################
## Manipulating lists for stronger for loops	##
##################################################

# 	Super powerful. In python you often want to merge lists and loop over the result.
#	For this we use the zip function

#	xips lists together and gives each list an index inside the loop




# inventory_names = ['screws','wheels','metal parts', 'rubber bits', 'wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]

# currently we can only use for loops for each list. But we can't easily put them together.
# we want to assign 43 to 'screws', 12 to 'wheels', '95' to metal parts and so on.
# we can do this with zip()

# note: I think I kinda did this or something similar when i was messing around with the map funciton earlier


#zip is a data type and must be converted into something readable

# print(list(zip(inventory_names,inventory_numbers)))

# alternatively

# for things in zip(inventory_names,inventory_numbers):
# 	print(things)

# you could use index to get some specific things from this

# for things in zip(inventory_names,inventory_numbers):
# 	print(things[0]) # 0 would give you items, 1 would give you number
# 	print(things[1])



# for zip, if you provide two variables to a for loop, items from the first
# list will be stored in the first variable and items from the second list will be
# stored in the second
# for name, number in zip(inventory_names,inventory_numbers):
# 	print(f'{name} {number}')
	

#enumerate function: used to get the current index inside of the for loop

# print(list(enumerate(inventory_names)))

# for thing in enumerate(inventory_names):
# 	print(thing)

# for index, name in enumerate(inventory_names):
# 	print(f'{index} : {name}')
# 	if index == len(inventory_names) // 2:
# 		print ('half way done...')
# 	if index == len(inventory_names) - 1:
# 		print ('complete')




# exercise #

# combine zip and enumerate to get 'screws [id:0} - inventory: 43'
# This was really tough for me. it stumped me. Going to need pracitce for sure

# inventory_names = ['screws','wheels','metal parts', 'rubber bits', 'wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]


# for index, inventory_tuple in enumerate(zip(inventory_names,inventory_numbers)):
# 	print (f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}')


# I definetly tried to overcomplicate it. The point is that zip creates tuples, each with 2 values. You can
# access those with an index number. One value from each list.

#enumerate does the same thing, except for only one list. it creates touples with the index number and the value from the list.

# you can nest enumerate functions within zip functions and vise versa.






# combine zip and enumerate to get 'screws [id:0} - inventory: 43'
# This was really tough for me. it stumped me. Going to need pracitce for sure

# inventory_names = ['screws','wheels','metal parts', 'rubber bits', 'wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]


# for index, inventory_info in enumerate(zip(inventory_names,inventory_numbers)):
# 	item_type = inventory_info[0]
# 	item_quantity = inventory_info[1]
# 	print (f'{item_quantity} {item_type}[id: {index}] in inventory')


## THIS IS A TOUGH CONCEPT AND WILL TAKE LOTS OF PRACTICE##




















##########################
##	List Comprehension	##
##########################




# list comprehension is one of the most powerful tools.

# it's basically creating a list in one line.

# example: You want to create a list with the numbers from 0 to 99

#how i would do it with my current knowledge
# my_list = []
# for num in range(0,100):
# 	my_list.append(num)

# #how it can be done with list comprehension

# my_list = [num for num in range(0,100)]

# print(my_list)


# my_list = [x for x in range(0,22) if x % 2 == 0]

# # the first variable x basically just allows the code to append x
# # to the list you are assigning it to

# print (my_list)


# the middle line is basically the same. Just no colon. The value we 
# return to the list is the first value inside the list.
# The first word in the comprehension list is the equivalant of putting list.append(var) after your
# for thing.

# you can modify the first word in the comprehension list like so:

# my_list = [x*3 for x in range(0,10)]

# print (my_list)

# my_list2 = [(x,x+1,x+2) for x in range(0,10)]

# print(my_list2)



# this is the most basic type of list comprehension you can do.
# to make it even more powerful, combine it with a ternary operator (like I already tried above)
# unfortunately else does not work with the for loops. 

# it does work in if/else
#example

# ##if
# my_list = [x for x in range(0,22) if x % 2 == 0]

# ##else

# my_list2 = [x if x < 10 else 0 for x in range (0,100)]

# print(my_list2)


# this can be used to filter other lists



































