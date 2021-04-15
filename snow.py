# importa i moduli utilizzati
import pygame
import random

# inizializza pygame
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# dimensione dello schermo
SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# inizializza lista vuota
snow_list = []

# generazione posizione iniziale dei fiocchi
for i in range(50):
	x = random.randrange(0, 400)
	y = random.randrange(0, 400)
	snow_list.append([x, y])

clock = pygame.time.Clock()
# ciclo principale
done = False

while not done:
	# gestione degli eventi
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(BLACK)

	for i in range(len(snow_list)):
		# disegna il fiocco
		pygame.draw.circle(screen, WHITE, snow_list[i], 2)

		# muovilo giù di un pixel
		snow_list[i][1] += 1

		# gestione delle collisioni
		if snow_list[i][1] > 400:
			# spostalo verso la cima allo schermo
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# dagli una nuova posizione sulle x
			x = random.randrange(0, 400)
			snow_list[i][0] = x

	pygame.display.flip()
	clock.tick(60)

pygame.quit()