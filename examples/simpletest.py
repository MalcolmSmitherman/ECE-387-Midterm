import time
import board
import busio
import adafruit_mma8451

i2c = busio.I2C(board.SCL, board.SDA)


sensor = adafruit_mma8451.MMA8451(i2c)

# Main loop to print the acceleration and orientation every second.
while True:
    x, y, z = sensor.acceleration
    print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
    orientation = sensor.orientation

    print('Orientation: ', end='')
    if orientation == adafruit_mma8451.PL_PUF:
        print('Portrait, up, front')
    elif orientation == adafruit_mma8451.PL_PUB:
        print('Portrait, up, back')
    elif orientation == adafruit_mma8451.PL_PDF:
        print('Portrait, down, front')
    elif orientation == adafruit_mma8451.PL_PDB:
        print('Portrait, down, back')
    elif orientation == adafruit_mma8451.PL_LRF:
        print('Landscape, right, front')
    elif orientation == adafruit_mma8451.PL_LRB:
        print('Landscape, right, back')
    elif orientation == adafruit_mma8451.PL_LLF:
        print('Landscape, left, front')
    elif orientation == adafruit_mma8451.PL_LLB:
        print('Landscape, left, back')
    time.sleep(1.0)
