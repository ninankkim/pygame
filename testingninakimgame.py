#The import function down below uses time, random, and math.
#The import here goes into our library and uses those components to make our game work.
import pygame
import time 
import random
import math

#The first thing is we have a parent class called Enemy, and it's going to have Monster and Goblins in here.
#Because our monster and goblin share really similar characteristics of movement. 
#So, I used self, width, and height because it's going to help us understand the enemy movement.
#And it's going to be used when we want to manipulate how they move. 

#The self.x and self.y just is dividing the width by 10 to create a spot on the screen that'll show where they start.
#I just put the timer to 0, because time is constantly running and there isn't necessarily a time, instead keeps going.
#The speed is put to 2, because the higher the number, the faster it went (something that had to do with pixels).
#The x and y direction was equal to random, because their directions had to be randomized. 
#And the self.caught would be false until proven true under our if statements down below.

class Enemy:
    def __init__ (self, width, height):
        self.x = width/10
        self.y = height/10
        self.timer = 0
        self.speed = 2
        self.xdirection = random.randint(0, 1)
        self.ydirection = random.randint(0, 1)
        self.caught = False

#The define movement, we were able to dictate what the enemy does when they reach the end of the game screen.
#And we use the width and height of the screen to figure out how we do that. 
    def move(self, width, height):

#If the monster is moving right, it willcome out the other way from the left.
#Because x indicates the enemy is moving either left or right, when it moves greater than our width.
#We will equal x out to 0 to, essentially restart him.
#And we are using self.x because we are using the enemy class and gaining access to it's x properties.
        if self.x > width:
            self.x = 0

#If the monster is moving left, it will come out the other way from the right.
#Because when it's less than 0, when it's moving left. 
#It's now going to be equal to the width, to loop him back to the other side.
        elif self.x < 0:
            self.x = width

#If the monster is moving north, it will come out from the south.
        if self.y < 0:
            self.y = height

#If the monster is moving south, it will come out from the north.
        elif self.y > height:
            self.y = 0

#In my code, for less confusion I had to identity a key to help me remember:
#The y direciton is 0 is up and 1 is down (or 0 is north and 1 is south, imagine the y axis direction)
#The x direction is 0 is east and 1 is west (or 0 is left and 1 is right, imagine the x axis direction.
#The code here gives them movement. 

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
            self.caught = False

        def move(self, width, height, xdirection, ydirection):
#The hero movement is different because the hero cannot go out of the lines of the screen.
#If the hero is moving right, then we have to take into account the width of the game screen and the dimensions of our hero.
#We name is self.x because we are using the class Hero and accessing it's x properties.
#And we use the number 32 because schoology told us the images are 32 x 32? I read that somewhere LOL.
#I learned that there's an origin point on an image and might've not been the direct center.
#So we have to either add or subtract 32 so it doesn't go out of the lines of the screen. 
            if self.x + 32 > width:
                self.x = width - 32

#If the hero is moving left, it will stop at the left.
            elif self.x < 0:
                self.x = 0

#If the hero is moving up, it will stop at the top.
            if self.y < 0:
                self.y = 0

#If the monster is moving down, it will stop at the bottom. 
            elif self.y + 32 > height:
                self.y = height - 32

#In my code, I had to identity the key for this:
#x direction is 0 is east and 1 is west (like the x axis direction).
#y direciton is 0 is up and 1 is down (like the y axis direction).
#I am confused by even my code logic on this.
#But it works because we're having to get the self.y direction by using -=, which is getting 2 and subracting it from the self.y.

            if ydirection == 0:
                self.y -= self.speed
            
            elif ydirection == 1:
                self.y += self.speed
            
            if xdirection == 0:
                self.x += self.speed

            elif xdirection == 1:
                self.x -= self.speed

#The width and height was the measurements of our screen game.
#The movements were deteremined on how big or small our screen game was. 
def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

#The loaded images here are from the other template.
#It will load the hero, monster and goblins.
#I mean YES, COULD I HAVE CHANGED THE PICTURES SO MY PROJECT WASN'T SO VANILLA - SURE, BUT WAS I AFRAID MY CODE WOULD BREAK, YES. 
#SO, THE SAME WE SHALL KEEP IT.
    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha()

#The trouble I had was finding the function to play the game.
#But similarly you have to load music, in order for you to play the music. 
#And I added the win_sound music, so when we win this darn game and weirdly, the Sound command had to be capitalized.
#But the play function didn't have to so, I was like why. But it's the way it's suppose to be - smh coding. 
    win_sound = pygame.mixer.Sound ('sounds/win.wav')
    # pygame.mixer.music.load('sounds/music.wav')
    # pygame.mixer.music.play()
    lose_sound = pygame.mixer.Sound ('sounds/lose.wav')

# The game initialization
#In here, I'm just creating the variables with the width and height. 
#Andnd we have 5 characters in this game (1 hero, 1 monster, 3 goblins).
    monster = Monster(width, height)
    player = Hero(width, height)

    goblin1 = Goblin(width, height)
    goblin2 = Goblin (width, height)
    goblin3 = Goblin (width, height)

