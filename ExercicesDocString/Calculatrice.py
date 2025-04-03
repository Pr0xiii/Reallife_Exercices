first_number = input("Entrez un premier nombre : ")
second_number = input("Entrez un deuxieme nombre : ")

if first_number.isdigit() and second_number.isdigit():
    result = f"Le résultat de l'addition de {first_number} avec {second_number} est égal à {int(first_number) + int(second_number)}"
else:
    result = "Veuillez entrer deux nombres valides"
    
print(result)