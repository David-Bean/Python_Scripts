# 2048 game
# run this file from terminal to play
# To do: make sure a new 2 is generated with each swipe. insert it at a random 0 on the board each time

import random,time

def list_to_board(list_):
    row1 = list_[0:4]
    row2 = list_[4:8]
    row3 = list_[8:12]
    row4 = list_[12:16]
    board = [row1,row2,row3,row4]
    return board

def populate_board():
	new_board = []
	count = 0
	while len(new_board) < 16:
		if random.randint(0,100) < 10 and count < 2:
			new_board.append(2)
			count += 1
		else:
			new_board.append(0)
	return new_board

def build_new_board():
	new_board = populate_board()
	# print(new_board)
	while new_board.count(2) != 2:
		new_board = populate_board()
	# There is an infinitely small chance that this function keeps generating boards with 1 or 0 2s
	# in a forever loop :D
	return new_board


def buildboard(raw_board):

	row1 = []
	row2 = []
	row3 = []
	row4 = []

	counter = 0

	for num in raw_board:
		if counter in range(0,4):
			row1.append(num)
			counter += 1
		elif counter in range(4,8):
			row2.append(num)
			counter += 1
		elif counter in range(8,12):
			row3.append(num)
			counter += 1
		elif counter in range(12,16):
			row4.append(num)
			counter += 1

	gameboard = [row1,row2,row3,row4]

	return gameboard



# prow = [2,0,6,6]

#left [4,4,8,0]
#left [8,0,8,0]
#left [8,8,0,0]
#left [16,0,0,0]

# I need to make it so that if a number to the left is the same as that number, add them together,
# replace the new number with the added number, and replace what ever non zero number was to the right
# with the second number. Ignoring zeroes. any zeros will be sent to the end of the list.
# I also need to make sure that this happens for every pair of same numbers in the line.


def left_shift(prow):
	prow2 = []
	for num in prow:
		if num != 0:
			prow2.append(num)

	while len(prow2) < 4:
		prow2.append(0)

	return prow2


def right_shift(prow):
	prow2 = []
	for num in prow:
		if num != 0:
			prow2.append(num)

	while len(prow2) < 4:
		prow2.insert(0,0)

	return prow2




def add(prow2):
	prow3 = []
	i = 0
	for num in prow2:
		n = len(prow2)
		if i == (n - 1):
			prow3.append(num)
			break
		if prow2[i] == prow2[i+1]:
			prow3.append(num * 2)
			del prow2[i+1]
			prow3.append(0)
		else:
			prow3.append(num)
		i += 1
	return prow3

def add_inverse(prow2):
	prow2r = prow2
	prow2r.reverse()
	prow3 = []
	i = 0
	for num in prow2r:
		n = len(prow2r)
		if i == (n-1):
			prow3.append(num)
			break
		if prow2r[i] == prow2r[i+1]:
			prow3.append(num*2)
			del prow2r[i+1]
			prow3.append(0)
		else:
			prow3.append(num)
		i += 1
	prow3.reverse()
	return prow3

def left_swipe(x):
	y = left_shift(add(left_shift(x)))
	return y

def right_swipe(w):
	x = right_shift(w)
	y = add_inverse(x)
	z = right_shift(y)
	return z

def row_columns(board):
	columns = []
	i = 0
	while i in range(0,4):
		new_column = []
		for row in board:
			new_column.append(row[i])
		i += 1
		columns.append(new_column)
	return columns

def up_swipe_board(board):
	columns = row_columns(board)
	swipedboard = left_swipe_board(columns)
	new_board = row_columns(swipedboard)
	return (new_board)

def down_swipe_board(board):
	columns = row_columns(board)
	swipedboard = right_swipe_board(columns)
	new_board = row_columns(swipedboard)
	return (new_board)

def left_swipe_board(board):
	new_board = []
	for row in board:
		step1 = left_swipe(row)
		new_board.append(step1)
	return new_board

def right_swipe_board(board):
	new_board = []
	for row in board:
		step1 = right_swipe(row)
		new_board.append(step1)
	return new_board

def rand_add(x_board):
    y_board = []
    for row in x_board:
        for num in row:
            chance = random.randint(0,100)
            if num != 0:
                y_board.append(num)
            else:
                if chance < 5:
                    y_board.append(2)
                else:
                    y_board.append(0)
    return(y_board)

