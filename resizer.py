from PIL import Image


im = Image.open("foster-lake.jpg") #enter a img
out = im.resize((128, 128))
out.save("128.png")


