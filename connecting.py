#!/usr/bin/python
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget
from math import cos
from numpy import linspace

Config.set('graphics', 'width', '256')
Config.set('graphics', 'height', '144')


class Animation(Widget):

    def __init__(self, **kwargs):
        super(Animation, self).__init__(**kwargs)
        self.ball_factors = list(linspace(1, 4, 24))
        self.balls = []
        with self.canvas:
            Color(0.0399625, 0.31640625, 0.4921875)
            for i in range(24):
                x = 69 + 5 * i
                y = 56
                self.balls.append(Ellipse(pos=(x, y), size=(4, 4)))
        self.bind(pos=self.update)
        self.n = 0

    def update(self, dt):
        self.n += 1
        for i in range(24):
            x = 69 + 5 * i
            y = 56 + 20 * cos(self.n * (self.ball_factors[i] / 30))
            self.balls[i].pos = (x, y)


class AnimationApp(App):

    def build(self):
        game = Animation()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    AnimationApp().run()
