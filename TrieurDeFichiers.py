import pathlib
import time

suffix_dictionnary = {
    "Musique": [".mp3", ".wav", ".flac"],
    "Videos": [".avi", ".mp4", ".gif"],
    "Images": [".bmp", ".png", ".jpg"],
    "Documents": [".txt", ".pptx", ".csv", ".xls", ".odp", ".pages"]
}

base_dossier = pathlib.Path(r"C:\Users\jolan\Documents\ExercicesDocString\Data")

def move_element(element, dir_name):
    target_dir = base_dossier / dir_name
    target_dir.mkdir(exist_ok=True)  # Crée le dossier s'il n'existe pas

    new_element = target_dir / element.name

    if new_element.exists():
        stem, suffix = new_element.stem, new_element.suffix
        counter = 1
        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_element = target_dir / new_name
            if not new_element.exists():
                break
            counter += 1

    element.rename(new_element)
    print(f"Fichier déplacé vers : {new_element}")
    
while True:
    for cle, value in suffix_dictionnary.items():
        for child in base_dossier.iterdir():
            if value.__contains__(child.suffix):
                print(f"{child.name} peut bouger vers le dossier {cle}")
                move_element(child, cle)
    time.sleep(10)