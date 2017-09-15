#Duh
import pygame

#custom class
from Player import Player  ##once you import you must make player var

#have to init the pygame object so we can use it
pygame.init()

#screen size is a tuple
screen_size = (1000,800)
#painting background, need a tuple for background color
background_color = (82, 111, 53)
hero_image = pygame.image.load('Super_Hero_.png')

#create a screen for pygame to use to draw on
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Shooter Game!")


the_player = Player('Super_Hero_.png', 100, 100, screen)

#player = {
#	"x": 100,
#	"y": 100
#}
#set up main game loop
#will run forever until break
game_on = True
while game_on: 
	#loop through all pygame events
	#this is how to exit game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			#print "User pressed a key!"
			if event.key == 273: #up
				#the_player.y -= the_player.speed
				the_player.should_move("up", True)
			elif event.key == 274:
				#the_player.y += the_player.speed
				the_player.should_move("down", True)
			if event.key == 275: #right
				#the_player.x += the_player.speed
				the_player.should_move("right", True)
			elif event.key == 276: #left
				#the_player.x -= the_player.speed
				the_player.should_move("left", True)

		elif event.type == pygame.KEYUP:
			#print "User pressed a key!"
			if event.key == 273: #up
				#the_player.y -= the_player.speed
				the_player.should_move("up", False)
			elif event.key == 274:
				#the_player.y += the_player.speed
				the_player.should_move("down", False)
			if event.key == 275: #right
				#the_player.x += the_player.speed
				the_player.should_move("right", False)
			elif event.key == 276: #left
				#the_player.x -= the_player.speed
				the_player.should_move("left", False)


	screen.fill(background_color) ##paints the screen

	the_player.draw_me()

	#screen.blit(the_player.image, [the_player.x, the_player.y])

	pygame.display.flip()