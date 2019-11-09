import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60
NEXT_PHASE={
    'ada':'potato',
    'potato':'ada'
}
TIMER_MAXIMUM = 100


class Ada_Or_Potato(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.phase='ada'
        self.timer=0

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.ada = arcade.Sprite("images/ada.png", 1)
        self.ada.center_x=WINDOW_WIDTH/2
        self.ada.center_y=WINDOW_HEIGHT/2
        self.potato=arcade.Sprite("images/potato.png",0.2)
        self.potato.center_x=WINDOW_WIDTH/2
        self.potato.center_y=WINDOW_HEIGHT/2
        self.score=0
        self.a_sprite_list=arcade.SpriteList()
        self.a_sprite_list.append(self.ada)
        self.b_sprite_list=arcade.SpriteList()
        self.b_sprite_list.append(self.potato)
    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        #self.score
        self.update_timer()

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        if self.phase=='ada':
            self.ada.draw()
        else:
            self.potato.draw()

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.phase = NEXT_PHASE[self.phase]





def main():
    window = Ada_Or_Potato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
