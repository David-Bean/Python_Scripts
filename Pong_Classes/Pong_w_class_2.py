import pygame,sys,time,random

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

ball_list = []

class Paddle():

	def __init__(self,side,speed,p_width,p_height):


		self.speed = speed
		self.y_pos = WINDOW_HEIGHT/2
		self.side = side
		self.p_width = p_width
		self.p_height = p_height


		self.surface = pygame.Surface((self.p_width,self.p_height))
		self.surface.fill('white')

		self.ball_list = ball_list

		if self.side == 'left':
			self.x_pos = 10
		if self.side == 'right':
			self.x_pos = WINDOW_WIDTH - self.p_width

		self.hit_box = pygame.Rect((self.x_pos,self.y_pos,self.p_width,self.p_height))


	def move(self):

		keys = pygame.key.get_pressed()
		if self.side == 'left':

			if keys[pygame.K_UP] and self.hit_box.top > 0:
				self.y_pos -= self.speed

			if keys[pygame.K_DOWN] and self.hit_box.bottom < WINDOW_HEIGHT:
				self.y_pos += self.speed

			self.hit_box.update((self.x_pos,self.y_pos,self.p_width,self.p_height))


		if self.side == 'right':

			for ball in ball_list:

				if ball.y_pos < self.y_pos and self.hit_box.top > 0:
					self.y_pos -= self.speed

				if ball.y_pos > self.y_pos and self.hit_box.bottom < WINDOW_HEIGHT:
					self.y_pos += self.speed


			self.hit_box.update((self.x_pos,self.y_pos,self.p_width,self.p_height))

	

class Ball(pygame.sprite.Sprite):

	def __init__(self,x_pos,y_pos,x_direction,y_direction,b_speed,b_width,b_height,b_color,l_paddle,r_paddle,*groups):

		super().__init__(*groups)

		self.b_speed = b_speed
		self.b_width = b_width
		self.b_height = b_height
		self.b_color = b_color

		self.surface = pygame.Surface((self.b_width,self.b_height))
		self.surface.fill(self.b_color)

		self.y_pos = y_pos
		self.x_pos = x_pos

		self.x_direction = x_direction
		self.y_direction = y_direction

		self.hit_box = pygame.Rect(self.x_pos,self.y_pos,self.b_width,self.b_height)
		self.r_paddle = r_paddle
		self.l_paddle = l_paddle


	def collisions(self):

		if self.hit_box.top <= 0:
			self.y_direction = -1
		if self.hit_box.bottom >= WINDOW_HEIGHT:
			self.y_direction = 1


		if self.hit_box.right > WINDOW_WIDTH:
			self.x_direction = -1
		# if self.hit_box.left < 0:
		# 	self.x_direction = 1

		# if self.hit_box.right >= WINDOW_WIDTH:
		# 	main.l_score += 1

		# if self.hit_box.right < 0:
		# 	Main.



		if self.hit_box.colliderect(self.r_paddle.hit_box):


			if self.r_paddle.hit_box.left - self.hit_box.right  < 10 and self.x_direction == 1:
				self.x_direction = -1


		if self.hit_box.colliderect(self.l_paddle.hit_box):


			if self.hit_box.left - self.r_paddle.hit_box.right < 10 and self.x_direction == -1:
				self.x_direction = 1



			# if self.b_speed < 30:
			# 	self.b_speed += 1

			new_ball(self.x_pos,self.y_pos,self.x_direction,self.y_direction,self.b_speed,self.b_width,self.b_height,self.b_color,self.l_paddle,self.r_paddle)

			# new_ball(self.x_pos,self.y_pos,self.x_direction, self.y_direction)


	def move(self):

		if self.x_direction == -1:
			self.x_pos -= self.b_speed
		if self.x_direction == 1:
			self.x_pos += self.b_speed

		if self.y_direction == 1:
			self.y_pos -= self.b_speed
		if self.y_direction == -1:
			self.y_pos += self.b_speed

		self.hit_box.update(self.x_pos,self.y_pos,self.b_width,self.b_height)



def new_ball(x_pos,y_pos,x_direction,y_direction,b_speed,b_width,b_height,b_color,l_paddle,r_paddle):

	red = random.randint(100,225)
	green = random.randint(100,225)
	blue = random.randint(100,225)

	b_color = (red,green,blue)
	if b_speed < 20:
		b_speed = random.randint(7,10)

	new_ball = Ball(x_pos+50,y_pos,x_direction,y_direction,b_speed,b_width,b_height,b_color,l_paddle,r_paddle)
	ball_list.append(new_ball)

	if len(ball_list) > 300:
		del ball_list [1]

			# if len(ball_list) < 30:

			# 	new_ball = Ball(x_pos,y_pos,x_direction,y_direction,b_speed,b_width,b_height,b_color,l_paddle,r_paddle)
			# 	ball_list.append(new_ball)

			# 	if len(ball_list) < 30



class Main():

	def __init__(self):

		self.l_score = 0
		self.r_score = 0

		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		self.background = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
		self.background.fill((25,25,25))

		self.keys = pygame.key.get_pressed()

		self.p_width,self.p_height = 25,120
		self.p_speed = 25

		self.b_width,self.b_height = 25,25
		self.b_speed = 10
		self.b_color = 'red'






		self.l_paddle = Paddle(
			'left',
			self.p_speed,
			self.p_width,
			self.p_height,)

		self.r_paddle =	Paddle(
			'right',
			self.p_speed,
			self.p_width,
			self.p_height,)



		self.ball_1 = new_ball(
			x_pos = random.randint(220,520),
			y_pos = random.randint(400,880),
			x_direction = random.choice([-1,1]),
			y_direction = random.choice([-1,1]),
			b_speed = self.b_speed,
			b_width = self.b_width,
			b_height = self.b_height,
			b_color = self.b_color,
			l_paddle = self.l_paddle,
			r_paddle = self.r_paddle,
			)

		
	

	

		while True:

		#input

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()



			if pygame.key.get_pressed()[pygame.K_r]:
				ball_list.clear()
				Main()


			

			#updates

			self.l_paddle.move()
			self.r_paddle.move()


			for ball in ball_list:
				ball.collisions()
				ball.move()

		

			self.display.blit(self.background,(0,0))

			for ball in ball_list:
				self.display.blit(ball.surface,(ball.x_pos,ball.y_pos))


			self.display.blit(self.l_paddle.surface,(self.l_paddle.x_pos,self.l_paddle.y_pos))
			self.display.blit(self.r_paddle.surface,(self.r_paddle.x_pos,self.r_paddle.y_pos))

			pygame.display.update()

			self.clock.tick(60)

	
main = Main()

