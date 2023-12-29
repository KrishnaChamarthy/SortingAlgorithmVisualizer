import random

import pygame
from node import Node

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Algorithm Visualizer')

font = pygame.font.SysFont('Arial', 30)
large_font = pygame.font.SysFont('Arial', 40)


def title_label():
    title = large_font.render('ALGORITHM VISUALIZER', 1, (255, 0, 0))
    WIN.blit(title, (WIN.get_width()/2 - title.get_width()/2, 5))


def options():
    options_text = font.render('A - ASCENDING | D - DESCENDING | SPACE - START | R - RESET', 1, (0, 0, 0))
    WIN.blit(options_text, (WIN.get_width()/2 - options_text.get_width()/2, 50))
    sort_options = font.render('B - BUBBLE SORT | S - SELECTION SORT', 1, (0, 0, 0))
    WIN.blit(sort_options, (WIN.get_width()/2 - sort_options.get_width()/2, 80))


def sort_label(ascending, sort):
    if ascending:
        asc = 'Ascending'
    else:
        asc = 'Descending'
    if sort == 0:
        st = 'Bubble Sort'
    else:
        st = 'Selection Sort'
    sort_text = font.render(f'{asc} {st}', 1, (0, 0, 255))
    WIN.blit(sort_text, (WIN.get_width()/2 - sort_text.get_width()/2, 110))
    pygame.draw.rect(WIN, (0, 0, 0), (0, 150, WIDTH, 10))


def create_array():
    arr = []
    gradient = [(200, 200, 200), (100, 100, 100), (140, 140, 140), (180, 180, 180), (120, 120, 120), (160, 160, 160)]
    for i in range(40):
        arr.append(Node(i, random.randint(10, 40), gradient[i % 6]))
    return arr


def draw_array(arr):
    for num in arr:
        num.draw(WIN)


def bubble_sort(ascending, arr):
    if ascending:
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1):
                if arr[j].num > arr[j+1].num:
                    c1 = arr[j].color
                    c2 = arr[j+1].color
                    arr[j].change_color((200, 0, 0))
                    arr[j+1].change_color((255, 0, 0))
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    arr[j].x, arr[j + 1].x = arr[j + 1].x, arr[j].x
                    WIN.fill((255, 255, 255))
                    draw_labels(ascending, 0)
                    draw_array(arr)
                    pygame.display.update()
                    pygame.time.wait(50)
                    arr[j].change_color(c2)
                    arr[j+1].change_color(c1)
    else:
        for i in range(len(arr)-1, 0, -1):
            for j in range(len(arr)-1, 0, -1):
                if arr[j].num > arr[j-1].num:
                    c1 = arr[j].color
                    c2 = arr[j-1].color
                    arr[j].change_color((200, 0, 0))
                    arr[j-1].change_color((255, 0, 0))
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    arr[j].x, arr[j - 1].x = arr[j - 1].x, arr[j].x
                    WIN.fill((255, 255, 255))
                    draw_labels(ascending, 0)
                    draw_array(arr)
                    pygame.display.update()
                    pygame.time.wait(50)
                    arr[j].change_color(c2)
                    arr[j-1].change_color(c1)
    return arr


def selection_sort(ascending, arr):
    if ascending:
        for i in range(len(arr) - 1):
            min_ele = i
            for j in range(i+1, len(arr)):
                if arr[j].num < arr[min_ele].num:
                    min_ele = j

            if min_ele != i:
                c1 = arr[i].color
                c2 = arr[min_ele].color
                arr[i].change_color((200, 0, 0))
                arr[min_ele].change_color((255, 0, 0))
                arr[i], arr[min_ele] = arr[min_ele], arr[i]
                arr[i].x, arr[min_ele].x = arr[min_ele].x, arr[i].x
                WIN.fill((255, 255, 255))
                draw_labels(ascending, 1)
                draw_array(arr)
                pygame.display.update()
                pygame.time.wait(100)
                arr[i].change_color(c2)
                arr[min_ele].change_color(c1)
    else:
        for i in range(len(arr) - 1, 0, -1):
            min_ele = i
            for j in range(i-1, -1, -1):
                if arr[j].num < arr[min_ele].num:
                    min_ele = j

            if min_ele != i:
                c1 = arr[i].color
                c2 = arr[min_ele].color
                arr[i].change_color((200, 0, 0))
                arr[min_ele].change_color((255, 0, 0))
                arr[i], arr[min_ele] = arr[min_ele], arr[i]
                arr[i].x, arr[min_ele].x = arr[min_ele].x, arr[i].x
                WIN.fill((255, 255, 255))
                draw_labels(ascending, 1)
                draw_array(arr)
                pygame.display.update()
                pygame.time.wait(100)
                arr[i].change_color(c2)
                arr[min_ele].change_color(c1)
    return arr


def solve(ascending, sort, arr):
    if sort == 0:
        return bubble_sort(ascending, arr)
    else:
        return selection_sort(ascending, arr)


def draw_labels(ascending,sort):
    title_label()
    options()
    sort_label(ascending, sort)


def main():
    run = True
    clock = pygame.time.Clock()
    ascending = True
    sort = 0
    arr = create_array()
    while run:
        clock.tick(FPS)
        WIN.fill((255, 255, 255))
        draw_labels(ascending, sort)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    ascending = True
                if event.key == pygame.K_d:
                    ascending = False
                if event.key == pygame.K_b:
                    sort = 0
                if event.key == pygame.K_s:
                    sort = 1
                if event.key == pygame.K_SPACE:
                    arr = solve(ascending, sort, arr)
                if event.key == pygame.K_r:
                    arr = create_array()
        draw_array(arr)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
