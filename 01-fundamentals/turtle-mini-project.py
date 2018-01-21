import turtle
import colorsys


def spiral_into_the_grid():
    """Use turtle graphics to create a colorful spiral."""
    turtle.setup(width=1600, height=900)
    turtle.speed(0)
    turtle.hideturtle()
    window = turtle.Screen()
    window.bgpic('img/TRON.gif')

    for i in range(1250):
        colors = colorsys.hsv_to_rgb(i / 1250, 1.0, 1.0)
        turtle.color(colors)
        turtle.forward(i)
        turtle.left(115)

    turtle.done()


spiral_into_the_grid()
