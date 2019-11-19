#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import random
import math

SCREEN_DIM = (1600, 900)


class Vec2d:
    """
    класс двумерных векторов
    """
    def __init__(self, coord):
        """конструктор принимает на вход кортеж координат вектора
        """
        self.xy = coord

    def __sub__(self, obj):
        """"возвращает разность двух векторов"""
        return Vec2d((self.xy[0] - obj.xy[0], self.xy[1] - obj.xy[1]))

    def __add__(self, obj):
        """возвращает сумму двух векторов"""
        return Vec2d((self.xy[0] + obj.xy[0], self.xy[1] + obj.xy[1]))

    def __mul__(self, obj):
        """возвращает произведение вектора на число или вектор"""
        if isinstance(obj, float) or isinstance(obj, int):
            return Vec2d((self.xy[0] * obj, self.xy[1] * obj))
        elif isinstance(obj, Vec2d):
            return self.xy[0] * obj.xy[0] + self.xy[1] * obj.xy[1]
        else:
            raise ValueError("The second variable must be Vec2d or float or int, not {}".format(type(obj)))

    def len(self):
        """возвращает длину вектора"""
        return math.sqrt(self.xy[0] * self.xy[0] + self.xy[1] * self.xy[1])

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return self.xy


class Polyline:
    def __init__(self):
        self.points = list()
        self.speeds = list()
    
    def add_points(self, point):
        self.points.append(Vec2d(point))
        self.speeds.append(Vec2d((random.random() * 2, random.random() * 2)))

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].xy[0] > SCREEN_DIM[0] or self.points[p].xy[0] < 0:
                self.speeds[p] = Vec2d((- self.speeds[p].xy[0], self.speeds[p].xy[1]))
            if self.points[p].xy[1] > SCREEN_DIM[1] or self.points[p].xy[1] < 0:
                self.speeds[p] = Vec2d((self.speeds[p].xy[0], -self.speeds[p].xy[1]))

    @staticmethod
    def draw_points(points, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n].xy[0]), int(points[p_n].xy[1])),
                                 (int(points[p_n + 1].xy[0]), int(points[p_n + 1].xy[1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.xy[0]), int(p.xy[1])), width)


class Knot(Polyline):
    count = 35

    def __init__(self):
        super().__init__()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.curve = list()

    @staticmethod
    def get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + Knot.get_point(points, alpha, deg - 1) * (1 - alpha)

    @staticmethod
    def get_points(points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Knot.get_point(points, i * alpha))
        return res

    def add_points(self, point):
        super().add_points(point)
        self.curve = self.get_knot()

    def set_points(self):
        super().set_points()
        self.curve = self.get_knot()

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = list()
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(Knot.get_points(ptn, Knot.count))
        return res

    def del_point(self):
        if len(self.points) > 0:
            i = random.randint(0, len(self.points) - 1)
            del self.points[i]
            del self.speeds[i]
            self.curve = self.get_knot()

    def change_speed(self, mode):
        if mode == 'UP':
            for i in range(len(self.speeds)):
                self.speeds[i] += self.speeds[i] * 0.1
        elif mode == 'DOWN':
            for i in range(len(self.speeds)):
                self.speeds[i] -= self.speeds[i] * 0.1

    def draw(self):
        super().draw_points(self.points, color=self.color)
        super().draw_points(self.curve, style="line", color=self.color)


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = list()
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["S", "Switch between knots"])
    data.append(["A", "Add new knot"])
    data.append(["UP", "Increase the speed of the selected knot"])
    data.append(["DOWN", "Decrease the speed of the selected knot"])
    data.append(["DELETE", "Delete random point from the selected knot"])
    data.append(["", ""])
    data.append([str(Knot.count), "Current points"])
    data.append([str(knot_now + 1), "Selected knot"])
    data.append([str(len(knots)), "Amount of knots"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    knots = [Knot()]
    working = True
    line1 = Polyline()
    show_help = False
    pause = True
    hue = 0
    knot_now = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knots = [Knot()]
                    knot_now = 0
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_a:
                    knots.append(Knot())
                if event.key == pygame.K_KP_PLUS:
                    Knot.count += 1
                if event.key == pygame.K_UP:
                    knots[knot_now].change_speed('UP')
                if event.key == pygame.K_DOWN:
                    knots[knot_now].change_speed('DOWN')
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    Knot.count -= 1 if Knot.count > 1 else 0
                if event.key == pygame.K_s and len(knots) > 1:
                    if knot_now != len(knots) - 1:
                        knot_now += 1
                    else:
                        knot_now = 0
                if event.key == pygame.K_DELETE:
                    knots[knot_now].del_point()

            if event.type == pygame.MOUSEBUTTONDOWN:
                knots[knot_now].add_points(event.pos)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        for k in knots:
            k.draw()
            if not pause:
                k.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
