
name1 = 'David'
object1 = 'Onion'
object2 = 'Book'
animal = 'Narwal'

story1 = "{one} was a very good magician. They could make anybody's weenie turn into a {two}. Everey thursday, {one}\
would go to the mall and buy a {three} for their mom, who {one} knew would use it to its fullest and most unique\
potential. But last Thursday when {one} was returning from the mall, he was suddenly attacked by a wild {four}. \nAnd they died.\n\n"\
.format(one = name1, two = object1, three = object2, four = animal)

print(story1)

#VS

story2 = f"{name1} was a very good magician. They could make anybody's weenie turn into a {object1}. Everey thursday {name1} \
would go to the mall and buy a {object2} for their mom, who {name1} knew would use it to its fullest and most unique\
potential. But last Thursday when {name1} was returning from the mall, he was suddenly attacked by a wild {animal}. And they died.\n\n"

print (story2)





#	Input current age, and a number of years from now to see what your age will be.
age = 23
years= 1000

ageteller = f'You are currently {age} years old. \nIn {years} years, you will be {age+years} years old.'

print(ageteller)





