import fitz
import PIL.Image
import io
import os

pdf = fitz.open('C:/Users/Михаил/PycharmProjects/Script_Image/doc/TEST.pdf')
folder = 'C:/Users/Михаил/PycharmProjects/Script_Image/image'
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img['image']
        img = PIL.Image.open(io.BytesIO(image_data))
        extensions = base_img['ext']
        image_path = os.path.join(folder, f'image{counter}.{extensions}')
        img.save(image_path)

        counter += 1
