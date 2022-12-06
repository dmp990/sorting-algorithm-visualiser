import random

from information import *

pygame.init()


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

    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            ...
