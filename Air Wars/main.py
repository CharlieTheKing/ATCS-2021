"""
Air Wars Arcade Program

@author: Charlie King
@version: 4/21/22
"""

import arcade
import random

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
RADIUS = 150
SCREEN_TITLE = "Air Wars!"
SCALING = 0.15
LEVEL = 1
app = None

# Classes
class Bug(arcade.Sprite):
    """Base class for all flying sprites
    Flying sprites include bugs and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()

        self.AI()

        x1 = self.center_x - 40
        x2 = self.center_x + 40
        y1 = self.center_y - 60
        y2 = self.center_y + 60
        self.set_hit_box([(x1, y1), (x2, y1), (x1, y2), (x2, y2)])

    def AI(self):
        # Set its speed to a random speed heading left
        x_change_max = int(app.level - 3 - app.level * 3)
        x_change_min = int(app.level - 2 - app.level * 2)
        # adjust course depending on location of player
        if self.center_y - app.player.center_y > 1 or self.center_y - app.player.center_y < -1:
            self.velocity = (random.randint(x_change_max, x_change_min), (app.player.center_y - self.center_y) / 50)
        else:
            self.velocity = (random.randint(x_change_max, x_change_min), 0)

class Bullet(arcade.Sprite):
    def update(self):

        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """
        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()

        self.velocity = (3, 0)

class Cloud(arcade.Sprite):
    """Base class for all flying sprites
    Flying sprites include bugs and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()

        # Set its speed to a random speed heading left
        x_change_max = int(app.level - 3 - app.level * 2)
        x_change_min = int(app.level - 2 - app.level * 1.5)
        self.velocity = (random.randint(x_change_max, x_change_min), 0)



# Classes
class AirWars(arcade.Window):
    """ The game """

    def __init__(self):
        """Initialize the game
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set up the empty sprite lists
        self.small_enemies_list = None
        self.clouds_list = None
        self.all_sprites = None
        self.paused = None
        self.player = None
        self.game_started = False
        self.game_over = False
        self.level = 1
        self.reset()

    def reset(self):
        # Set up the empty sprite lists
        self.small_enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.paused = False
        self.player = None
        self.setup()
        self.on_draw()

    def game_over(self):
        self.small_enemies_list = None
        self.clouds_list = None
        self.bullet_list = None
        self.all_sprites = None


    def setup(self):
        """Get the game ready to play"""

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

        # Set up the player
        self.player = arcade.Sprite("plane.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        if self.game_started is True:
            self.all_sprites.append(self.player)

        arcade.unschedule(self.add_small_enemy)
        # Spawn new enemy every 1.5 / self.level seconds
        arcade.schedule(self.add_small_enemy, 1.5 / self.level)

        # Spawn new cloud every 3 seconds
        arcade.unschedule(self.add_cloud)
        arcade.schedule(self.add_cloud, 4)

        self.on_update(float)

    def add_small_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # Create enemy sprite
        enemy = Bug("bug.png", 0.08)

        # Set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 15)

        # Add it to the enemies list
        self.small_enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def shoot_bullet(self):
        bullet = Bullet("Bullet.png", 0.04)
        bullet.center_x = app.player.center_x + 30
        bullet.center_y = app.player.center_y
        self.bullet_list.append(bullet)
        self.all_sprites.append(bullet)


    def add_cloud(self, delta_time: float):
        """Adds a new cloud to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new cloud sprite
        cloud = Cloud("cloud.png", SCALING)

        # Set its position to a random height and off screen right
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        cloud.velocity = (random.randint(-2, -1), 0)

        # Add it to the enemies list
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if self.game_started is True:

            if symbol == arcade.key.Q:
                # Quit immediately
                arcade.close_window()

            if symbol == arcade.key.P:
                self.paused = not self.paused

            if symbol == arcade.key.W or symbol == arcade.key.UP:
                self.player.change_y = 5

            if symbol == arcade.key.S or symbol == arcade.key.DOWN:
                self.player.change_y = -5

            if symbol == arcade.key.A or symbol == arcade.key.LEFT:
                self.player.change_x = -5

            if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
                self.player.change_x = 5

            if symbol == arcade.key.SPACE:
                self.shoot_bullet()

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if symbol == arcade.key.ENTER and self.game_started is False:
            self.game_started = True
            self.reset()

        if symbol == arcade.key.ENTER and self.game_over is True:
            self.game_over = False
            self.level = 1
            self.reset()


        if (
                symbol == arcade.key.W
                or symbol == arcade.key.A
                or symbol == arcade.key.UP
                or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
                symbol == arcade.key.A
                or symbol == arcade.key.D
                or symbol == arcade.key.LEFT
                or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing

        Arguments:
            delta_time {float} -- Time since the last update
        """

        # If paused, don't update anything
        if self.paused:
            return

        if self.player.right >= (SCREEN_WIDTH - 75):
            self.level = self.level + 1
            self.reset()
            return

        # Did you hit anything? If so, end the game
        if self.player.collides_with_list(self.small_enemies_list):
            # checks if bug spawned on top of the plane
            if self.player.right < SCREEN_WIDTH - 90:
                self.game_over = True
                return

        for bullet in self.bullet_list:
            for small_enemy in self.small_enemies_list:
                if bullet.collides_with_sprite(small_enemy):
                    self.small_enemies_list.remove(small_enemy)
                    self.bullet_list.remove(bullet)

        # Update everything
        self.all_sprites.update()

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        # Draw a blue circle
        if self.game_started is False:
            arcade.draw_text("Press return to start", 260, 385.0,
                arcade.color.BLACK, 40, 80, 'left')

        elif self.game_over is True:
            arcade.draw_text("Game Over", 360, 415.0,
                             arcade.color.BLACK, 40, 80, 'left')
            arcade.draw_text("You reached level " + str(self.level), 260, 365.0,
                             arcade.color.BLACK, 40, 80, 'left')
            arcade.draw_text("Press return to play again", 200, 312.0,
                             arcade.color.BLACK, 40, 80, 'left')

        else:
            # Draw finish line
            self.all_sprites.draw()
            # draw checkerboard finish line
            for i in range(30):
                if i % 2 == 1:
                    arcade.draw_rectangle_filled(
                        SCREEN_WIDTH - 60, i * 40, 40, SCREEN_HEIGHT, arcade.color.WHITE
                    )
                else:
                    arcade.draw_rectangle_filled(
                        SCREEN_WIDTH - 60, i * 40, 40, SCREEN_HEIGHT, arcade.color.BLACK
                    )
            for i in range(30):
                if i % 2 == 1:
                    arcade.draw_rectangle_filled(
                        SCREEN_WIDTH - 20, i * 40, 40, SCREEN_HEIGHT, arcade.color.BLACK
                    )
                else:
                    arcade.draw_rectangle_filled(
                        SCREEN_WIDTH - 20, i * 40, 40, SCREEN_HEIGHT, arcade.color.WHITE
                    )
            # draw level count
            arcade.draw_text("Level " + str(self.level), 30, SCREEN_HEIGHT - 60, arcade.color.BLACK, 30)


# Main code entry point
if __name__ == "__main__":
    app = AirWars()
    arcade.run()
