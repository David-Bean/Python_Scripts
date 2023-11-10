
# name1 = 'Bob'
# object1 = 'Wagina and Linda'
# object2 = 'cizz saw'
# animal = 'chimpmingo Climbmichael'

# story1 = "{one} was a very good magician. They could make anybody's weenie turn into a {two}. Everey thursday, {one}\
# would go to the mall and buy a {three} for their mom, who {one} knew would use it to its fullest and most unique\
# potential. But last Thursday when {one} was returning from the mall, he was suddenly attacked by a wild {four}. \nAnd they died.\n\n"\
# .format(one = name1, two = object1, three = object2, four = animal)

# print(story1)

# #VS

# story2 = f"{name1} was a very good magician. They could make anybody's weenie turn into a {object1}. Everey thursday {name1} \
# would go to the mall and buy a {object2} for their mom, who {name1} knew would use it to its fullest and most unique\
# potential. But last Thursday when {name1} was returning from the mall, he was suddenly attacked by a wild {animal}. And they died.\n\n"

# print (story2)







# #	Input current age, and a number of years from now to see what your age will be.

# age = 23
# years= 1000

# ageteller = f'You are currently {age} years old. \nIn {years} years, you will be {age+years} years old.'

# print(ageteller)




# #Lists and tuples
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


