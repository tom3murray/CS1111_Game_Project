# Tommy and Noah
# tkm2uft
# syr4gv

import uvage as gamebox
import random

camera = gamebox.Camera(800, 600)
a_road = gamebox.from_image(400,600,"a_road.png")
a_road.width = 800
b_road = gamebox.from_image(400,6300,"b_road.png")
b_road.width = 800
roads = [a_road, b_road]

sheet = gamebox.load_sprite_sheet("car.png", 1, 3)
player_car = gamebox.from_image(400, 500, sheet[2])
player_car.scale_by(.25)

car_speed = -15

left_wall = gamebox.from_color(0, 0, 'white', 0, 10000)
right_wall = gamebox.from_color(718, 0, 'white', 0, 10000)

r_white_car = gamebox.from_image(400,0,"white_car.png")
r_white_car.scale_by(.307)
r_yellow_car = gamebox.from_image(400,-100,"yellow_car.png")
r_yellow_car.scale_by(0.23453608)
r_red_car = gamebox.from_image(400,-200,"red_car.png")
r_red_car.scale_by(0.22377049)
r_pink_car = gamebox.from_image(400,-300,"pink_car.png")
r_pink_car.scale_by(0.273)
r_gray_car = gamebox.from_image(400,-400,"gray_car.png")
r_gray_car.scale_by(0.25657894)
r_blue_car = gamebox.from_image(400,-500,"blue_car.png")
r_blue_car.scale_by(0.13074712)

right_lane_cars = [r_white_car,r_yellow_car,r_red_car,r_pink_car,r_gray_car,r_blue_car]

l_white_car = gamebox.from_image(130,-100,"white_car.png")
l_white_car.rotate(180)
l_white_car.scale_by(.307)
l_yellow_car = gamebox.from_image(130,-200,"yellow_car.png")
l_yellow_car.rotate(180)
l_yellow_car.scale_by(0.23453608)
l_red_car = gamebox.from_image(130,-300,"red_car.png")
l_red_car.rotate(180)
l_red_car.scale_by(0.22377049)
l_pink_car = gamebox.from_image(130,-400,"pink_car.png")
l_pink_car.rotate(180)
l_pink_car.scale_by(0.273)
l_gray_car = gamebox.from_image(130,-500,"gray_car.png")
l_gray_car.rotate(180)
l_gray_car.scale_by(0.25657894)
l_blue_car = gamebox.from_image(130,-600,"blue_car.png")
l_blue_car.rotate(180)
l_blue_car.scale_by(0.13074712)

left_lane_cars = [l_white_car,l_yellow_car,l_red_car,l_pink_car,l_gray_car,l_blue_car]

a_crater = gamebox.from_image(0,800,"crater.png")
a_crater.scale_by(.125)
b_crater = gamebox.from_image(0,1000,"crater.png")
b_crater.scale_by(.125)
a_nails = gamebox.from_image(0,1200,"nails.png")
a_nails.scale_by(.06)
b_nails = gamebox.from_image(0,1400,"nails.png")
b_nails.scale_by(.06)
a_puddle = gamebox.from_image(0,1600,"puddle.png")
a_puddle.scale_by(.173)
b_puddle = gamebox.from_image(0,1800,"puddle.png")
b_puddle.scale_by(.173)


coins = []
for x in range(5):
    randy = random.randint(0, 717)
    randx = random.randint(0, 400)
    randx*=-1
    coins.append(gamebox.from_image(randy, randx, "coins.jpg"))
for coin in coins:
    coin.scale_by(.05)

coinnum = 0


terrain_hazards = [a_crater, b_crater, a_nails, b_nails, a_puddle, b_puddle]
hazard_domain = [(0,130),(600,718)]

all_enemies = left_lane_cars + right_lane_cars + terrain_hazards

life1 = gamebox.from_image(750,10,"heart.png")
life1.width = 20
life2 = gamebox.from_image(750,40,"heart.png")
life2.width = 20
life3 = gamebox.from_image(750,70,"heart.png")
life3.width = 20

int_current_score = 0

game_over = gamebox.from_text(camera.x, camera.y, 'GAME OVER', 100, "red")
game_over_bool = False

