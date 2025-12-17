import requests

# Remplacez par votre lien .ics.phps
url = "https://utils.bde-insa-lyon.fr/cal/get.php?url=https://ade-outils.insa-lyon.fr/ADE-Cal:~rgirard!2025-2026:e7463c202c6a0d6238442e875fda974f50722eeb&mode=1&desc=true&count=true&types=lang,sport,huma,support,p2i,other,*&ctypes=*,td,cm,tp,ev,soutien"
filename = "calendrier.ics"

try:
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print("Fichier mis à jour avec succès.")
    else:
        print(f"Erreur lors du téléchargement : {response.status_code}")
except Exception as e:
    print(f"Erreur : {e}")
