import random
from PIL import Image
from StringIO import StringIO
random_string = ''
random_string = 'FFFF18'
hex_string = 'ABCDEF1234567890'
im = Image.new("RGBA", (1920, 1080), "white")
pix = im.load()
for x in range(0,1920):
	for y in range(0,1080):
		pix[x,y] = (random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)),255)
im.save("random.png")