def right_lane_traffic(li_cars):
    '''
    Creates and draws cars to populate the right lane
    :param li_cars: The list of right lane car sprites
    :return: No return
    '''
    for bot_car in li_cars:
        bot_car.y += 5
        if bot_car.y > 800:
            random_x = random.randint(400,600)
            bot_car.x = random_x
            random_y = random.randint(-1000,-200)
            bot_car.y = random_y
        for other_bot_car in li_cars:
            if bot_car != other_bot_car:
                bot_car.move_to_stop_overlapping(other_bot_car)
        camera.draw(bot_car)
        
def left_lane_traffic(li_cars):
    '''
    Creates and draws the left lane cars
    :param li_cars: A list of cars meant to populate the left lane
    :return:
    '''
    for bot_car in li_cars:
        bot_car.y += 20
        if bot_car.y > 800:
            random_x = random.randint(130,330)
            bot_car.x = random_x
            random_y = random.randint(-1000,-200)
            bot_car.y = random_y
        for other_bot_car in li_cars:
            if bot_car != other_bot_car:
                bot_car.move_to_stop_overlapping(other_bot_car)
        camera.draw(bot_car)

def hazards(li_hazards):
    '''
    Places hazards along the side of the road
    :param li_hazards: The list of hazards
    :return: No return
    '''
    global hazard_domain

    for hazard in li_hazards:
        hazard.y += 10
        if hazard.y > 800:
            random_x_range = random.choice(hazard_domain)
            random_x = random.randint(random_x_range[0],random_x_range[1])
            hazard.x = random_x
            random_y = random.randint(-1000,-200)
            hazard.y = random_y
        for other_hazard in li_hazards:
            if hazard != other_hazard:
                hazard.move_to_stop_overlapping(other_hazard)
        camera.draw(hazard)

def coin_maker():
    '''
    Places, removes, and moves coins and creates new coins
    :return:
    '''
    global coinnum
    global coins
    coin_counter = gamebox.from_text(760, 525, str(coinnum), 50, "yellow")
    camera.draw(coin_counter)
    for coin in coins:
        camera.draw(coin)
        coin.y += 3
        if player_car.touches(coin):
            coinnum += 1
        if player_car.touches(coin) or coin.y >= 600:
            coins.remove(coin)
            rand = random.randint(0, 717)
            c = gamebox.from_image(rand, 0, "coins.jpg")
            c.scale_by(.05)
            coins.append(c)



def life_taker():
    '''
    Removes a heart when an obstacle is hit, and displays a game over when hearts reach zero, as well as stopping the
    game
    :return:
    '''
    global all_enemies
    global game_over
    global game_over_bool

    for enemy in all_enemies:
        if player_car.touches(enemy):
            enemy.y = 1000
            if life3.y > 1000:
                if life2.y > 1000:
                    life1.y = 1100
                    camera.draw(game_over)
                    game_over_bool = True
                else:
                    life2.y = 1100
            else: life3.y = 1100
    camera.draw(life1)
    camera.draw(life2)
    camera.draw(life3)

def score_keeper():
    '''
    Ups the score by one every tick and displays
    :return:
    '''
    global int_current_score
    int_current_score += 1
    str_current_score = str(int_current_score)
    score = gamebox.from_text(760, 575, str_current_score, 50, "red")
    camera.draw(score)

def tick():
    '''
    If it is not game_over, allows car movement left and right, as well as stopping collision with sides, and uses all
    helper functions
    :return:
    '''
    camera.clear('blue')
    if game_over_bool == False:
        for road in roads:
            road.y += 10
            camera.draw(road)
            if road.top >= 0:
                road.y -= 5500

        if gamebox.is_pressing("right arrow"):
            player_car.image = sheet[0]
            player_car.x += 10
        elif gamebox.is_pressing("left arrow"):
            player_car.image = sheet[1]
            player_car.x -= 10
        else:
            player_car.image = sheet[2]

        if player_car.touches(left_wall):
            player_car.move_to_stop_overlapping(left_wall)
        if player_car.touches(right_wall):
            player_car.move_to_stop_overlapping(right_wall)

        right_lane_traffic(right_lane_cars)

        left_lane_traffic(left_lane_cars)

        hazards(terrain_hazards)

        score_keeper()

        life_taker()

        coin_maker()

        camera.draw(player_car)
        camera.display()

gamebox.timer_loop(30, tick)
