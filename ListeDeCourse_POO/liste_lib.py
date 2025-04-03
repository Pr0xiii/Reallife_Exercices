import json

class Liste(list):
    def __init__(self, liste_name):
        self.liste_name = liste_name

    def ajouter(self, element):
        if not isinstance(element, str):
            print("Veuillez rentrer une chaine de caractère")

        if not element in self:
            self.append(element)
        else:
            print("Element déjà dans la liste")
    
    def retirer(self, element):
        if not isinstance(element, str):
            print("Veuillez rentrer une chaine de caractère")

        if element in self:
            self.remove(element)
        else:
            print("L'élément que vous essayer de retirer ne se trouve pas dans la liste")

    def sauvegarder(self):
        json_name = f"{self.liste_name}.json"
        with open(json_name, "w") as f:
            json.dump(self, f, indent=4)

    def afficher(self):
        for index, nom in enumerate(self):
            print(f"{index + 1}: {nom}")

if __name__ == "__main__":
    liste_course = Liste("Courses")
    liste_course.ajouter("Pommes")
    liste_course.ajouter("Poires")
    liste_course.ajouter("Melon")
    liste_course.ajouter("Pommes")
    liste_course.afficher()
    liste_course.sauvegarder()

    liste_todo = Liste("TODO")
    liste_todo.ajouter("Ecole")
    liste_todo.ajouter("Primaire")
    liste_todo.ajouter("Jsp")
    liste_todo.ajouter("Letsgo")
    liste_todo.afficher()
    liste_todo.sauvegarder()
    