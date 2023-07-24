import os

def generate_image_tags(directory):
    image_tags = ''
    inc = 0
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_name, file_ext = os.path.splitext(filename)
            source = "../shooting/" + directory_name + "/" + filename
            image_tags += f'<img src="{source}" alt="{file_name}" class="card" id="{inc}_{directory_name}">\n'
            inc = inc + 1
    return image_tags

# Remplacez le chemin du dossier ci-dessous par le dossier souhaité
directory_path = '../shooting/Arianne'
directory_name = 'louison'  # Remplacez par le nom du dossier

image_tags = generate_image_tags(directory_path)
print(image_tags)
