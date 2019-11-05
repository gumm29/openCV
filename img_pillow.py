from PIL import Image, ImageFilter

im = Image.open('imagem.jpg')
im.show()
im_filter = im.filter(ImageFilter.SHARPEN)
im_filter.save('teste_img_1.jpg', 'JPEG')
r,g,b = im_filter.split()
exif_data = im._getexif()
exif_data