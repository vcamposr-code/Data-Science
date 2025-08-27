"""
Ejercicio-Fundamentos de Data Science.
"""

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 5.5, 7.0]},
    {"nombre": "Luis", "notas": [4.1, 5.1, 6.0]},
    {"nombre": "Sofia", "notas": [4.0, 2.9, 4.5]},
]

# 1. Calcular el promedio de notas de cada estudiante
promedios = []
print("\n1:Promedio de los estudiantes y promedios mas altos y bajos\n")
for estudiante in estudiantes:
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
    estudiante["promedio"] = promedio
    promedios.append(promedio)
    print(f"-El promedio de {estudiante['nombre']} es {promedio:.1f}")

# Encontrar el mayor y menor promedio
mayor = max(estudiantes, key=lambda x: x["promedio"])
menor = min(estudiantes, key=lambda x: x["promedio"])

# Mostrar resultados
print(f"-Mayor promedio: {mayor['nombre']} con {mayor['promedio']:.1f}")
print(f"-Menor promedio: {menor['nombre']} con {menor['promedio']:.1f}")

# 2.Cuantos estudiantes aprobaron todas las asignaturas(nota>=4.0)
aprobados = 0
for estudiante in estudiantes:
    if all(nota >= 4.0 for nota in estudiante["notas"]):
        aprobados += 1
print("\n2:Cantidad de estudaintes que aprobaron todas las asignaturas\n")
print(f"-Cantidad de estudiantes que aprobaron todas las asignaturas: {aprobados}")

# 3. Encontrar la moda para las notas de los estudiantes
valores_nota = []
for estudiante in estudiantes:
    valores_nota.extend(
        estudiante["notas"]
    )  # Agregamos todas las notas en una sola lista

moda = max(set(valores_nota), key=valores_nota.count)

print("\n3:Moda de las notas\n")
print(f"-La moda para las notas es: {moda}")

# 4. Calcular el porcentaje de estudiantes con al menos una baja nota (nota < 4.0)
umbral_baja_nota = 4.0
bajas = sum(
    1
    for estudiante in estudiantes
    if any(nota < umbral_baja_nota for nota in estudiante["notas"])
)
porcentaje_bajas = (bajas / len(estudiantes)) * 100
print("\n4:Porcentaje de estudiantes con nota (bajo 4.0)\n")
print(f"-El {porcentaje_bajas:.1f}% de los estudiantes tienen al menos una baja nota.")

# 5. Ordenar lista según el mayor promedio
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["promedio"], reverse=True)

print("\n5:Lista de estudiantes ordenada por mayor promedio\n")
for estudiante in estudiantes_ordenados:
    print(f"Nombre: {estudiante['nombre']}, Promedio: {estudiante['promedio']:.1f}")
