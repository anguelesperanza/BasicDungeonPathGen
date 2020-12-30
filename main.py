
# The following modules are needed to run the program

import pyglet
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640


window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_WIDTH)

room_batch = pyglet.graphics.Batch()
grid_batch = pyglet.graphics.Batch()

grid_image_list = []
grid_coor = []
walk_path = []

# 1 = left | 2 = up | 3 = right | 4 = down | stop 
walk_dir = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,0]
# This will hold all coordinates of an area that has already been assigned as 'room' (walk)
# We will use this to make sure we don't overlap areas
walk_coor = []



def make_grid():

    # The purpose of this method is to make a grid to display on the pyglet window
    # This makes things easy to look at
    # And it also get's our coordinates as tuples (x,y) and stores them in the grid_coor[] list

    global grid_batch

    grid_square_x = grid_square_y = 0
    grid_square_width = grid_square_height = 32;
    # current_grid_square = 0
    grid_square = pyglet.resource.image('grid.png')


    grid_done = False
    while grid_done == False:


        
        if grid_square_x < WINDOW_WIDTH:
            grid_coor.append((grid_square_x, grid_square_y))
            temp = pyglet.sprite.Sprite(grid_square, grid_square_x, grid_square_y, batch = grid_batch)
            grid_image_list.append(temp)
            grid_square_x = grid_square_x + grid_square_width

        else:

            if grid_square_y < WINDOW_HEIGHT:
                grid_square_x = 0
                grid_square_y =  grid_square_y + grid_square_height
                grid_coor.append((grid_square_x, grid_square_y))

            else:
                grid_done = True


def make_path():

    # This is the Drunkard Walk Algorithm
    # This code does not allow for the algorithm to:
    #   A) Walk off screen
    #   B) Walk on a path that has already been walked
    walk_square = pyglet.resource.image('path.png')
    end_square = pyglet.resource.image('end.png')
    start_square = pyglet.resource.image('start.png')


    # This is a flag to tell the program to stop walking
    walk_done = False

    # This picks a random spot on the grid as the algorithm's starting part
    start_pos = random.randint(0, len(grid_coor) - 1)
    start_pos_x = grid_coor[start_pos][0]
    start_pos_y = grid_coor[start_pos][1]

    # The size of our tiles and each grid square
    tile_width = 32;
    tile_height = 32;

    
    # The intial start square is not included in the loop for the walk path
    # These lines make sure the initial start square does start off screen
    if (start_pos_x >= WINDOW_WIDTH):
        start_pos_x = start_pos_x - tile_width
    if (start_pos_y >= WINDOW_HEIGHT):
        start_pos_y = start_pos_y - tile_height

    # Here we add the first walk square
    walk_coor.append((start_pos_x, start_pos_y))

    temp = pyglet.sprite.Sprite(start_square, start_pos_x, start_pos_y, batch = room_batch)
    walk_path.append(temp)
    print(grid_coor[start_pos][0], grid_coor[start_pos][1])

    while walk_done == False:
        random_walk_dir = random.randint(0, len(walk_dir) - 1)
        random_walk_dir = walk_dir[random_walk_dir]

        if random_walk_dir == 1:
            print("Attempting to go left:", random_walk_dir)
            # If we are at the left most edge of the grid, don't do anything

            if (start_pos_x - tile_width, start_pos_y) in walk_coor:
                print('       Path found already. Cannot go left')

            else:
                if (start_pos_x - tile_width < 0):
                    print("       Edge of map. Cannot go left")
                else:
                    start_pos_x = start_pos_x - tile_width
                    temp = pyglet.sprite.Sprite(walk_square, start_pos_x, start_pos_y, batch = room_batch)
                    walk_path.append(temp)
                    walk_coor.append((start_pos_x, start_pos_y))
                # walk_done = True

        elif random_walk_dir == 2:
            print('Attempting to go up', random_walk_dir)
            # If we are at the left most edge of the grid, don't do anything
            if (start_pos_x, start_pos_y + tile_height) in walk_coor:
                print('       Path found already. Cannot go up.')

            else:
                    
                if (start_pos_y + tile_height >= WINDOW_HEIGHT):
                    print("       Edge of map. Cannot go Up")
                else:
                    start_pos_y = start_pos_y + tile_height
                    temp = pyglet.sprite.Sprite(walk_square, start_pos_x, start_pos_y, batch = room_batch)
                    walk_path.append(temp)
                    walk_coor.append((start_pos_x, start_pos_y))
            

        elif random_walk_dir == 3:
            print('Attempting to go  right', random_walk_dir)
            # If we are at the left most edge of the grid, don't do anything

            if (start_pos_x + tile_width, start_pos_y) in walk_coor:
                print('       Path found already. Cannot go right')
            else:
                if (start_pos_x + tile_width >= WINDOW_WIDTH):
                    print("       Edge of map. Cannot go right")
                else:
                    start_pos_x = start_pos_x + tile_width
                    temp = pyglet.sprite.Sprite(walk_square, start_pos_x, start_pos_y, batch = room_batch)
                    walk_path.append(temp)
                    walk_coor.append((start_pos_x, start_pos_y))

        elif random_walk_dir == 4:
            print('Attempting to go down', random_walk_dir)
            # If we are at the left most edge of the grid, don't do anything
            if (start_pos_x, start_pos_y - tile_height) in walk_coor:
                print('       Path found already. Cannot go down')

            else:

                if (start_pos_y - tile_height < 0):
                    print("       Edge of map. Cannot go down")
                else:
                    start_pos_y = start_pos_y - tile_height
                    temp = pyglet.sprite.Sprite(walk_square, start_pos_x, start_pos_y, batch = room_batch)
                    walk_path.append(temp)
                    walk_coor.append((start_pos_x, start_pos_y))
        else:
            print('end found')
            temp = pyglet.sprite.Sprite(end_square, start_pos_x, start_pos_y, batch = room_batch)
            walk_path.append(temp)
            walk_coor.append((start_pos_x, start_pos_y))
            walk_done = True

@window.event
def on_draw():
    # pass
    grid_batch.draw()
    room_batch.draw()

def main():
    make_grid()
    make_path()
    pyglet.app.run()


if __name__=="__main__":
    main()