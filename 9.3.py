from PIL import Image, ImageFilter
import os

output_folder = "filtered_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Создана папка: {output_folder}")

files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

my_filter = ImageFilter.FIND_EDGES

print("Начинаем обработку изображений...")
print("-" * 30)

for file_name in files:
    try:
        img = Image.open(file_name)
        
        img_filtered = img.filter(my_filter)
        
        name_without_ext = file_name.split(".")[0]
        new_name = f"{name_without_ext}_filtered.jpg"
        
        save_path = os.path.join(output_folder, new_name)
        
        img_filtered.save(save_path)
        
        print(f"✓ {file_name} -> {new_name}")
        
    except FileNotFoundError:
        print(f"✗ Файл {file_name} не найден! Пропускаем...")
    except Exception as e:
        print(f"✗ Ошибка при обработке {file_name}: {e}")

print("-" * 30)
print(f"Готово! Все изображения сохранены в папку '{output_folder}'")