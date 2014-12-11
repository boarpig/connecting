#!/usr/bin/python
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Color, Ellipse
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from math import cos
from numpy import linspace

Config.set('graphics', 'width', '256')
Config.set('graphics', 'height', '144')


class Animation(FloatLayout):

    def __init__(self, **kwargs):
        super(Animation, self).__init__(**kwargs)
        self.ball_factors = list(linspace(1, 4, 24))
        self.balls = []
        self.label = ""
        with self.canvas:
            Color(0.04296875, 0.37109375, 0.58203125)
            for i in range(24):
                x = 69 + 5 * i
                y = 56
                self.balls.append(Ellipse(pos=(x, y), size=(4, 4)))
            self.label = Label(text="Connecting to Prismata...",
                               color=(0.04296875, 0.37109375, 0.58203125, 1),
                               pos=(75, 56), font_size='12pt',
                               markup=True)
        self.bind(pos=self.update)
        self.n = 0

    def update(self, dt):
        self.n += 1
        for i in range(24):
            x = 69 + 5 * i
            y = 56 + 20 * cos(self.n * (self.ball_factors[i] / 15))
            self.balls[i].pos = (x, y)


class AnimationApp(App):

    def build(self):
        game = Animation()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    AnimationApp().run()
