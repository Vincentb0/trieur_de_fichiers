from pathlib import Path

p = Path(r"C:\Users\vboth\Downloads")  # !!! chemin à changer

def creation_repertoire(repertoire = ""):
    nouveau_repertoire = p / repertoire
    nouveau_repertoire.mkdir(exist_ok=True)
    return nouveau_repertoire

def deplacer_fichier(rep):
    if fichier.is_file():
        try:
            fichier.rename(rep / fichier.name)
        except:
            print("Certains fichier n'ont pu être déplacé car ils existent déja")


for fichier in p.iterdir():
    match fichier.suffix:
        case ".txt" | ".pdf" | ".xls" | ".xlsx" | ".odp" | ".docx" | ".pptx" | ".cvs":
            documents = creation_repertoire("Documents")
            deplacer_fichier(documents)
        case ".mp3" | ".wav" | ".flac":
            musique = creation_repertoire("Musiques")
            deplacer_fichier(musique)
        case ".avi" | ".mp4" | ".gif":
            video = creation_repertoire("Vidéos")
            deplacer_fichier(video)
        case ".bmp" | ".png" | ".jpg":
            image = creation_repertoire("Images")
            deplacer_fichier(image)
        case _:
            divers = creation_repertoire("Divers")
            deplacer_fichier(divers)
