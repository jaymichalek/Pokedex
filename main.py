from PIL import Image, ImageFilter

img = Image.open('image-playground/charmander.jpg')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(180)
crooked.save("grayCharmander.png", 'png')
# filtered_img.show()
