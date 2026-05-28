from PIL import Image
import os

#для одной картинки
print("1. Добавляем водяной знак на одно изображение")
img = Image.open("me4real.jpg")
wm = Image.open("watermark.png")


position = (img.width - wm.width, img.height - wm.height)
img.paste(wm, position, wm)  
img.save("watermark_me4real.jpg")
print("   Сохранено: watermark_me4real.jpg")

#для нескольких картинок
#print("\n2. Добавляем водяной знак на все изображения 1.jpg - 5.jpg")

#os.makedirs("watermarked", exist_ok=True)


#files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
#wm = Image.open("watermark.png")  

#for name in files:
 #   try:
  #      img = Image.open(name)
   #     img.paste(wm, (img.width - wm.width, img.height - wm.height), wm)
        
    #    new_name = f"watermarked/{name}"
     #   img.save(new_name)
      #  print(f"   ✓ {name} -> {new_name}")
        
    #except FileNotFoundError:
     #   print(f"   ✗ Файл {name} не найден!")

#print("\nГотово!")