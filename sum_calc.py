
# class Sum:
# 	def __init__(*args):
# 		self.args == args

# 	def add():
# 		sum ([num for num in self.args])

def add(*args):
	sum_ = sum([num for num in args])
	return sum_

# This is a practice file for an exercise

if __name__ == '__main__':
	print ('This cannot be executed from the main file, but it can be executed from sum_calc module')

