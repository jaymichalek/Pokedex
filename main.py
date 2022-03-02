from PIL import Image, ImageFilter

img = Image.open('image-playground/charmander.jpg')
filtered_img = img.convert('L')
resize = filtered_img.resize((300, 300))
resize.save("grayCharmander.png", 'png')
# filtered_img.show()
