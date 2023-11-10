#############################################
##	Asteroid Shooter w/o classes	#########
#############################################

#	Classes are new to me, so for the first time we make asteroid shooter,
# 	we will be focusing on learning the tools for pygame.

#	The second time, we will make it with classes.


#########################
#	How do games work?
#########################
#
#		How films work:
#
#			Any film is just a collection of images played quickly in sequence.
#			played fast enough, they blend into a consistent viewing experience
#
#
#		Video games work in basically the same way.
#
#			The only difference is that each image is dynamically generated as you go along.
#
#			1. Get player input and check for any kind of change.
#
#			2. We use input to move the player character and update all other elements
#
#			3. All individual images are combined (player image, enemy image, ui graphics)
#
#			4. The final frame is shown to the player
#
#		This is all one loop. We keep running the loop over and over again.
#		This loop is run 30 times in a second to make 30 frams per second.
#		
#
#	What does Pygame do in this process?
#
#		Not all that much. Pygame is ultimately a fairly simple module.
#		The key features are: 
#
#		displaying graphics, playing sounds, and getting user input, and
#		checking collisons, and some other minor tools like repeated timers and image
#		manipulation
#
#		We have to create all the game logic ourselves. If you can get through this you are
#		going to be a compitent programmer
#
#		We are also expanding Pygame for this course, using a level editor.
#
#
#
#
#
#
#
#
#
##############################################
#	Creating a new blank window		##########
##############################################
#
#	Display surface: 
#		the image that the player sees at the end of every game loop
#		Any other graphics (player, enemies, background, text) will be placed on this.
#		There can only be a single display surface and any image not on it will not be
#		shown,
#	
#	Creating a display surface:
#		first import pygame.

# import pygame, sys

#		then run pygame.init()

# pygame.init()

# 		display surface should be a seperate variable because we use it a lot.
#		window height and with are usually stored in seperate variables.
#

# WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
# display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

# pygame.display.set_caption('Asteroid Shooter (no class but still badass)')

#		Right now there is no loop, the display surface is only generated for a single frame.
#		
#		To fix this, we need a while true loop.
#		it keeps the game running for ever.
#
#		DO NOT RUN THE CODE UNTIL CLEARCODE TELLS YOU
#		with something like pass, the while true loop will run forever with no way to close it out.
#
#	3 things need to be established in the loop before we can run it.
#

# while True:

#	1. input
#			in pygame, inputs are called events (mouse click, mouse movement, touch screen ect.)

	# for event in pygame.event.get(): # <--- A [list] of inputs that the player sends to python. could be anything.
	# 	if event.type == pygame.QUIT:# <--- This QUIT is the input python gets from pressing the x in the top of the window
	# 		pygame.quit() # <--- function that closes the entire game. Breaks the loop.
	# 		sys.exit()


#		2. updates
#			nothing to put in here yet

#		3. show the frame to the player. (update the display surface)
	
#	pygame.display.update() # <--- takes anything we got from the updates secton and puts it on the display surface.

#	Just running code to here throws an error when we quit the window. To fix that, import sys use sys.exit() function.
#	it ends any kind of code you are currently running. It will not read anything after that point. So i will out
#	it below pygame.quit()
#
#
#
# 	Exercise: look through methods on https://www.pygame.org/docs/ref/display.html?highlight=display
#		and find one method that changes the title of the window.
#
#
#
#####################
#	Adding images	#
#####################
#
#	Surface vs Display surface
#		To add image, we need to a surface. This =/= display surface
#		
#		Display Surface
#			The main canvas. There is only a single display surface
#			It will always be shown
#
#		Surface
#			Basically an image. 
#			There can be unlimited surfaces
#			A surface will only be visibil if it is on the display
#	
#
#	3 ways to create a surface:
#
#		importing an image(png,jpeg)
#
#		creating one in pygame
#
#		creating text
#
#
#
#	Making a surface in pygame
#
#		pygame.Surface((w,h))
#
#		we need to attach the surface to the display surface.
#		and we need to make it... actually look like something.		
#		both display surface and the surface we just made are black
#
#		Surfaces are placed in the display surface with the blit method
#		(stands for black image transfer)
#
#			display_surface.blit(surface,(x,y))
#
#		The position always places the top left of the surface
#
#
#	Color in pygame
#		
#		pygame has a lot of inbuilt color options, but you can also
#		specify your own with rbg tuples (red,green,blue)
#
#		range for each item in tuple is 0-255.
#
#		(255,0,0) would be pure red
#
#		To get started we will just use inbuilt colors.
#		We will put them in the update loop
#

#		default colors availabe in python can be found in the python documentation
#		example:
#			display_surface.fill(red)
#
#		For a list of named colors you can use in pygame:
#			https://www.pygame.org/docs/ref/color_list.html?highlight=named%20colors
#
#
#########################
#	Placing elements	#
#########################
#
#	Blit places things @ (0,0) by default.
#		origin point is in the top left here.
#
#	The one thing that is that different is that an increase in y moves down.
#	I suppose that you can think of it like there is an imaginary - sign in front of each
#	y value
#
#
#########################
#	Images and Text		#
#########################
#
#	Images can be imported with pygame.image.load('path')
#
#	image = pygame.image.load('file path')
#
#	You should also convert the image for better performance. Game will run
#	extrememly slowly otherwise.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#