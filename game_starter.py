import arcade
import Other_sprites_sheet
#Remember to credit authors


# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BACKGROUND_IMG = "images/game_background.png"
GAME_TITLE = "Meteor Garden"
GAME_SPEED = 1/60
character_speed=4
FACING_RIGHT=0
FACING_LEFT=1

class Character(arcade.Sprite):
    def __init__(self):

        super().__init__()
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 6
        self.scale = 0.25
        '''code below is from Paul Vincent Craven via http://arcade.academy/examples/sprite_face_left_or_right.html'''
        texture = arcade.load_texture("images/main_facing_right.png", mirrored=True, scale=self.scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/main_facing_right.png", scale=self.scale)
        self.textures.append(texture)
        self.set_texture(FACING_RIGHT)


    def update_animation(self, delta_time: float = 1/60):
        '''update_animation function is from Paul Vincent Craven via http://arcade.academy/examples/sprite_face_left_or_right.html'''
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.change_x<0:
            self.set_texture(FACING_RIGHT)
        if self.change_x > 0:
            self.set_texture(FACING_LEFT)
        if self.right>WINDOW_WIDTH-1:
            self.right=WINDOW_WIDTH-1
        if self.left < 0:
            self.left = 0
        if self.top > WINDOW_HEIGHT - 1:
            self.top = WINDOW_HEIGHT - 1

class Introduction(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show(self):
        self.background=arcade.load_texture(BACKGROUND_IMG)
        self.character=Character()
        self.dad = Other_sprites_sheet.Dad().dad
        self.dad.center_x = 500
        self.dad.center_y = 120

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                                      WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.character.draw()
        self.dad.draw()
        arcade.draw_text("Your objective is to get rid of meteors\n before they touch the garden\n"
                       "Just touch the meteors with your wand\n before they touch the garden\n"
                       "Use up, left, right keys to move \nand collect any falling bottles\n"
                       "Click to start",50,400,arcade.color.ALABAMA_CRIMSON,font_size=18)
        arcade.draw_text("I'll be back soon but I'll leave this to you.\nDad has faith in you, so good luck!",350,210,arcade.color.BLACK)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        main_level = MeteorGarden()
        self.window.show_view(main_level)


class MeteorGarden(arcade.View):

    def __init__(self):
        """ Initialize variables """
        super().__init__()
        self.platform_list = None



    def on_show(self):
        """ Setup the game (or reset the game) """
        self.time=0.0
        self.background = arcade.load_texture(BACKGROUND_IMG)
        self.character = Character()
        self.platform_list = arcade.SpriteList()

        '''for loop inspired by Paul Vincent Craven's setup from
         http://arcade.academy/examples/sprite_moving_platforms.html#sprite-moving-platforms'''
        for placement in range(10):
            wall = arcade.Sprite("images/main_facing_right.png",0.1)
            wall.bottom = 0
            wall.center_x = placement * 100
            self.platform_list.append(wall)
        self.physics=arcade.PhysicsEnginePlatformer(self.character,
                                           self.platform_list,
                                           gravity_constant=0.15)
        self.meteor_list = arcade.SpriteList()




    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH//2, WINDOW_HEIGHT//2,
                                      WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.character.draw()
        self.meteor_list.draw()
        seconds = int(self.time) % 60
        arcade.draw_text("Time is now:"+str(seconds), 300, 300, arcade.color.BLACK, 30)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.character.update_animation()
        self.physics.update()
        self.time+=delta_time
        if self.time<60 and int(self.time)%2==0:
            self.meteor_list.append(Other_sprites_sheet.Meteor())

        self.meteor_list.update()




    def on_key_press(self, key, modifiers: int):
        if key==arcade.key.LEFT:
            self.character.change_x=-character_speed
        elif key==arcade.key.RIGHT:
            self.character.change_x=character_speed
        elif key==arcade.key.UP:
            if self.physics.can_jump():
                self.character.change_y=character_speed

    def on_key_release(self, key, modifiers: int):#nestnig no
        if key==arcade.key.UP:
            self.character.change_y=0

        elif key==arcade.key.LEFT or key==arcade.key.RIGHT:
            self.character.change_x=0


#mouse press:collides with points

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Meteor Game")
    intro=Introduction()
    window.show_view(intro)
    arcade.run()



if __name__ == "__main__":
    main()