from PIL import Image, ImageFilter

img = Image.open('image-playground/charmander.jpg')
filtered_img = img.convert('L')
filtered_img.save("grayCharmander.png", 'png')
