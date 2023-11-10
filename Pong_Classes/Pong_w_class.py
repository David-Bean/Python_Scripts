import pygame,sys,time,random

clock = pygame.time.Clock()

WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720

display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

background = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
background.fill((25,25,25))

p_width,p_height = 25,120
p_speed = 9

b_width,b_height = 25,25
b_speed = 10

l_score = 0
r_score = 0



def new_ball(x_pos,y_pos,x_direction,y_direction):
		return Ball(x_pos,y_pos,x_direction,y_direction)

class Paddle():

	def __init__(self,side,speed):

		self.speed = speed
		self.y_pos = WINDOW_HEIGHT/2
		self.side = side

		self.surface = pygame.Surface((p_width,p_height))
		self.surface.fill('white')

		if self.side == 'left':
			self.x_pos = 10
		if self.side == 'right':
			self.x_pos = WINDOW_WIDTH - p_width

		self.hit_box = pygame.Rect((self.x_pos,self.y_pos,p_width,p_height))


	def move(self):

		keys = pygame.key.get_pressed()

		if self.side == 'left':

			if keys[pygame.K_UP] and self.hit_box.top > 0:
				self.y_pos -= self.speed
			if keys[pygame.K_DOWN] and self.hit_box.bottom < WINDOW_HEIGHT:
				self.y_pos += self.speed

		if self.side == 'right':

			if ball.y_pos < self.y_pos and self.hit_box.top > 0:
				self.y_pos -= 2*self.speed
			if ball.y_pos > self.y_pos and self.hit_box.bottom < WINDOW_HEIGHT:
				self.y_pos += 2*self.speed


		self.hit_box.update((self.x_pos,self.y_pos,p_width,p_height))

	

class Ball(pygame.sprite.Sprite):

	def __init__(self,x_pos,y_pos,x_direction,y_direction,*groups):

		super().__init__(*groups)

		self.speed = b_speed
		self.width = b_width
		self.height = b_height
		self.color = 'yellow'

		self.surface = pygame.Surface((self.width,self.height))
		self.surface.fill(self.color)

		self.y_pos = x_pos
		self.x_pos = y_pos

		self.x_direction = x_direction
		self.y_direction = y_direction

		self.hit_box = pygame.Rect(self.x_pos,self.y_pos,self.width,self.height)


	def collisions(self):

		if self.hit_box.top <= 0:
			self.y_direction = -1
		if self.hit_box.bottom >= WINDOW_HEIGHT:
			self.y_direction = 1

		if self.hit_box.right >= WINDOW_WIDTH:
			global l_score
			l_score += 1
			main()

		if self.hit_box.right < 0:
			global r_score
			r_score += 1
			main()



		if self.hit_box.colliderect(r_paddle.hit_box):
			if r_paddle.hit_box.left - self.hit_box.right  < 10 and self.x_direction == 1:
				self.x_direction = -1


		if self.hit_box.colliderect(l_paddle.hit_box):
			if self.hit_box.left - r_paddle.hit_box.right < 10 and self.x_direction == -1:
				self.x_direction = 1

			self.speed += 1

			# new_ball(self.x_pos,self.y_pos,self.x_direction, self.y_direction)


			


	def move(self):

		if self.x_direction == -1:
			self.x_pos -= self.speed
		if self.x_direction == 1:
			self.x_pos += self.speed

		if self.y_direction == 1:
			self.y_pos -= self.speed
		if self.y_direction == -1:
			self.y_pos += self.speed

		self.hit_box.update(self.x_pos,self.y_pos,self.width,self.height)





def play():
	while True:

		#input

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_r]:
			main()


		

		#updates

		l_paddle.move()
		r_paddle.move()
		ball.collisions()
		ball.move()

		display.blit(background,(0,0))
		display.blit(ball.surface,(ball.x_pos,ball.y_pos))
		display.blit(l_paddle.surface,(l_paddle.x_pos,l_paddle.y_pos))
		display.blit(r_paddle.surface,(r_paddle.x_pos,r_paddle.y_pos))

		pygame.display.update()
		clock.tick(30)


def main():

	clock = pygame.time.Clock()
	WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
	display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	background = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
	background.fill((25,25,25))

	keys = pygame.key.get_pressed()

	global l_paddle
	global r_paddle
	global ball

	l_paddle = Paddle('left',p_speed)
	r_paddle = Paddle('right',p_speed)
	ball = new_ball(random.randint(220,520),random.randint(400,880),random.choice([-1,1]),random.choice([-1,1]))

	play()

main()




