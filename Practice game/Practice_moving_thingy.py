import pygame,sys

# from time import time

# WINDOW_WIDTH = 960
# WINDOW_HEIGHT = 947

# window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

# bg_image = pygame.image.load('bg_image.jpeg').convert()

# lgi = pygame.image.load('little_guy_image.png').convert()
# lgi = pygame.transform.smoothscale(lgi,(100,100))

# lgi_y = 500
# lgi_x = 500

# while True:

# 	# events
# 	for event in pygame.event.get():

# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()


# 	keys = pygame.key.get_pressed()

# 	if keys[pygame.K_UP]:
# 		lgi_y -= 3
# 	if keys[pygame.K_DOWN]:
# 		lgi_y += 3
# 	if keys[pygame.K_RIGHT]:
# 		lgi_x += 3
# 	if keys[pygame.K_LEFT]:
# 		lgi_x -= 3


# 	# updates
# 	window.fill((255,255,255))
# 	window.blit(bg_image,(0,0))
# 	window.blit(lgi,(lgi_x,lgi_y))


# 	# display
# 	pygame.display.update()














# PONG
SW,SH = 1000,700
player_speed = 10
ball_speed = 8




ball_speed_x = ball_speed
ball_speed_y = ball_speed

clock = pygame.time.Clock()

paddle_w,paddle_h = 25,100

# paddle_w,paddle_h = 100,25

ball_w,ball_h = 25,25

display_surface = pygame.display.set_mode((SW,SH))

l_paddle = pygame.Surface((paddle_w,paddle_h))
l_paddle.fill('white')
l_y = SW/2

l_rect = pygame.Rect(0,SW/2,paddle_w,paddle_h)



r_paddle = pygame.Surface((paddle_w,paddle_h))
r_paddle.fill('white')
r_y = SW/2

r_rect = pygame.Rect(SW-paddle_w,SW/2,paddle_w,paddle_h)



ball = pygame.Surface((ball_w,ball_h))
ball.fill('green')
b_x,b_y = paddle_w,SH/2

b_rect = pygame.Rect(paddle_w,SH/2,ball_w,ball_h)


bg = pygame.Surface((SW,SH))
bg.fill('black')



while True:
        
	#input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP] and l_rect.top > 0:
		l_y -= player_speed


	if keys[pygame.K_DOWN] and l_rect.bottom < SH:
		l_y += player_speed

	#updates


	if b_rect.colliderect(r_rect):
		#print('collision')
		if abs(b_rect.right - r_rect.left) < 10 and ball_speed_x > 0:
			ball_speed_x = -ball_speed_x

		if abs(b_rect.bottom - r_rect.top) < 10 and ball_speed_y < 0:
			ball_speed_y = -ball_speed_y

		if abs(b_rect.top - r_rect.bottom) < 10 and ball_speed_y > 0:
			ball_speed_y = -ball_speed_y


	if b_rect.colliderect(l_rect):

		if abs(b_rect.left - l_rect.right) < 10 and ball_speed_x < 0:
			ball_speed_x = -ball_speed_x

		if abs(b_rect.bottom - l_rect.top) < 10 and ball_speed_y > 0:
			ball_speed_y = -ball_speed_y

		if abs(b_rect.top - l_rect.bottom) < 10 and ball_speed_y < 0:
			ball_speed_y = -ball_speed_y



#	Ball window collision

	if b_rect.right >= SW or b_rect.left <= 0:
		ball_speed_x = -ball_speed_x
	b_x += ball_speed_x

	if b_rect.top <= 0 or b_rect.bottom >= SH:
		ball_speed_y = -ball_speed_y
	b_y += ball_speed_y



	display_surface.blit(bg,(0,0))

	display_surface.blit(l_paddle,(0,l_y))
	l_rect.update(0,l_y,paddle_w,paddle_h)

	# display_surface.blit(l_paddle,(0,b_y))
	# l_rect.update(0,b_y,paddle_w,paddle_h)

	display_surface.blit(r_paddle,(SW - paddle_w,b_y))
	r_rect.update(SW-paddle_w,b_y,paddle_w,paddle_h)

	display_surface.blit(ball,(b_x,b_y))
	b_rect.update(b_x,b_y,ball_w,ball_h)



	pygame.display.update()

	clock.tick(60)









