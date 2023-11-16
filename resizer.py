from PIL import Image


im = Image.open("default.png") #enter a img
out = im.resize((128, 128))
out.save("icon-128x128.png")


