# Tommy and Noah
# tkm2uft
# syr4gv

import uvage as gamebox

camera = gamebox.Camera(800, 600)
road = gamebox.from_image(400,600,"road.png")
road.width = 800

sheet = gamebox.load_sprite_sheet("car.png", 1, 3)
car = gamebox.from_image(400, 500, sheet[2])
car.scale_by(.25)

car_speed = -15

left_wall = gamebox.from_color(0, 0, 'white', 0, 10000)
right_wall = gamebox.from_color(800, 0, 'white', 0, 10000)

def tick():
    global road

    camera.clear('blue')
    camera.draw(road)
    camera.draw(car)
    camera.display()

    camera.move(0, -15)
    car.speedy = car_speed
    car.move_speed()

    if camera.y <= -1000:
        camera.y = 0
        car.y = 215

    if gamebox.is_pressing("right arrow"):
        car.image = sheet[0]
        car.x += 15
    elif gamebox.is_pressing("left arrow"):
        car.image = sheet[1]
        car.x -= 15
    else:
        car.image = sheet[2]

    if car.touches(left_wall):
        car.move_to_stop_overlapping(left_wall)
    if car.touches(right_wall):
        car.move_to_stop_overlapping(right_wall)

gamebox.timer_loop(30, tick)