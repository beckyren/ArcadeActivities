import arcade
class Dad(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.dad=arcade.Sprite("images/dad.png",0.4)
        #self.dad_list=arcade.SpriteList()
        #self.dad_list.append(self.dad)
