from PIL import Image, ImageFilter

img = Image.open('astro.jpg')
# Keeps aspect ratio as close to specified size
img.thumbnail((400, 200))
img.save('thumbnail.jpg')
print(img.size)
