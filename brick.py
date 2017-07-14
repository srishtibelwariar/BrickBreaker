#!/usr/bin/env python
#Brick Breaker game
#Srishti Belwariar

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import ObjectProperty



class BBPaddle(Widget):
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.v
            offset = (ball.center_x - self.center_x) / (self.height/ 2)
            vy= vy* -1
            rebound = Vector(vx, vy)
            vel = rebound
            ball.v = vel.x, vel.y + offset


class BBBall(Widget):
    v_x=NumericProperty(10);
    v_y=NumericProperty(10);
    v=ReferenceListProperty(v_x, v_y)
    
    def move(self):
        self.pos = Vector(*self.v) + self.pos
            
            
class BBGame(Widget):
    ball = ObjectProperty(None)
    player= ObjectProperty(None)
    
    def serve_ball(self,  vel=(4, 0)):
        self.ball.center_x = self.player.center_x
        self.ball.y = self.y +60
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()
        self.player.bounce_ball(self.ball)
        
        # bounce off top, left and right edges
        if (self.ball.top > self.height):
            self.ball.v_y = self.ball.v_y * -1
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.v_x = self.ball.v_x * -1
        
        #initiate reserves if ball misses paddle   
        if (self.ball.y<self.y):
            self.serve_ball(vel=(4, 0))
    
    #allows for user control on paddle using mouse (plan to change it to arrow keys)
    def on_touch_move(self, touch):
        self.player.center_x = touch.x

class BBApp(App):
    def build(self):
        game = BBGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    BBApp().run()