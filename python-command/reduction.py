import os
from PIL import Image

def resize_images_in_directory(directory_path, reduction_factor):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(root, file)
                resize_image(file_path, reduction_factor)

def resize_image(image_path, reduction_factor):
    try:
        img = Image.open(image_path)
        new_width = img.width // reduction_factor
        new_height = img.height // reduction_factor
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image_path)
        print(f"Image {image_path} resized successfully.")
    except Exception as e:
        print(f"Error resizing image {image_path}: {e}")

if __name__ == "__main__":
    directory_path = "./shooting/arianne"  # Remplacez par le chemin du dossier contenant les images
    reduction_factor = 5  # Facteur de réduction souhaité (par exemple, 5 pour diviser la taille par 5)
    resize_images_in_directory(directory_path, reduction_factor)