def move(old_board):
	print('type: "left", "right", "up", or "down"\nnote: sometimes a new 2 doesnt populate. Try swiping again')
	# NEED TO FIX THE 2 PROBLEM
	time.sleep(.25)
	move = input('\nswipe direction: ')
	if move == 'up':
		new_board = up_swipe_board(old_board)
	elif move == 'down':
		new_board = down_swipe_board(old_board)
	elif move == 'left':
		new_board = left_swipe_board(old_board)
	elif move == 'right':
		new_board = right_swipe_board(old_board)
	else:
		print('invalid input')
		return(old_board)

	rando_board = rand_add(new_board)
	final_board = buildboard(rando_board)

	print('\n')
	print_board(final_board)
	return(final_board)

def print_board(board):
	for row in board:
		print(row)

def main():

	move_count = 0
	raw_board = build_new_board()
	start_board = buildboard(raw_board)
	print(f'\n\n\n\n\nStarting Board:\n')
	print_board(start_board)
	# print('type: "left", "right", "up", or "down"\n\n note: sometimes a new 2 doesnt populate. Try swiping again')

	while move_count < 100000000000000000:
		print(f'\nmoves:{move_count}')
		if move_count == 0:
			poop = move(start_board)			
		else:
			poop = move(poop)
		move_count += 1

main()
















# list.insert(index, value) # At index, insert value.
# list.remove(value) # Remove first instance of value.


#How do I remove an item on a list by index number?
# Use del and specify the index of the element you want to delete:

# >>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> del a[-1]
# >>> a
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Also supports slices:

# >>> del a[2:4]
# >>> a
# [0, 1, 4, 5, 6, 7, 8, 9]


