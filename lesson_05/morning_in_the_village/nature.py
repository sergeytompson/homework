import simple_draw as sd


def smile(wink_cnt, x=500, y=210):
    start_point = sd.get_point(x - 50, y - 30)
    finish_point = sd.get_point(x + 50, y + 30)
    sd.ellipse(start_point, finish_point, width=1)
    points = [sd.get_point(x - 20, y - 10), sd.get_point(x - 10, y - 18), sd.get_point(x + 10, y - 18),
              sd.get_point(x + 20, y - 10)]
    sd.lines(points)
    point = sd.get_point(x - 15, y + 10)
    sd.circle(point, 5)
    point = sd.get_point(x + 15, y + 10)
    sd.circle(point, 5)
    if wink_cnt >= 6:
        first_point = sd.get_point(x - 20, y + 10)
        second_point = sd.get_point(x - 10, y + 15)
        sd.rectangle(first_point, second_point, sd.background_color)


def draw_branches(start_point, angle, length, lst, deviation=30):
    thickness = 4
    color = sd.COLOR_DARK_ORANGE
    if length < 50:
        thickness = 3
    if length < 25:
        thickness = 2
    if length < 10:
        thickness = 1
        color = sd.COLOR_GREEN
    if length < 2:
        return
    angle_deviation = sd.random_number(-40, 40) / 100
    length_deviation = sd.random_number(-20, 20) / 100
    first_angle = angle + deviation + (deviation * angle_deviation)
    second_angle = angle - deviation + (deviation * angle_deviation)
    first_branch = sd.get_vector(start_point, first_angle, length, thickness)
    lst.append([first_branch, color])
    second_branch = sd.get_vector(start_point, second_angle, length, thickness)
    lst.append([second_branch, color])
    first_end = first_branch.end_point
    second_end = second_branch.end_point
    length *= 0.75 + (0.75 * length_deviation)
    draw_branches(first_end, first_angle, length, lst)
    draw_branches(second_end, second_angle, length, lst)
    return lst


def tree(ground_level, angle=90, height=100, x=900):
    start_trunc = sd.get_point(x, ground_level)
    trunc = sd.get_vector(start_trunc, angle, height, 5)
    color = sd.COLOR_DARK_ORANGE
    tree_list = [[trunc, color]]
    end_trunc = trunc.end_point
    branch_length = height * 0.75
    lst = draw_branches(end_trunc, angle, branch_length, tree_list)
    return lst


def ground(ground_level):
    start_point = sd.get_point(0, 0)
    finish_point = sd.get_point(1200, ground_level)
    sd.rectangle(start_point, finish_point, sd.COLOR_DARK_ORANGE)
#  good !
