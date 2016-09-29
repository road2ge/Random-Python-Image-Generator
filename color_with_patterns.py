import random
from PIL import Image
im = Image.new("RGBA", (1920, 1080), "white")
pix = im.load()
for x1 in range(1,11):
    random_color = (random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)),255)
    for x in range((192*x1-1),(192*x1)):
        for y in range(0,1080):
            pix[x,y] = random_color
im.save("random_pattern.png")