# https://pythontutor.com/render.html#code=def%20buildboard%28raw_board%29%3A%0A%0A%20%20%20%20row1%20%3D%20%5B%5D%0A%20%20%20%20row2%20%3D%20%5B%5D%0A%20%20%20%20row3%20%3D%20%5B%5D%0A%20%20%20%20row4%20%3D%20%5B%5D%0A%0A%20%20%20%20counter%20%3D%200%0A%0A%20%20%20%20for%20num%20in%20raw_board%3A%0A%20%20%20%20%20%20%20%20if%20counter%20in%20range%280,4%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20row1.append%28num%29%0A%20%20%20%20%20%20%20%20%20%20%20%20counter%20%2B%3D%201%0A%20%20%20%20%20%20%20%20elif%20counter%20in%20range%284,8%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20row2.append%28num%29%0A%20%20%20%20%20%20%20%20%20%20%20%20counter%20%2B%3D%201%0A%20%20%20%20%20%20%20%20elif%20counter%20in%20range%288,12%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20row3.append%28num%29%0A%20%20%20%20%20%20%20%20%20%20%20%20counter%20%2B%3D%201%0A%20%20%20%20%20%20%20%20elif%20counter%20in%20range%2812,16%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20row4.append%28num%29%0A%20%20%20%20%20%20%20%20%20%20%20%20counter%20%2B%3D%201%0A%0A%20%20%20%20gameboard%20%3D%20%5Brow1,row2,row3,row4%5D%0A%0A%20%20%20%20return%20gameboard%0A%0A%0A%0Adef%20right_shift%28prow%29%3A%0A%20%20%20%20prow2%20%3D%20%5B%5D%0A%20%20%20%20for%20num%20in%20prow%3A%0A%20%20%20%20%20%20%20%20if%20num%20!%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20prow2.append%28num%29%0A%0A%20%20%20%20while%20len%28prow2%29%20%3C%204%3A%0A%20%20%20%20%20%20%20%20prow2.insert%280,0%29%0A%0A%20%20%20%20return%20prow2%0A%0A%0A%0Adef%20add_inverse%28prow2%29%3A%0A%0A%20%20%20%20prow2r%20%3D%20prow2%0A%20%20%20%20prow2r.reverse%28%29%0A%20%20%20%20print%28prow2r%29%0A%0A%20%20%20%20prow3%20%3D%20%5B%5D%0A%20%20%20%20i%20%3D%200%0A%0A%20%20%20%20for%20num%20in%20prow2r%3A%0A%0A%20%20%20%20%20%20%20%20n%20%3D%20len%28prow2r%29%0A%0A%20%20%20%20%20%20%20%20if%20i%20%3D%3D%20%28n-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20prow3.append%28num%29%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%0A%20%20%20%20%20%20%20%20if%20prow2r%5Bi%5D%20%3D%3D%20prow2r%5Bi%2B1%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20prow3.append%28num*2%29%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20prow2r%5Bi%2B1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20prow3.append%280%29%0A%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20prow3.append%28num%29%0A%0A%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%0A%20%20%20%20prow3.reverse%28%29%0A%20%20%20%20return%20prow3%0A%0A%0A%0A%0Adef%20right_swipe%28w%29%3A%0A%0A%20%20%20%20x%20%3D%20right_shift%28w%29%0A%20%20%20%20y%20%3D%20add_inverse%28x%29%0A%20%20%20%20z%20%3D%20right_shift%28y%29%0A%20%20%20%20return%20z%0A%0A%0A%0A%0Adef%20row_columns%28board%29%3A%0A%0A%20%20%20%20columns%20%3D%20%5B%5D%0A%0A%20%20%20%20i%20%3D%200%0A%0A%0A%20%20%20%20while%20i%20in%20range%280,4%29%3A%0A%0A%20%20%20%20%20%20%20%20new_column%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20for%20row%20in%20board%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20new_column.append%28row%5Bi%5D%29%0A%0A%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%0A%20%20%20%20%20%20%20%20columns.append%28new_column%29%0A%0A%0A%0A%20%20%20%20return%20columns%0A%0A%0A%0A%0Adef%20down_swipe_board%28board%29%3A%0A%0A%20%20%20%20columns%20%3D%20row_columns%28board%29%0A%20%20%20%20swipedboard%20%3D%20right_swipe_board%28columns%29%0A%20%20%20%20new_board%20%3D%20row_columns%28swipedboard%29%0A%0A%20%20%20%20return%20%28new_board%29%0A%0A%0A%0A%0Adef%20right_swipe_board%28board%29%3A%0A%20%20%20%20new_board%20%3D%20%5B%5D%0A%20%20%20%20for%20row%20in%20board%3A%0A%20%20%20%20%20%20%20%20step1%20%3D%20right_swipe%28row%29%0A%20%20%20%20%20%20%20%20new_board.append%28step1%29%0A%20%20%20%20return%20new_board%0A%0A%0A%0Adef%20move%28old_board%29%3A%0A%20%20%20%20move%20%3D%20input%28'%5Cnswipe%20direction%3A%20'%29%0A%20%20%20%20if%20move%20%3D%3D%20'up'%3A%0A%20%20%20%20%20%20%20%20new_board%20%3D%20up_swipe_board%28old_board%29%0A%20%20%20%20elif%20move%20%3D%3D%20'down'%3A%0A%20%20%20%20%20%20%20%20new_board%20%3D%20down_swipe_board%28old_board%29%0A%20%20%20%20elif%20move%20%3D%3D%20'left'%3A%0A%20%20%20%20%20%20%20%20new_board%20%3D%20left_swipe_board%28old_board%29%0A%20%20%20%20elif%20move%20%3D%3D%20'right'%3A%0A%20%20%20%20%20%20%20%20new_board%20%3D%20right_swipe_board%28old_board%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28'invalid%20input.%20up%20right%20left%20down'%29%0A%20%20%20%20%0A%0A%20%20%20%20print%28'%5Cn'%29%0A%20%20%20%20print_board%28new_board%29%0A%20%20%20%20return%28new_board%29%0A%0Adef%20print_board%28board%29%3A%0A%20%20%20%20for%20row%20in%20board%3A%0A%20%20%20%20%20%20%20%20print%28row%29%0A%0A%0A%23%20Main%0Adef%20main%28%29%3A%0A%0A%20%20%20%20move_count%20%3D%200%0A%0A%20%20%20%20raw_board%20%3D%20%5B2,2,2,8,0,4,0,4,8,2,0,4,2,0,2,0%5D%0A%20%20%20%20start_board%20%3D%20buildboard%28raw_board%29%0A%20%20%20%20print%28f'%5Cn%5Cn%5Cn%20Starting%20Board%3A%5Cn'%29%0A%20%20%20%20print_board%28start_board%29%0A%0A%0A%20%20%20%20while%20move_count%20%3C%20100%3A%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20print%28f'%5Cn%20moves%3A%7Bmove_count%7D'%29%0A%0A%20%20%20%20%20%20%20%20if%20move_count%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20poop%20%3D%20move%28start_board%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20poop%20%3D%20move%28poop%29%0A%0A%20%20%20%20%20%20%20%20move_count%20%2B%3D%201%0A%0A%0Amain%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false