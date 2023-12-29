import pygame


class Node:
    def __init__(self, pos, num, color):
        self.pos = pos
        self.num = num
        self.color = color
        self.x = 0
        self.y = 160
        self.height = 0
        self.get_pos()

    def get_pos(self):
        self.x = 100 + (self.pos * 15)
        self.height = self.num * 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 15, self.height))

    def change_color(self, color):
        self.color = color
