import arcade
from random import randint
class Restart_Button(arcade.Sprite):
    def __init__(self):
        super().__init__()
        texture =arcade.load_texture("images/Button.png", scale=0.1)
        self.textures.append(texture)
        self.set_texture(0)
class Dad(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.dad=arcade.Sprite("images/dad.png",0.4)
class Meteor(arcade.Sprite):
    def __init__(self):
        super().__init__()
        texture = arcade.load_texture("images/glitch_meteor/meteor0001.png",scale=0.2)
        self.textures.append(texture)
        self.set_texture(0)
        self.center_x=randint(10,590)
        self.center_y=600
        self.velocity=0,-6
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        touching_grass=50
        if self.bottom<touching_grass:
            self.bottom=20
class Bottle(arcade.Sprite):
    def __init__(self):
        super().__init__()
        texture=arcade.load_texture("images/LeapsAndBounds.png",scale=0.15)
        self.textures.append(texture)
        self.set_texture(0)
        self.center_x=randint(10,590)
        self.center_y=600
        self.velocity=0,-5
    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.bottom<20:
            self.bottom=20



