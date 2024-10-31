print (" ")
print("Ordonez Martinez Valeria")
print (" ")

# Almacenar las asignaturas en una lista
asignaturas = ["matematicas", "español", "quimica", "historia"]
print("Las materias son:", asignaturas)
print(" ")

# Poner las calificaciones
notas = []
for x in asignaturas:
    calif = int(input(f"Cuál es tu calificación en {x} "))
    notas.append(calif)
    

# Mostrar las notas
print(" ")
print("Tus calificaciones son:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
print(" ")