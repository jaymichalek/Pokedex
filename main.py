from PIL import Image, ImageFilter

img = Image.open('image-playground/charmander.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grayCharmander.png", 'png')
# filtered_img.show()
