import arcade
#Remember to credit authors


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_IMG = "images/game_background.png"
GAME_TITLE = "Meteor Garden"
GAME_SPEED = 1/60
character_speed=5
FACING_RIGHT=0
FACING_LEFT=1

class Character(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.scale = 0.25
        '''code below is from Paul Vincent Craven via http://arcade.academy/examples/sprite_face_left_or_right.html'''
        texture = arcade.load_texture("images/main_facing_right.png", mirrored=True, scale=self.scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/main_facing_right.png", scale=self.scale)
        self.textures.append(texture)
        self.set_texture(FACING_RIGHT)
    def update_animation(self, delta_time: float = 1/60):
        '''code below is from Paul Vincent Craven via http://arcade.academy/examples/sprite_face_left_or_right.html'''
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.change_x<0:
            self.set_texture(FACING_LEFT)
        if self.change_x > 0:
            self.set_texture(FACING_RIGHT)










class MeteorGarden(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

        self.character=None

    def setup(self):
        """ Setup the game (or reset the game) """
        self.background = arcade.load_texture(BACKGROUND_IMG)
        self.character = Character()

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH//2, WINDOW_HEIGHT//2,
                                      WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.character.draw()

        #draw_text
        #Physics engine

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.character.update()
    def on_key_press(self, key, modifiers: int):
        if key==arcade.key.UP:
            self.character.change_y+=character_speed*2


        elif key==arcade.key.LEFT:
            self.character.change_x=-character_speed
        elif key==arcade.key.RIGHT:
            self.character.change_x=character_speed

    def on_key_release(self, key, modifiers: int):
        if key==arcade.key.UP: 
            self.character.change_y-=(character_speed)
        elif key==arcade.key.LEFT or key==arcade.key.RIGHT:
            self.character.change_x=0


#mouse press:collides with points

def main():
    window = MeteorGarden()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
