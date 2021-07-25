import pygame
import random
import sys

pygame.init()

pygame.font.init()

FPS = 60
SIZE = WIDTH, HEIGHT = (600, 400)
BGCLR = (255, 224, 224)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

w,h = (300, 150)

surface = pygame.Surface((w,h))

head = "head.png"

arr = [[], []]

for i in range(1,100):
	arr[0].append(i*-5)
for i in range(1,50):
	arr[1].append(i*5)
for i in range(1, 10):
	arr[1].append(i*1000)
for i in range(1, 5):
	arr[1].append(i*-500)
arr[1].append(-20000)

luck = 0

money = 14250

rgb = [0,0,0]

index = 0

def drawText(screen, text):
	if rgb[0] >= 140:
		rgb[0] = 0
	if rgb[1] >= 149:
		rgb[1] = 0
	if rgb[2] >= 154:
		rgb[2] = 0
	
	rgb[0] += 5
	rgb[1] += 1
	rgb[2] += 1


	font = pygame.font.SysFont("timesnewroman", 20)
	text = font.render(text, True, rgb)
	text_r = text.get_rect(center=(WIDTH/2, HEIGHT - 100))
	screen.blit(text, text_r)
	return i

class B79P(object):
	def __init__(self):
		self.outline = pygame.Rect(WIDTH/2-60, HEIGHT/2-140, 120, 120)
		self.head = pygame.image.load(head).convert()
		self.head = pygame.transform.scale(self.head, (100, 100))
		self.og_head = self.head.copy()
		self.head_rect = self.head.get_rect(center=(WIDTH/2, HEIGHT/2 - 80))
		self.rotation = 0
		self.num = 0
	def rotateHead(self):
		if self.rotation >= 359:
			self.rotation = 0
		self.head = self.og_head
		self.rotation += 1
		self.head = pygame.transform.rotate(self.head, self.rotation)
	def updateNum(self, num):
		n = self.num + num
		self.num = 0
		return n
	def checkMouse(self):
		C = random.choice(arr)
		c = random.choice(C)
		return c


	def render(self, screen):
		self.rotateHead()
		self.head = pygame.transform.scale(self.head, (100, 100))
		screen.blit(self.head, self.head_rect)
		pygame.draw.rect(screen, (0,0,0), self.outline, 2)

sprites = pygame.sprite.Group()

btn = B79P()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if btn.outline.collidepoint(event.pos):
				x = btn.checkMouse()
				money += x

	screen.fill(BGCLR)

	money -= 0.1

	btn.render(screen)
	
	drawText(screen, str(money))
	pygame.display.update()
	clock.tick(FPS)
