import simple_draw as sd

_snowflakes_list = []


def snowflakes_creation(amount):
    global _snowflakes_list
    for _ in range(amount):
        _snowflakes_list.append([sd.random_number(50, 1150), 615, sd.random_number(10, 30)])


def draw_snowflakes(color=sd.COLOR_WHITE):
    for snowflake in _snowflakes_list:
        current_point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(current_point, snowflake[2], color)


def move_snowflakes():
    global _snowflakes_list
    for snowflake in _snowflakes_list:
        snowflake[1] -= sd.random_number(1, 15)
        snowflake[0] += sd.random_number(-15, 15)


def went_abroad():
    global _snowflakes_list
    cnt = 0
    dropped_set = set()
    for snowflake in _snowflakes_list:
        if 0 - snowflake[2] >= snowflake[0] >= 1200 + snowflake[2] or snowflake[1] <= 0 - snowflake[2] * 2:
            dropped_set.add(cnt)
        cnt += 1
    return dropped_set


def delete_snowflakes(snowflakes_set):
    global _snowflakes_list
    cnt = 0
    for i in snowflakes_set:
        del _snowflakes_list[i - cnt]
        cnt += 1
