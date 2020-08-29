import pygame
import time 
import random
import math

#The class called Enemy will be the Monster and Goblin
class Enemy:
#The def will include the self, and width/height of the Monster and Goblin.
#Because it will identity the dimensions of the enemy and screen so later on we can do more.
#The timer is = to 0 because it's essentially just kinda keep going.
#The speed is I believe explaining the speed of how fast it moves, by like pixels.
#By using the random.randint function - it allowed us to randomize it's movements.
#The random movement allowed it to go anywhere on the screens.
#The caught is false because we'll use a boolean to do true/false.
#The true or false will determine to start, finish, or restart the game later on.
    def __init__ (self, width, height):
        self.x = width/10
        self.y = height/10
        self.timer = 0
        self.speed = 2
        self.xdirection = random.randint(0, 1)
        self.ydirection = random.randint(0, 1)
        self.caught = False

#By defining movement, we're able to dictate where the enemy goes.
#By using the if function and using width, and height.
#By doi
    def move(self, width, height):
#If the monster is moving right, it will come out the other way from the left.
#And we named self.x because we are using the class enemy and gaining access to it's x properties.
        if self.x > width:
            self.x = 0

#If the monster is moving left, it will come out the other way from the right.
        elif self.x < 0:
            self.x = width

#If the monster is moving north, it will come out from the south.
        if self.y < 0:
            self.y = height

#If the monster is moving south, it will come out from the north.
        elif self.y > height:
            self.y = 0

#In my code, for less confusion I have identitied that:
# y direciton is 0 is up and 1 is down (or 0 is north and 1 is south)
# x direction is 0 is east and 1 is west
# The part of the code is taking properties from the direction to make it go diagnal.
        if self.ydirection == 0:
            self.y -= self.speed
        
        elif self.ydirection == 1:
            self.y += self.speed
        
        if self.xdirection == 0:
            self.x += self.speed

        elif self.xdirection == 1:
            self.x -= self.speed

#The classes here are taking from the parent class of Enemy.
#And I had to use pass or my code would scream at me.
#Since there was nothing under so it wouldn't run. 
class Monster(Enemy):
    pass
class Goblin(Enemy):
    pass

#I had to make another class hero and I couldn't merge it with Monster
#Because although they moved in the same aspect
#The hero would have to be controlled
class Hero:
        def __init__ (self, width, height):
            self.x = width/2
            self.y = height/2
            self.timer = 0
            self.speed = 2

        def move(self, width, height, xdirection, ydirection):
#If the hero is moving right, it will come out the other way from the left.
#We name is self.x because we are using the class Hero and accessing it's x properties.
#And we use the number 32 because schoology told us the images are 32 x 32?
            if self.x + 32 > width:
                self.x = width - 32

#If the hero is moving left, it will come out the other way from the right.
            elif self.x < 0:
                self.x = 0

#If the hero is moving up, it will come out from the south.
            if self.y < 0:
                self.y = 0
#If the monster is moving down, it will come out from the north.
            elif self.y + 32 > height:
                self.y = height - 32

#In my code, I had to identity for this:
#y direciton is 0 is up and 1 is down
#x direction is 0 is east and 1 is west
#I am confused by even my code logic on this.
            if ydirection == 0:
                self.y -= self.speed
            
            elif ydirection == 1:
                self.y += self.speed
            
            if xdirection == 0:
                self.x += self.speed

            elif xdirection == 1:
                self.x -= self.speed

#The width and height was the measurements of our screen game.
#So we called to the width and height so we'd keep our characters here.
def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

#The loaded images here are from the other template.
#It will load the hero, monster and goblins.
    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png'). convert_alpha()

#The trouble I had was to find the function to play the game.
#We apparently have to load the music first in order to play it.
#The win sound game is just what we play once the game wins.
#But we have to use the .Sound function for that (I don't know why).
    win_sound = pygame.mixer.Sound ('sounds/win.wav')
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play()

    # Game initialization
#In here, I'm just creating the variables and we have 5 (1 hero, 1 monster, 3 goblins)
    monster = Monster(width, height)
    player = Hero(width, height)

    goblin1 = Goblin(width, height)
    goblin2 = Goblin (width, height)
    goblin3 = Goblin (width, height)

