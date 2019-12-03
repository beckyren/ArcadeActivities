import arcade

from random import randint


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.ANDROID_GREEN
GAME_TITLE = "Introduction"
NEXT_PHASE={
    'ada':'potato',
    'potato':'ada'
}
TIMER_MAXIMUM = 100
print("Hello, make sure to only click Ada! If you click the green space you won't get points off(mostly), \n"
      "but if you click the potato I will deduct a point!")


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
            self.timer += randint(0,1)*randint(1,6)
            #Ohhh I finally get it, the self timer adds up quicker with bigger maxes in randint
        else:
            self.timer = 0
            self.phase = NEXT_PHASE[self.phase]

    def on_mouse_press(self, x, y, button, modifiers):
        if self.phase=='ada' and button == arcade.MOUSE_BUTTON_LEFT:
            if (self.ada.points[1][0] - 10 > x > self.ada.points[0][0] + 10) and (
                    self.ada.points[3][1] - 30 > y > self.ada.points[1][1] + 30):
                self.score+=1
                print("Added 1 to your score\nScore is now: ",str(self.score))
        elif self.phase=='potato' and button ==arcade.MOUSE_BUTTON_LEFT:
            if(x<self.potato.points[1][0] and x>self.potato.points[0][0]) and (y<self.potato.points[2][1]-10 and y>self.potato.points[0][1]+10):
                self.score-=1
                print("Subtracted 1 from your score\nScore is now: ",str(self.score))

def main():
    window = Ada_Or_Potato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
