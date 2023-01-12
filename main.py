import random
from time import sleep
from turtle import Screen
from player import Player
from invaders import Invaders
from bullet import Bullet
from score_board import ScoreBoard
from anime import Animate

background_image = "space.gif"

# can change the entire game speed by this
game_speed = 0.1

screen = Screen()
screen.register_shape(background_image)
screen.bgpic(background_image)
screen.setup(width=500, height=650)

screen.tracer(0)

# creating necessary class object
player = Player()
invaders = Invaders()
bullet = Bullet(game_speed)
score_board = ScoreBoard()
anime_player = Animate(game_speed, [player])
anime_aliens = Animate(game_speed, invaders.all_invaders)

# keyboard keys pressing commands
screen.listen()
screen.onkey(player.go_right, key="Right")
screen.onkey(player.go_left, key="Left")
screen.onkey(bullet.create_player_bullet, key="Up")

game_is_on = True
while game_is_on:
    sleep(game_speed)

    # to create bullet at position of the spaceship :player
    bullet.player_xcor = player.xcor()

    # to create random attack bullet from aliens
    attacker = random.choice(invaders.all_invaders)

    # to create bullet at position of the aliens :enemies
    bullet.create_aliens_bullet(attacker.xcor(), attacker.ycor())

    # moving things in board
    bullet.move_all_bullets()
    anime_aliens.move_inplace()
    anime_player.move_inplace()
    anime_aliens.move_sides()

    # DETECT collisions
    for enemy in invaders.all_invaders:
        for player_bullet in bullet.all_player_bullets:
            # collision with player bullets
            if player_bullet.distance(enemy) < 30:
                invaders.destroy(enemy)
                bullet.destroy_player_bullet(player_bullet)
                score_board.increase_score()

        for enemy_bullet in bullet.all_aliens_bullets:
            # collision with enemy bullets
            if enemy_bullet.distance(player) < 40:
                score_board.reduce_lives()
                bullet.destroy_all_bullets()
                player.revive()

        # if players lives all lost
        if score_board.lives == 0:
            game_is_on = False
            score_board.lose()

        # if players hit all the aliens
        if score_board.score >= 3600:
            game_is_on = False
            score_board.win()

    screen.update()

screen.exitonclick()
