from PIL import Image, ImageDraw, ImageFont
from os.path import join

# create a new image
image = Image.new('RGB', (1920, 1080), (240, 240, 240))

# create a font
font = ImageFont.truetype(
    font = join('resources', 'RabbidHighway.otf'),
    size = 25)

# drawable object
draw = ImageDraw.Draw(image)

# draw text 
draw.text(
    xy = (1920/2,1080/2), # center of screen
    text = 'Test',
    fill = (0,0,0),
    font = font,
    stroke_width = 2,
    stroke_fill = (255,0,0),
    anchor = 'mm'
)
# show image
image.show()