#The portion below gives the font and text - and the formula was just taken from schoology. 
#The number 32 is the font size and the surface literally creates a surface to put the text.
#The 255, 0 , 255 is defining the color or the RGB.
    f = pygame.font.Font(None, 32)
    surf = f.render("Press ENTER to play again", 1, (255,0,255))

    surf_losetext = f.render("You lose! Hit ENTER to play again.", 1, (255,0,255))

#The false statement says that the game is going, and keeps going. 
    stop_game = False
    game_timer = 0
    while not stop_game:
        game_timer += 1
        
        monster.move(width, height)
        if game_timer >= 10:
            screen.blit(goblin_image, [goblin1.x, goblin1.y])
        if game_timer >= 20:
            goblin1.move(width, height)
        if game_timer >= 200:
            screen.blit(goblin_image, [goblin2.x, goblin2.y])
            goblin2.move(width, height)
        if game_timer >= 300:
            screen.blit(goblin_image, [goblin3.x, goblin3.y])
            goblin3.move(width, height)
        for event in pygame.event.get():

#I believe this part is once we close out, the game just quits. 
        # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

#The game logic portion, which is funny because I LACKED A WHOLE LOT OF LOGIC AND LOST MY DAMN MARBLES HERE. 
#The part here is step 14 and what happens when the hero catches the monster and when the goblin catches the hero. 
#So by using the distance function = sqrt(sqr(x1 - x2) + sqr(y1 - y2))
#The equation above we are determining when the characters will collide.
#So, we're calculating when the player or hero and monster have collided.
#And we will do the same for when the hero collides with the goblin.
#And hence, since they collided = true because images touched each other.
        if math.sqrt((player.x - monster.x)**2 + (player.y - monster.y)**2) <= 32:
            monster.caught = True 
#And here, we use the win sound so that when hero and monster collide, music plays. 
            win_sound.play()

        if math.sqrt((player.x - goblin1.x)**2 + (player.y - goblin1.y)**2) <= 32:
            player.caught = True
            lose_sound.play()
        if math.sqrt((player.x - goblin2.x)**2 + (player.y - goblin2.y)**2) <= 32:
            player.caught = True
            lose_sound.play()
        if math.sqrt((player.x - goblin3.x)**2 + (player.y - goblin3.y)**2) <= 32:
            player.caught = True
            lose_sound.play()

        

#And above near lines 98-101 I identitied the key and restated again:
#In my code, I had to identity for this:
#y direciton is 0 is up and 1 is down (north and south).
#x direction is 0 is east and 1 is west (right and left).
#I am confused by even my code logic on this.
#But essentially we are assigning keys to our movements.
#So, by using K_RIGHT K_LEFT K_DOWN K_UP we are literally accessing our arrow keys.
#The return is enter, and by pressing enter we restart the game.
#the x direction and y direction is = 2 is because the move direction gets called
# and 0 and 1 is equal to a direction, but when it isn't it doens't move

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
        

#I just created the option that if the user had ENOUGH OF THIS MUSIC AND GAME - they can straight up dip.
        if key [pygame.K_q]:
            stop_game = True

#The key for enter were also created, so once the monster has been caught or the hero has been caught.
#The return key would restart the game and put the monster or hero in a randomized area so the user can keep playing.

        if key [pygame.K_RETURN] and monster.caught:
            monster.caught = False
            monster.x = random.randint(0, width)
            monster.y = random.randint(0, height)

        elif key [pygame.K_RETURN] and player.caught:
            player.caught = False
            player.x = random.randint(0, width)
            player.y = random.randint(0, height)

#Uhh, here you just use the player.move function so it takes properties from his class.
        player.move(width, height, xdirection, ydirection)

#The background and the blit just makes the image appear - it's like a method or function that was used. 
#And we had to create if and if not statements because if the player or monster is caught, a text must also appear. 

        # Draw background
        screen.blit(background_image, [0, 0])

        if not player.caught:
            screen.blit(hero_image, [player.x, player.y])
        if player.caught:
            screen.blit(surf_losetext, [width/7, height/2])

        # screen.blit(goblin_image, [goblin1.x, goblin1.y])
        # screen.blit(goblin_image, [goblin2.x, goblin2.y])
        # screen.blit(goblin_image, [goblin3.x, goblin3.y])
        if not monster.caught:
            screen.blit(monster_image, [monster.x, monster.y])
        if monster.caught:
            screen.blit(surf, [width/5, height/2])



#The time was confusing, but this was the formula that was given to us on the template.
#So, I used 2000, because it goes by mil-seconds so it's just acknowledging time. 
        # Game display

        pygame.display.update()
        monster.timer += clock.tick(60)
        if monster.timer >= 2000:
            monster.timer = 0
#The random function will redirect the monster into another direction inside the box.
#It's what we did kinda up there
#If i've gone 2000 cycles, then we're going to give them a random cordinate to move them. 

#The random function will randomy redirect the monster into any given direction inside the screen.
#And the timer and speed does have influence over the character's direction. 
#And up above, we're already acknowledged that 0 and 1 pertain to direction.
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
