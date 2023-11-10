

#Input two names and their genders. name1 is the parent, and name2 is the child

name1 = 'Elmo'
gender1 = 'man'

name2 = 'Amanda'
gender2 = 'woman'


# Rules for making a story:

#	General
#	------------
#	
#	always begin the story with: print (f"")

#	write story inside the quotation marks. i.e: print (f"your story here")



# 	For parent
#	------------

#	instead of typing their name wirte {name1}

#	instead of writing he/she, write {they1}

#	instead of writing his/hers, write {posessive1}

#	if {they1} of {posessive1} is at the beginnig of a sentence, add .title(). i.e: {they1.title()}


#	For child
#	-------------
#	Use same rules as for parent, except use 2 as a suffix instead of 1. i.e: {name2}, {they2}, ect.


##############################


if gender1 == 'man':
	they1 = 'he'
	parenttype = 'father'
	posessive1 = 'his'

if gender1 == 'woman':
	they1 = 'she'
	parenttype = 'mother'
	posessive1 = 'her'



if gender2 == 'man':
	they2 = 'he'
	childtype = 'son'
	posessive2 = 'his'

if gender2 == 'woman':
	they2 = 'she'
	childtype = 'daughter'
	posessive2 = 'her'

###########################################
#	WRITE STORY HERE

print (f"{name1} is {name2}'s {parenttype}. Therefore {name2} is {posessive1} {childtype}. {they1.title()}\
 takes {name2} out for ice cream once a week. {name2} says {they2} would go every day if {they2} could\
 have it {posessive2} way. But {name1} is secretly putting tiny ammounts of poison in {name2}'s ice\
 cream every time they go out. So it's probably in {name2}'s best interest that {they2} doesn't go get ice cream\
 with {posessive2} {parenttype} every day.\n\n The end\n\n")






