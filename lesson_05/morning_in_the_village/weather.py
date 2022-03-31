import simple_draw as sd


def rainbow(rainbow_colors):
    step = 0
    for color in rainbow_colors:
        centre = sd.get_point(-400 + step, -400 + step)
        sd.circle(centre, 1700, color, 5)
        step += 4
    last_color = rainbow_colors.pop(0)
    rainbow_colors.append(last_color)


def snow(snowflakes_params, dropped_out_snowflakes, ground_level):
    for snowflake in snowflakes_params:
        if snowflake[1] <= snowflake[2] + ground_level:
            dropped_out_snowflakes.append(snowflake)
            index = snowflakes_params.index(snowflake)
            snowflakes_params[index] = [sd.random_number(50, 1150), 600,
                                        sd.random_number(10, 30)]
        snowflake[1] -= sd.random_number(1, 15)
        snowflake[0] += sd.random_number(-15, 15)
        current_point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(current_point, snowflake[2])
        for dropped_snowflake in dropped_out_snowflakes:
            current_point = sd.get_point(dropped_snowflake[0], dropped_snowflake[1])
            sd.snowflake(current_point, dropped_snowflake[2])


def snow_delete(snowflakes_params):
    for snowflake in snowflakes_params:
        current_point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(current_point, snowflake[2], sd.background_color)


def sun(angle, rays_list):
    centre = sd.get_point(100, 500)
    sd.circle(centre, width=0)
    step = 0
    for _ in range(10):
        sd.vector(centre, angle + step, 100, width=3)
        ray = [centre, angle + step]
        rays_list.append(ray)
        step += 36


def delete_rays(rays_list):
    for ray in rays_list:
        sd.vector(ray[0], ray[1], 100, sd.background_color, 3)
#  good !
