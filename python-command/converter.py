import os
import sys
from PIL import Image

def compress_images(directory, quality=85):
    """
    Compresse toutes les images d'un dossier.

    :param directory: Dossier contenant les images à compresser.
    :param output_directory: Dossier où stocker les images compressées.
    :param quality: Qualité de la compression (1-95).
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(directory, filename)
            try:
                image = Image.open(file_path)
            except Exception as e:
                print(f"Impossible d'ouvrir l'image {filename}. Erreur: {str(e)}")
                continue

            # Modifier la qualité de l'image
            output_file_path = os.path.join(directory, filename)
            image.save(output_file_path, quality=quality, optimize=True)

            print(f"Image {filename} compressée avec succès.")
        else:
            print(f"{filename} n'est pas une image .jpg, .jpeg ou .png, elle n'a donc pas été compressée.")



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python compress_images.py <directory> <quality>")
        sys.exit(1)

    directory = sys.argv[1]

    try:
        quality = int(sys.argv[2])
    except ValueError:
        print("Quality should be an integer between 1 and 95")
        sys.exit(1)
    
    compress_images(directory, quality)

