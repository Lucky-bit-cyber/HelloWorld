from PIL import Image, ImageDraw

img = Image.new('RGB', (320, 240),color=(255,255,255))
pixels = img.load()
fill = ImageDraw.Draw(img)
pixels[160, 120] = (255, 255, 255)  # middle of the plane also the circle


# using straight line to fill the circle
def fillCircle(x_centre, y_centre, r):
    # first Point
    x = 0
    y = r

    # first midpoint is (1,r-0.5)
    d = 4 / 5 - r

    # the pixels in the center point
    pixels[x + x_centre, y - y_centre] = (255, 0, 0)

    # draw a line from (-r,0) to (r,0)
    fill.line((x_centre - y, y_centre, x_centre + y, y_centre), (255, 0, 0))

    # when x == y, get 1/8 circle
    while x < y:
        x += 1
        if d <= 0:  # choose upper pixel
            d += 2 * x + 3
        else:  # choose lower pixel
            y -= 1
            d += 2 * x - 2 * y - 5

        # there are four different sections within the circle needed to fill.
        fill.line((x_centre - x, y_centre + y, x_centre + x, y_centre + y),(255, 0, 0))
        fill.line((x_centre - x, y_centre - y, x_centre + x, y_centre - y),(255, 0, 0))
        fill.line((x_centre - y, y_centre + x, x_centre + y, y_centre + x),(255, 0, 0))
        fill.line((x_centre - y, y_centre - x, x_centre + y, y_centre - x),(255, 0, 0))
        # print(x+x_centre,y-y_centre)


def midPointCircleDraw(x_centre, y_centre, r, color=(255, 0, 255)):
    # first Point
    x = 0
    y = r

    # first midpoint is (1,r-0.5)
    d = 4 / 5 - r

    # the pixels in the center point
    pixels[x + x_centre, y - y_centre] = color

    # when x == y, get 1/8 circle
    while x < y:
        x += 1
        if d <= 0:  # choose upper pixel
            d += 2 * x + 3
        else:  # choose lower pixel
            y -= 1
            d += 2 * x - 2 * y - 5

        # 1/8 circle for per "pixels" method
        pixels[x + x_centre, y - y_centre] = color
        pixels[x + x_centre, -y - y_centre] = color
        pixels[-x + x_centre, y - y_centre] = color
        pixels[-x + x_centre, -y - y_centre] = color

        pixels[y - x_centre, x + y_centre] = color
        pixels[-y - x_centre, x + y_centre] = color
        pixels[y - x_centre, -x + y_centre] = color
        pixels[-y - x_centre, -x + y_centre] = color

        # print(x+x_centre,y-y_centre)


x_center = 160
y_center = 120
radius = 100

# draw the circle
midPointCircleDraw(x_center, y_center, radius,color = (255,0,0))

# fill the circle
fillCircle(x_center, y_center, radius)

# creating anti-aliasing on the circle
color = [i for i in range(0,150,15)]
distant = [i for i in range(20)]
for i in range(len(color)):
    midPointCircleDraw(x_center, y_center, radius+(i/10),color=(255,color[i],color[i]))



img.show()
