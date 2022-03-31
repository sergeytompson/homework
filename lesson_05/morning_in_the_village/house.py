import simple_draw as sd
START_HOUSE = 200
WIDTH_HOUSE = 480
HEIGHT_HOUSE = 300


def wall(ground_level, x=START_HOUSE, width=WIDTH_HOUSE, height=HEIGHT_HOUSE, brick_height=20):
    y = ground_level
    left_bottom = sd.get_point(x, y)
    right_top = sd.get_point(x + width, y + height)
    sd.rectangle(left_bottom, right_top, width=2)
    for i in range(y + 20, height + y, 20):
        start_point = sd.get_point(x, i)
        finish_point = sd.get_point(x + width, i)
        sd.line(start_point, finish_point)
    for i in range(y, height + y, brick_height):
        for j in range(x, width + x, brick_height * 2):
            if (i - y) % (brick_height * 2) == 0:
                start_point = sd.get_point(j + brick_height, i)
                finish_point = sd.get_point(j + brick_height, i + brick_height)
            else:
                start_point = sd.get_point(j, i)
                finish_point = sd.get_point(j, i + brick_height)
            sd.line(start_point, finish_point)


def window(x=450, y=150, width=100, height=120):
    left_bottom = sd.get_point(x, y)
    right_top = sd.get_point(x + width, y + height)
    sd.rectangle(left_bottom, right_top, sd.background_color)
    sd.rectangle(left_bottom, right_top, width=4)


def roof(ground_level, deviation=20, height=100):
    base_y = HEIGHT_HOUSE + ground_level
    first_point = sd.get_point(START_HOUSE - deviation, base_y)
    second_point = sd.get_point(START_HOUSE + deviation + WIDTH_HOUSE, base_y)
    third_point = sd.get_point(START_HOUSE + (deviation + WIDTH_HOUSE) // 2, base_y + height)
    points = [first_point, second_point, third_point]
    sd.polygon(points, color=sd.COLOR_DARK_ORANGE, width=0)
#  good !
