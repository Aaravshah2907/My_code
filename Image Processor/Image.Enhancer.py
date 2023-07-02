from PIL import Image, ImageEnhance, ImageFilter
import os

path = r"I:\Others\Img_Recreation\Img"  # folder for unedited images
path_exist = os.path.exists(path)


def img_enhancer():
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        # sharpening, BW
        edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)

        # contrast
        factor = 2
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/

        clean_name = os.path.splitext(filename)[0]

        edit.save(f'{path}/{clean_name}_edited.jpg')


if path_exist:
    pass
else:
    os.mkdir(path)
    
img_enhancer()
print(path_exist)
