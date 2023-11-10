
# Zoom:	The graph will be printed from +zoom to -zoom on both x and y axes
# 	tinker with the denominator in the resolution variable to get the graph to fit on your screen appropriately.
#	It Should stay around 30 if the terminal takes up your whole screen.

# 	keep in mind that we are drawing in very low resolution. ideal zoom values are below 100 for non-linear functions.  Although you set zoom as small as you want,
# 	the graph can only zoom in on (0,0). Also, right now it doesn't know exactly where coordinates are. It has a range based on the value of the resolution.
#	at small zoom values, multiple lines can be printed with the x or y coordinate they are close to. You will see a lot of '0' around the origin at small zoom values.

#	for zoom values greater than 6, the coordinates show up best if the value is a multiple of 5.






zoom = 10

def f(x): y = x - (2/x)								;return y

#		      ^ type your function here.
#				you must use '*' as the multiplication symbol

#				in python, instead of using '^', use '**' for exponents.
#				

#				example: f(x) = 2x^2 + 2x + 1    should instead inputed as       f(x): y = 2*x**2 + 2*x + 1






























#----- The code --------------------------------------------------------------------------------




resolution = zoom /30 #30 by default

resmult = 0.58620689655171659415699991

#resmult widens the range that f(x) values can fall into so that more can be printed.
# it basically adds more Xs to the screen for larger zoom values to help combat the lack of pixels.

#resmult = 0.58620689655171659415699991 (a fine tuned value I found to get best results. copy it from here if you
# choose to mess with resmult and want to restore it)



def build_dictionary():

	# This builds a dictionary that will be used later to print a line on the graph.
	# the zoom variable determines the range of key values (which represent x choordinates)
	# that will be added to the dictionary.

	# The resolution determines how far apart each key is from the previous.
	# The ideal ratio of zoom to resolution seems to be about 30 for full screen.
	# the counter variable tells the dictionary which x coordinates will be turned into keys.


	dictionary = {}

	counter = -zoom


	while counter < zoom:

		keyadd = counter + resolution

		dictionary.update({keyadd : ' '})

		# the ' ' above is where you can change what the default (non-graphed) values appear as.


		counter += resolution


	return dictionary







def printer(yrow,yrow_high,yrow_low):


	# This part scans the keys dictionary built earlier.
	# if f(x) (aka y) inside the key is within the range of the y values given by
	# yrow_high and yrow_low, the value at that key is updated to 'X' to show that there is a point
	# on the line nearby.

	dictionary = build_dictionary()

	sidebar_y = round(float(yrow),1)

	round_y = int(repr(sidebar_y)[-1])




	for x in dictionary.keys():


		round_x = repr(round(x,1))

		x_coord = int(abs(round(x,1)))

		y_coord = abs(sidebar_y)
	
		
		
		y = f(x)

		# decides where to put coordinate values on y = 0

		if zoom > 10:

			if -resmult*resolution < x < resmult*resolution:

				if int(round_x[-1]) == 0 and y_coord % 5 == 0 and round_y == 0 :
						dictionary.update({x : int(y_coord)})

				else: dictionary.update({x :'|'})



			if -resmult*yrow_low > 0 < resmult*yrow_high:
			
					if round_y == 0 and x_coord % 5 == 0 and int(round_x[-1]) == 0 :
						dictionary.update({x :x_coord})

					else: dictionary.update({x :'-'})

		else:

			if -resmult*resolution < x < resmult*resolution:

				if int(round_x[-1]) == 0 and round_y == 0 :
						dictionary.update({x : int(y_coord)})

				else: dictionary.update({x :'|'})



			if -resmult*yrow_low > 0 < resmult*yrow_high:
			
					if round_y == 0 and int(round_x[-1]) == 0 :
						dictionary.update({x :x_coord})

					else: dictionary.update({x :'-'})


		# all that code above and below is just for building the side bar and plotting coordinates on y=0 and x=0.
		# the little if statement 'if yrow_high > y > yrow_low:' is the only part that actually plots f(x)
		# onto the screen. If you want the line to be plotted with a symbol or string other than 'X', you can change that here.


		#***** Most important line in the whole function******

		if yrow_high > y > yrow_low:
			dictionary.update({x :'X'})


		


		

	valuelist = list(dictionary.values())



	# This section of the function simply builds the sidebar that displays the y value of each printed line
	# without effecting the spacing. The sign of the y value is determined (+ or -), and then that is printed
	# next to the absolute value of the y value. Otherwise, rows with positive numbers would not be indented
	# correctly.

	# instead of a + or -, 0 gets a space.


	if sidebar_y > 0:
		sidebar_ = '+'

	elif sidebar_y == 0:
		sidebar_ = ' '

	else:
		sidebar_ = '-'

	sidebar = f'{sidebar_}{abs(sidebar_y)}	'


	# This line prints the values in the dictionary as a string. It essentially 'draws' the graph and prints the
	# sidebar

	print (sidebar,' '.join(map(str,valuelist)))







def graph():

	# This is the function that ties everything together.

	# This part is key to drawing the graph. if f(x) is in a range of values determined by
	# the row that is being printed and the resolution, it will flip a value in the dictionary from
	# a space to an X to show that there is a point near that location.

	# It also sets everything else in motion

	yrow = zoom

	while yrow >= -zoom:

                # Here is where I think I woud need to add a line or two that determines slope and changes
                # the gap between yrow_high and yrow_low accordingly. Might not need resmult here in that case.

		yrow_high = yrow + resmult*resolution
		yrow_low = yrow - resmult*resolution

		printer(yrow,yrow_high,yrow_low)

		yrow -= resolution



graph()




