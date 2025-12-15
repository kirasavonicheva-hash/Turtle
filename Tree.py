from turtle import *
from colorsys import *
import time
INITIAL_LENGTH = 120
ANGLE = 25
SCALE_FACTOR = 0.75
MIN_LENGTH = 5
SPEED = 10
name = 'main'
def setup_turtle():
    """Initialize turtle settings"""
    tracer(SPEED)
    bgcolor('black')
    left(90)
    up()
    goto(0, -200)
    down()
def calculate_color(length, initial_length):
    """Calculate color based on branch length"""
    h = 0.3 - (length / initial_length) * 3.0
    h = max(0, min(h, 1))
    return hsv_to_rgb(h, 1, 1)
def draw_tree(length, initial_length):
    """Recursively draw a fractal tree"""
    if length < MIN_LENGTH:
        return
    color(calculate_color(length, initial_length))
    pensize(max(1, length / 20))
    forward(length)
    right(ANGLE)
    draw_tree(length * SCALE_FACTOR, initial_length)
    left(ANGLE * 2)
    draw_tree(length * SCALE_FACTOR, initial_length)
    right(ANGLE)
    backward(length)
def main():
    """Main function to run the program"""
    setup_turtle()
    start_time = time.time()
    draw_tree(INITIAL_LENGTH, INITIAL_LENGTH)
    print(f"Tree drawn in {time.time() - start_time:.2f} seconds")
    hideturtle()
    done()
if name == "main":
    main()