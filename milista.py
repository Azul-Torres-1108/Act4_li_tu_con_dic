# Ejemplo de manejo de listas
Misnovios= ["Oebs49", "ivan", "Edson"]
MisNumeros= [555, 666, 777]
# Mostrando a mis novios 
print(Misnovios)
# Mostrando a mis numeros raros
print(MisNumeros)
print("----------------------------accediendo a los elementos de la lista--------------------------------")
print(Misnovios[-2])
if "Oebs499" in Misnovios:
    print("Si, Oebs49 esta en la lista de mis novios")
else:
    print("Chale no eres mi novio")

print("Numero de novioss")
Nnovios=len(Misnovios)
print(f"Numero de novios = {Nnovios}")
print("MI media naranja: ")
print("Ciclo for en listas")
posicion=0
for medianajaranja in Misnovios:
    print(medianajaranja)
    posicion+=1