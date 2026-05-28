from PIL import Image
file_name = "me4real.jpg"  
img = Image.open(file_name)


width, height = img.size

new_width = width // 3
new_height = height // 3

img_small = img.resize((new_width, new_height))


img_small.save("me4real_small.jpg")
print(f"Уменьшенное изображение сохранено: {new_width} x {new_height} пикселей")

img_mirror_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)

img_mirror_horizontal.save("me4real_mirror_horizontal.jpg")
print("Горизонтальный зеркальный образ сохранён")


img_mirror_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)

# Сохраняем
img_mirror_vertical.save("me4real_mirror_vertical.jpg")
print("Вертикальный зеркальный образ сохранён")

print("Готово! Все изображения сохранены в текущей папке.")