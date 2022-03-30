import simple_draw as sd
from morning_in_the_village.weather import snow, snow_delete
from morning_in_the_village import GROUND_LEVEL
sd.resolution = (1200, 600)

SNOWFLAKES_AMOUNT = 1
snowflakes_params = [[sd.random_number(100, 1100), sd.random_number(100, 600), sd.random_number(10, 30)]
                     for _ in range(SNOWFLAKES_AMOUNT)]
dropped_out_snowflakes = []
while True:
    sd.start_drawing()
    snow_delete(snowflakes_params)
    snow(snowflakes_params, dropped_out_snowflakes, GROUND_LEVEL)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
