from PIL import Image, ImageDraw

# create a new image
image = Image.new('RGB', (1000, 600), (230, 230, 230))

# draw shapes
draw = ImageDraw.Draw(image)
draw.rectangle(xy =((0, 0),(100, 200)), 
               fill = (200, 0, 0 ), 
               outline = (0, 20, 20), 
               width = 20)
draw.ellipse(
    xy = (100, 200, 120, 220),
    fill = (132, 200, 115)
)
# exercise
draw.line(
    xy = (140, 170, 180, 100, 300, 225),
    fill = (24, 45, 237),
    width = 10
)

image.show()