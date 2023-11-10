
def decorator(func):
	def wrapper():
		print('decoration begins...')
		func()
		print('decoration ends.')
	return wrapper

def func():
	print('Function')

# new_func = decorator(func)
# new_func()

func()

# Here we are officially adding new functionality to the function...
# LATER down in the code!
func = decorator(func)
func()

# I am seeing how you could layer in new functionalities as the function is 
# executed down the line...

# We can have really complex code and still check our function without making any
# changes to the code whatsoever