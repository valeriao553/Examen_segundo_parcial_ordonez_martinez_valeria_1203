print (" ")
print("Ordonez Martinez Valeria")
print (" ")

# Almacenar las asignaturas en una lista
asignaturas = ["matematicas", "español", "quimica", "historia"]
print("Las materias son:", asignaturas)
print(" ")

# Poner las calificaciones de todas las materias
calificaciones = []
for x in asignaturas:
    calif = int(input(f"Cual es tu calificacion es {x} "))
    print(" ")
    calificaciones.append(calif)

# Ver cuales son las materias aprobadas y las reprobadas
reprobadas = [asignaturas[i] for i in range(len(calificaciones)) if calificaciones[i] < 6]
aprobadas = [asignaturas[i] for i in range(len(calificaciones)) if calificaciones[i] >= 6]

# Mostrar resultados
if reprobadas:
    print(" ")
    print("Las materias reprobadas son:", reprobadas)
    print(" ")
else:
    print("No reprobaste ninguna materia.")
    print(" ")




