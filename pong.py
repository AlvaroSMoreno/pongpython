import pygame, sys

#SETUP
pygame.init()
clock = pygame.time.Clock()

def ball_animation():
	global ball_speed_x, ball_speed_y
	ball.x += ball_speed_x
	ball.y += ball_speed_y
	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1

def player_animation():
	global player_speed
	player.y += player_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def enemy_animation():
	global enemy_speed
	enemy.y += enemy_speed
	if enemy.top <= 0:
		enemy.top = 0
	if enemy.bottom >= screen_height:
		enemy.bottom = screen_height

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Juego de Pong")

#Rectangles
ball = pygame.Rect(screen_width/2 -11, screen_height/2 - 11,22,22)
player = pygame.Rect(screen_width-20, screen_height/2 -60, 10, 120)
enemy = pygame.Rect(10, screen_height/2 -60, 10, 120)

ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
enemy_speed = 0

bgColor = (25,25,25) #RGB -> Red:25 , Green: 25, Blue: 25
objectColor = (115, 115, 115) #RGB -> Red:115 , Green: 115, Blue: 115

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		#Eventos de teclado
		if event.type == pygame.KEYDOWN: #Es cuando presione la tecla
			if event.key == pygame.K_DOWN:
				player_speed += 3
			if event.key == pygame.K_UP:
				player_speed -= 3
			if event.key == pygame.K_s:
				enemy_speed += 3
			if event.key == pygame.K_w:
				enemy_speed -= 3

		if event.type == pygame.KEYUP: #Es cuando solte la tecla
			if event.key == pygame.K_DOWN:
				player_speed -= 3
			if event.key == pygame.K_UP:
				player_speed += 3
			if event.key == pygame.K_s:
				enemy_speed -= 3
			if event.key == pygame.K_w:
				enemy_speed += 3

	screen.fill(bgColor)
	pygame.draw.rect(screen, objectColor, player) #Dibujar player
	pygame.draw.rect(screen, objectColor, enemy) #Bibujar Enemigo
	pygame.draw.ellipse(screen, objectColor, ball) #Dibujando pelota
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2, screen_height)) #Dividir campo
	ball_animation()
	player_animation()
	enemy_animation()

	pygame.display.flip()
	clock.tick(60) #60 FPS