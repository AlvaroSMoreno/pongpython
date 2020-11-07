import pygame, sys, random

#SETUP
pygame.init()
clock = pygame.time.Clock()

def ball_animation():
	global ball_speed_x, ball_speed_y
	ball.x += ball_speed_x
	ball.y += ball_speed_y
	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1

	if ball.colliderect(player) or ball.colliderect(enemy):
		ball_speed_x *= -1

	if ball.left <= 0 or ball.right >= screen_width:
		#GOAL!
		goal()

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

def goal():
	global ball_speed_x, ball_speed_y, score_player, score_enemy
	if ball.x < screen_width / 2 : #pego en el enemy! o sea, punto para player
		score_player += 1
	else:
		score_enemy += 1
	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))
	if score_enemy >= 5 or score_player >= 5:
		pygame.exit()
		sys.exit()

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Juego de Pong")

game_font = pygame.font.SysFont("comicsansms", 30)

#Rectangles
ball = pygame.Rect(screen_width/2 -11, screen_height/2 - 11,22,22)
player = pygame.Rect(screen_width-20, screen_height/2 -60, 10, 120)
enemy = pygame.Rect(10, screen_height/2 -60, 10, 120)

ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
enemy_speed = 0
score_player = 0
score_enemy = 0
player_step = 3
enemy_step = 3

bgColor = (25,25,25) #RGB -> Red:25 , Green: 25, Blue: 25
objectColor = (115, 115, 115) #RGB -> Red:115 , Green: 115, Blue: 115
fontColor = (200, 200, 200)

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		#Eventos de teclado
		if event.type == pygame.KEYDOWN: #Es cuando presione la tecla
			if event.key == pygame.K_DOWN:
				player_speed += player_step
			if event.key == pygame.K_UP:
				player_speed -= player_step
			if event.key == pygame.K_s:
				enemy_speed += enemy_step
			if event.key == pygame.K_w:
				enemy_speed -= enemy_step

		if event.type == pygame.KEYUP: #Es cuando solte la tecla
			if event.key == pygame.K_DOWN:
				player_speed -= player_step
			if event.key == pygame.K_UP:
				player_speed += player_step
			if event.key == pygame.K_s:
				enemy_speed -= enemy_step
			if event.key == pygame.K_w:
				enemy_speed += enemy_step

	screen.fill(bgColor)
	pygame.draw.rect(screen, objectColor, player) #Dibujar player
	pygame.draw.rect(screen, objectColor, enemy) #Bibujar Enemigo
	pygame.draw.ellipse(screen, objectColor, ball) #Dibujando pelota
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2, screen_height)) #Dividir campo
	ball_animation()
	player_animation()
	enemy_animation()
	player_text = game_font.render(f"{score_player}", False, fontColor)
	enemy_text = game_font.render(f"{score_enemy}", False, fontColor)
	screen.blit(player_text, (screen_width/2 + 30, 10))
	screen.blit(enemy_text, (screen_width/2 - 40 , 10))
	pygame.display.flip()
	clock.tick(60) #60 FPS