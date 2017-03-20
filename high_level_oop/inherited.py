#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    pass


class Mammal(object):
    pass


class Bird(object):
    pass


class RunnableMixIn(object):
    def run(self):
        print(self.__sizeof__()+'Running...')


class FlyableMixIn(object):
    def fly(self):
        print(self.__sizeof__()+'Flying...')


class CarnivorousMixIn(object):
    pass


class HerbivoresMixIn(object):
    pass


# MixIn 多重继承 目的就是给一个类增加多个功能 通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass










