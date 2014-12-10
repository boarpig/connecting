#!/usr/bin/python
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.vector import Vector
from math import cos
from numpy import linspace


class Animation(Widget):

    def __init__(self, **kwargs):
        super(Animation, self).__init__(**kwargs)
        self.ball_factors = list(linspace(1, 4, 24))
        self.n = 0

    def update(self, dt):
        self.canvas.clear()
        self.n += 1
        with self.canvas:
            Color(1, 0, 0)
            for i in range(24):
                Ellipse(pos=(20 +10 * i, 100 + 50 * cos(self.n * (self.ball_factors[i] / 30))), size=(5, 5))


class AnimationApp(App):

    def build(self):
        game = Animation(size_hint=(1, 1))
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    AnimationApp().run()
