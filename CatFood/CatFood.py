# from random import randrange

# def getname():
# 	with open('FoodNames.txt') as file:
# 		bank = file.readlines()
# 	return bank[randrange(len(bank))].title().rstrip()

# def main():
# 	print(f"\nYour cat's name is officially: {getname()}")

# if __name__ == '__main__':
# 	main() 


# for i in range(10000):
# 	main()

# 759 744 751 757 753






# from random import randrange
# with open('Foodnames.txt') as file:
# 	bank = file.readlines()
# 	for i in range(10000):
# 		print(f"\nYour cat's name is officially: {bank[randrange(len(bank))].title().rstrip()}")
# # 129 133 130 129 126


# from random import randrange
# with open('Foodnames.txt') as file:
# 	bank = file.readlines()
	
# 	for i in range(10000):
# 		name = bank[randrange(len(bank))].title().rstrip()
# 		print(f"\nYour cat's name is officially: {name}")
# # 127 131 131 128 129


# from random import randrange
# with open('Foodnames.txt') as file:
# 	bank = file.readlines()
	
# 	for i in range(10000):
# 		name = bank[randrange(len(bank))].title().rstrip()
# 		print("Your cat's name is officially:"+name)
# 123 123 123 119 123



# from random import randrange
# with open('Foodnames.txt') as file:
# 	bank = file.readlines()
# 	for i in range(10000):
# 		name = bank[randrange(len(bank))].title().rstrip()
# 		print("\nYour cat's name is officially:"+name)
# # 129 124 130 130 127



# from random import randrange
# file = open('Foodnames.txt')
# bank = file.readlines()
# for i in range(10000):
# 	name = bank[randrange(len(bank))].title().rstrip()
# 	print("\nYour cat's name is officially:"+name)
# file.close()
# # 124 126 128 128 132

from random import randrange
for i in range(10000):
	file = open('Foodnames.txt')
	bank = file.readlines()
	index = randrange(len(bank))
	name = bank[index]
	name = name.title()
	name = name.rstrip()
	print("Your cat's name is: "+name)
	file.close()
	# 748 740 753 759 751
	# 758 752 746 754 748
