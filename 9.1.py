from PIL import Image

file_name = "me4real.jpg"  

img = Image.open(file_name)

img.show()

width, height = img.size

img_format = img.format

color_mode = img.mode

print("Информация об изображении:")
print(f"Размер: {width} x {height} пикселей")
print(f"Формат: {img_format}")
print(f"Цветовая модель: {color_mode}")