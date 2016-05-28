import sys, pygame

def main():
	pygame.init()
	scoreP1 = 0
	scoreP2 = 0
	size = (600, 450)
	speed = [2, 1]
	BallCords = [300,225]
	black = 0, 0, 0
	screen = pygame.display.set_mode(size)
	color = (200,50,100)
	radius = 5
	clock = pygame.time.Clock()
	LPad = pygame.Rect(50,200, 5, 50)
	RPad = pygame.Rect(545,200,5, 50)
	Clr_Pad = 255,255,255
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					if LPad[1] >= 101:
						LPad[1] = LPad[1] - 100
				if event.key == pygame.K_a:
					if LPad[1] <= 299:
						LPad[1] = LPad[1] + 100
				if event.key == pygame.K_e:
					if RPad[1] >= 101:
						RPad[1] = RPad[1] - 100
				if event.key == pygame.K_d:
					if RPad[1] <= 299:
						RPad[1] = RPad[1] + 100
					
		screen.fill((0,0,0))
		setScore(screen, scoreP2, scoreP1)
		pygame.draw.circle(screen, color, BallCords, radius)
		pygame.draw.rect(screen, Clr_Pad, LPad)
		pygame.draw.rect(screen, Clr_Pad, RPad)
		pygame.display.update()
		movecircle(BallCords, speed)
		speed, scoreP1, scoreP2 = borderCheck(BallCords, speed, size, radius, scoreP1, scoreP2)
		checkRPad(RPad, speed, BallCords)
		checkLPad(LPad, speed, BallCords)
		print(str(scoreP2))
		clock.tick(100)

def movecircle(cords, speed):
	for i in range(2):
		cords[i] = cords[i] + speed[i]
	return cords

def borderCheck(cords, speed, size, rad, LP, RP):
	for i in range(2):
		if i == 0:
			if (cords[i] - rad) <= 0:
				speed[i] = speed[i] *-1
				LP = LP + 1
			if (cords[i] + rad) >= size[i]:
				speed[i] = speed[i] *-1
				RP = RP + 1
		else:
			if (cords[i] - rad) <= 0:
				speed[i] = speed[i] *-1
			if (cords[i] + rad) >= size[i]:
				speed[i] = speed[i] *-1
	return speed, LP, RP

def checkRPad(rect, speed, cords):
	if speed[0] >= 0:
		if rect.collidepoint(cords[0], cords[1]) == True:
			speed[0] = speed[0] *-1
	return speed

def checkLPad(rect, speed, cords):
	if speed[0] <= 0:
		if rect.collidepoint(cords[0], cords[1]) == True:
			speed[0] = speed[0] *-1
	return speed
	
# NOTE Left and Right are REVERSED
# Anything l is displayed on the RIGHT and vice versa	
def setScore(screen, RS, LS):
	lScore = pygame.font.SysFont("monospace", 30)
	rScore = pygame.font.SysFont("monospace", 30)
	lLabel = lScore.render(str(LS), 1, (255,255,255))
	rLabel = rScore.render(str(RS), 1, (255,255,255))
	screen.blit(rLabel,(1,1))
	screen.blit(lLabel, (580,1))
			
main()