#In this portion, I had to create a font and text.
#By using the formula given on schoology. 
#The 32 is the font size.
#The surface literally creates a surface.
#The one in string is what's printing.
#The 255,0,255 is what definites the color
#I purposely removed out the option portion which would've read (255,255,0).
#Uhh mainly because it seemed confusing lol.
    f = pygame.font.Font(None, 32)
    surf = f.render("Press Enter to play again", 1, (255,0,255))

#The false statement says that the game is going, and keeps going. 
    stop_game = False
    while not stop_game:
        monster.move(width, height)
        goblin1.move(width, height)
        goblin2.move(width, height)
        goblin3.move(width, height)
        
        for event in pygame.event.get():

#I believe this part is once we close out, the game just stops.
        # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

#The part here is step 14, and it is what happens when the hero catches the monster.
#So by using the distance function = sqrt(sqr(x1 - x2) + sqr(y1 - y2))
#The equation above we are determining when the characters will collide.
#So, we're calculating when the player or hero and monster have collided.
#And we will do the same for when the hero collides with the goblin.
#And hence, since they collided = true because images touched each other.
        if math.sqrt((player.x - monster.x)**2 + (player.y - monster.y)**2) <= 32:
            monster.caught = True 
#And here, we use the win sound so that when hero and monster collide, music plays. 
            win_sound.play()

#And above near lines 98-101 I identitied the key and restated again:
#In my code, I had to identity for this:
#y direciton is 0 is up and 1 is down (north and south).
#x direction is 0 is east and 1 is west (right and left).
#I am confused by even my code logic on this.
#But essentially we are assigning keys to our movements.
#So, by using K_RIGHT K_LEFT K_DOWN K_UP we are literally accessing our arrow keys.
#The return is enter, and by pressing enter we restart the game.
        xdirection = 2
        ydirection = 2
        key = pygame.key.get_pressed()
        if key [pygame.K_RIGHT]: 
            xdirection = 0
        
        if key [pygame.K_LEFT]:
            xdirection = 1

        if key [pygame.K_UP]:
            ydirection = 0

        if key [pygame.K_DOWN]:
            ydirection = 1

#So, now we are doing the same thing where if we literally press enter once we catch monster.
#We use the function monster.caught = False to say you didn't catch him.
#So he is being respawned in a different randomized location to start the game again.

        if key [pygame.K_RETURN] and monster.caught:
            monster.caught = False
            monster.x = random.randint(0, width)
            monster.y = random.randint(0, height)
            

#Uhh, here you just use the player.move function so it takes properties from his class.
        player.move(width, height, xdirection, ydirection)

#The background and the blit just makes the image appear.
#So one for the background, one for hero, and three for the goblin.
#But you need to have an if statement here because of the game.
#So, then you use if statements of if you caught him or not. 
#Ehh this part confused me so much I don't even really understand it. 

        # Draw background
        screen.blit(background_image, [0, 0])
        screen.blit(hero_image, [player.x, player.y])
        screen.blit(goblin_image, [goblin1.x, goblin1.y])
        screen.blit(goblin_image, [goblin2.x, goblin2.y])
        screen.blit(goblin_image, [goblin3.x, goblin3.y])
        if not monster.caught:
            screen.blit(monster_image, [monster.x, monster.y])
        if monster.caught:
            screen.blit(surf, [width/5, height/2])


#I 
        # Game display

        pygame.display.update()
        monster.timer += clock.tick(60)
#If 2 seconds have gone by, it's just to check that the timer is running. So, you can put like any number.
        if monster.timer >= 2000:
            monster.timer = 0
#The random function will redirect the monster into another direction inside the box.
#It's what we did kinda up there
            monster.xdirection = random.randint(0, 1)
            monster.ydirection = random.randint(0, 1)

            goblin1.xdirection = random.randint(0, 1)
            goblin1.ydirection = random.randint(0, 1)

            goblin2.xdirection = random.randint(0, 1)
            goblin2.ydirection = random.randint(0, 1)

            goblin3.xdirection = random.randint(0, 1)
            goblin3.ydirection = random.randint(0, 1)


    pygame.quit()

if __name__ == '__main__':
    main()
