import pygame

class Information:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    SIDE_PADDING = 100
    TOP_PADDING = 100

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption=("Sorting Algorithms")
        self.set_list(lst)

        def set_list(self, lst):
            self.lst = lst
            self.max_val = max(lst)
            self.min_val = min(lst)
            self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
            self.block_height = round((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
            self.start_x = self.SIDE_PAD // 2
            

