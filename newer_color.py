import random
from PIL import Image
im = Image.new("RGBA", (1920, 1080), "white")
pix = im.load()
for x in range(0,1920):
	for y in range(0,1080):
		pix[x,y] = (random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)),255)
im.save("random.png")