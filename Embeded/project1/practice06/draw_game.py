import pygame
import sys

# 색깔
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 그리기 모드
DRAW = 0
ERASE = 1

class Paint:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Simple Paint")
        self.clock = pygame.time.Clock()

        self.draw_mode = DRAW
        self.brush_size = 5
        self.color = BLACK

        self.running = True
        self.draw_surface = pygame.Surface((800, 600))
        self.draw_surface.fill(WHITE)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_e:
                        self.draw_mode = ERASE if self.draw_mode == DRAW else DRAW
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # scroll up
                        self.brush_size += 1
                    elif event.button == 5:  # scroll down
                        self.brush_size -= 1 if self.brush_size > 1 else 0
                    else:
                        self.draw(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:
                        self.draw(event.pos)

            self.update()
            self.clock.tick(60)

    def draw(self, pos):
        if self.draw_mode == DRAW:
            pygame.draw.circle(self.draw_surface, self.color, pos, self.brush_size)
        elif self.draw_mode == ERASE:
            pygame.draw.circle(self.draw_surface, WHITE, pos, self.brush_size)

    def update(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.draw_surface, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    app = Paint()
    app.run()
    pygame.quit()
    sys.exit()
