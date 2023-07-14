from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/edit'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)

    fact = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(fact)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{clean_name}_edited.png')