import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_IMG = "images/game_background.png"
GAME_TITLE = "Meteor Garden"
GAME_SPEED = 1/60
character_speed=5
class Character(arcade.Sprite):
    def __init__(self):
        super().__init__("images/cisc108_banner.png")
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.scale = 0.5

class MeteorGarden(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def setup(self):
        """ Setup the game (or reset the game) """
        self.background = arcade.load_texture(BACKGROUND_IMG)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH//2, WINDOW_HEIGHT//2,
                                      WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        #draw_text
        #Physics engine

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

#mouse press:collides with points

def main():
    window = MeteorGarden()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
