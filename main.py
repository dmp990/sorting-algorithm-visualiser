import random

from information import *

pygame.init()

def draw(draw_info: Information):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()

def generate_list(n: int, min_val: int, max_val: int) -> list:
    """
    returns a list of n random integers from min_val to max_val
    """
    lst = []
    for _ in range(n):
        lst.append(random.randint(min_val, max_val))
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    lst = generate_list(n, min_val, max_val)

    draw_info = Information(800, 600, lst)

    while run:
        clock.tick(60)

        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()