import pygame, sys

#SETUP
pygame.init()
clock = pygame.time.Clock()

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Juego de Pong")

#Rectangles
ball = pygame.Rect(screen_width/2 -11, screen_height/2 - 11,22,22)
player = pygame.Rect(screen_width-20, screen_height/2 -60, 10, 120)
enemy = pygame.Rect(10, screen_height/2 -60, 10, 120)

bgColor = (25,25,25) #RGB -> Red:25 , Green: 25, Blue: 25
objectColor = (115, 115, 115) #RGB -> Red:115 , Green: 115, Blue: 115

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(bgColor)
	pygame.draw.rect(screen, objectColor, player) #Dibujar player
	pygame.draw.rect(screen, objectColor, enemy) #Bibujar Enemigo
	pygame.draw.ellipse(screen, objectColor, ball) #Dibujando pelota
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2, screen_height)) #Dividir campo

	pygame.display.flip()
	clock.tick(60) #60 FPS