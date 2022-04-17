import simple_draw as sd

_snowflakes_list = []


def snowflakes_creation(amount: int) -> None:
    global _snowflakes_list
    for _ in range(amount):
        _snowflakes_list.append([sd.random_number(50, 1150), 615, sd.random_number(10, 30)])


def draw_snowflakes(color: (int, int, int) = sd.COLOR_WHITE) -> None:
    for snowflake in _snowflakes_list:
        current_point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(current_point, snowflake[2], color)


def move_snowflakes() -> None:
    global _snowflakes_list
    for snowflake in _snowflakes_list:
        snowflake[1] -= sd.random_number(1, 15)
        snowflake[0] += sd.random_number(-15, 15)


def went_abroad() -> set:
    global _snowflakes_list
    dropped_set = set()
    for i in range(len(_snowflakes_list)):
        snowflake = _snowflakes_list[i]
        if 0 - snowflake[2] >= snowflake[0] >= sd.resolution[0] + snowflake[2]:
            dropped_set.add(i)
        elif snowflake[1] <= 0 - snowflake[2] * 2:
            dropped_set.add(i)
    return dropped_set


def delete_snowflakes(snowflakes_set: set) -> None:
    global _snowflakes_list
    snowflakes_list = sorted(snowflakes_set, reverse=True)
    for i in snowflakes_list:
        _snowflakes_list.pop(i)
