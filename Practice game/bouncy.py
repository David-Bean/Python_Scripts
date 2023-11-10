import pygame,sys
from time import time

pygame.init()

clock = pygame.time.Clock()
WINDOW_W,WINDOW_H = 1000,700
display = pygame.display.set_mode((WINDOW_W,WINDOW_H))

meter = 4 #  pixels
grav = 9.81
second = 60 # frames
# f_grav = (grav*meter)/second**2







obsticle_list = []

background = pygame.Surface((WINDOW_W,WINDOW_H))
background.fill(('grey'))
display.blit(background,(0,0))


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def place_ob(x_pos,y_pos,o_width,o_height,rotation):
	color = 'black'
	obs = Obsticle(x_pos,y_pos,o_width,o_height,rotation,color)
	obsticle_list.append(obs)

	print (len(obsticle_list))



class Cursor:

	def __init__(self,x_pos,y_pos,o_width,o_height,rotation,color):

		self.x_pos = x_pos
		self.y_pos = y_pos
		self.o_width = o_width
		self.o_height = o_height
		self.rotation = rotation
		self.color = color
		self.rect = pygame.Rect(self.x_pos,self.y_pos,self.o_width,self.o_height)

		self.center_x = self.rect.center[0]
		self.center_y = self.rect.center[1]

		self.shape = pygame.Surface((self.o_width,self.o_height)).convert_alpha()
		self.shape.fill(color)



	def move(self):

		self.keys = pygame.key.get_pressed()

		if self.keys[pygame.K_RIGHT]:
			self.x_pos += 4
		if self.keys[pygame.K_LEFT]:
			self.x_pos -= 4
		if self.keys[pygame.K_UP]:
			self.y_pos -= 4
		if self.keys[pygame.K_DOWN]:
			self.y_pos += 4

		if self.keys[pygame.K_z]:
			self.rotation -= 3
		if self.keys[pygame.K_x]:
			self.rotation += 3


		if self.keys[pygame.K_w]:
			if self.o_height <= 500:
			 	self.o_height += 3
		if self.keys[pygame.K_s]:
			if self.o_height >= 10:
				self.o_height -= 3
		if self.keys[pygame.K_a]:
			if self.o_width >= 10:
				self.o_width -= 3
		if self.keys[pygame.K_d]:
			if self.o_width <= 500:
				self.o_width += 3


		if self.keys[pygame.K_SPACE]:
			place_ob(self.x_pos,self.y_pos,self.o_width,self.o_height,self.rotation)


		self.shape = pygame.Surface((self.o_width,self.o_height)).convert_alpha()
		self.shape.fill(self.color)
		self.new_shape = rot_center(self.shape,self.rotation,self.center_x,self.center_y)[0]
		self.new_rect = rot_center(self.shape,self.rotation,self.center_x,self.center_y)[1]
		self.center_x = self.new_rect.center[0]
		self.center_y = self.new_rect.center[1]





class Obsticle:

	def __init__(self,x_pos,y_pos,o_width,o_height,rotation,color):

		self.x_pos = x_pos
		self.y_pos = y_pos
		self.o_width = o_width
		self.o_height = o_height
		self.rotation = rotation
		self.color = color

		self.shape = pygame.Surface((self.o_width,self.o_height)).convert_alpha()
		self.shape.fill(self.color)
		self.new_shape = rot_center(self.shape,self.rotation,self.x_pos,self.y_pos)[0]
		self.new_rect = rot_center(self.shape,self.rotation,self.x_pos,self.y_pos)[1]

class Ball:

	def __init__(self,x_pos,y_pos,o_width,o_height,color):

		self.x_pos = x_pos
		self.y_pos = y_pos
		self.o_width = o_width
		self.o_height = o_height
		self.color = color

		self.shape = pygame.Surface((self.o_width,self.o_height)).convert_alpha()
		self.shape.fill(self.color)
		self.rect = pygame.Rect(self.x_pos,self.y_pos,self.o_width,self.o_height)

		self.v_x = 0
		self.v_y = 0
		
		self.t_init = time()
		self.y_direction = 1


	def physics(self):

		# for obs in obsticle_list:
		# 	if self.

		self.delta_T = time() - self.t_init
		self.a_grav = meter*9.81*self.delta_T
		self.y_pos += self.a_grav

		print (f'y = {self.y_pos} delta_T = {self.delta_T} accel = {self.a_grav}')




def main():


	background = pygame.Surface((WINDOW_W,WINDOW_H))
	background.fill(('beige'))

	cursor = Cursor(0,0,100,50,0,'grey')
	place_ob(-1000,-1000,3,3,0)

	ball = Ball(WINDOW_W/2,WINDOW_H/2,50,50,'purple')
	floor = place_ob(-100,WINDOW_H-14,2000,14,0)


	

	while True:

		# clock_start = time.t

		#events

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				pygame.quit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.quit()
		if keys[pygame.K_r]:
			obsticle_list.clear()
			main()
			



		#updates
		cursor.move()

		display.blit(background,(0,0))
		ball.physics()

		# display.blit(obsticle_list[-1].new_shape,(obsticle_list[-1].x_pos,obsticle_list[-1].y_pos))


		for obsticle in obsticle_list:
			display.blit(obsticle.new_shape,(obsticle.x_pos,obsticle.y_pos))

		display.blit(cursor.new_shape,(cursor.x_pos,cursor.y_pos))
		display.blit(ball.shape,(ball.x_pos,ball.y_pos))

		pygame.display.update()
		clock.tick(60)


print(time())

main = main()
