# Tommy and Noah
# tkm2uft
# syr4gv

import uvage as gamebox

camera = gamebox.Camera(800, 600)
road = gamebox.from_image(400,600,"road.png")

sheet = gamebox.load_sprite_sheet("car.png", 3, 6)
car = gamebox.from_image(400, 400, sheet[3])

car_speed = -15

def tick():
    global road
    camera.draw(road)
    camera.draw(car)
    camera.display()
    camera.move(0, -15)
    if camera.y <= -1000:
        camera.y = 0
        car.y = 110
    car.speedy = car_speed
    car.move_speed()
    if gamebox.is_pressing("right arrow"):
        car.x += 10
    if gamebox.is_pressing("left arrow"):
        car.x -= 10

gamebox.timer_loop(30, tick)
