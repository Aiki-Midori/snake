import pygame as pg, sys, random

pg.init() #this is like starting the engine of a car
screen = pg.display.set_mode((600, 600)) #creates the window
clock = pg.time.Clock()


FPS = 14
blockx = 10
blocky = 0
size = 20
score = 0

# head
snake_surf = pg.Surface((size, size))
snake_surf.fill((50, 100, 255))
snake_rect = snake_surf.get_rect(center=(300, 300))

# segment
seg_list = [[snake_surf, snake_rect]]


def new_seg(c_pos):
  seg_surf = pg.Surface((size, size))
  seg_surf.fill((70, 100, 255))
  seg_rect = seg_surf.get_rect(center=c_pos)
  return [seg_surf, seg_rect]

# food
def new_food_pos(): 
  return (random.randint(0, 55) * 10, random.randint(0, 55) * 10)

food_list = []
food_pos = new_food_pos()
food_surf = pg.Surface((size, size))
food_surf.fill("Red")
food_list.append(food_surf)

# -------------------MAIN LOOP------------------- #
while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit() 
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_LEFT: blockx, blocky = -10, 0
      if event.key == pg.K_RIGHT: blockx, blocky = 10, 0
      if event.key == pg.K_DOWN: blockx, blocky = 0, 10
      if event.key == pg.K_UP: blockx, blocky = 0, -10

  screen.fill((100, 200, 100))

  for food in food_list: screen.blit(food, food.get_rect(center=food_pos))

  for i, seg in enumerate(seg_list):
    if i == 0:   
      screen.blit(snake_surf, snake_rect) #head
    elif i > 0:
      screen.blit(seg[0], seg_list[i-1][1]) #body
    print(seg[1].center)

  snake_rect.centerx += blockx
  snake_rect.centery += blocky

  if snake_rect.collidepoint(food_pos):
    food_pos = new_food_pos()
    food_list.pop(0)
    food_list.append(food_surf)
    seg_list.append(new_seg())

  # print(snake_rect.center, len(seg_list))

  pg.display.update()
  clock.tick(FPS)


# make snake head move block by block
# control the snake
# create food, spawn it in random blocks
# add new segments when snake eats/collides with food
# get coords of each segment
# each segments follow the head by moving the segment to the prev pos of the preceeding segment
