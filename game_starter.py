import arcade


# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BACKGROUND_IMG = "images/game_background.png"
GAME_TITLE = "Meteor Garden"
GAME_SPEED = 1/60


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
