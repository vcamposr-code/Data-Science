
estudiantes = {
    "miguel": [3.5, 4.0, 4.1, 3.9],
    "lucia": [5.1, 5.0, 5.3, 5.0],   
    "javier": [3.7, 4.0, 3.9, 3.9],
    "camila": [4.2, 4.0, 4.3, 4.2],
    "diego": [3.8, 4.0, 3.9, 3.9],
    "valeria": [5.1, 5.1, 5.0, 5.2], 
    "ricardo": [3.5, 3.6, 3.4, 3.4],
    "andrea": [3.9, 3.8, 3.9, 4.0],
    "marco": [4.1, 4.2, 4.3, 4.3],
    "beatriz": [4.5, 4.6, 4.6, 4.6],
    "fernando": [4.8, 4.7, 4.8, 4.8],
    "elena": [5.0, 4.9, 5.0, 5.0],
    "tomás": [3.9, 3.8, 3.8, 3.8],
    "gabriela": [4.6, 4.7, 4.6, 4.6],
    "roberto": [3.8, 3.9, 3.7, 3.8],
    "isabel": [5.1, 5.0, 5.2, 5.1], 
    "julio": [3.7, 3.8, 3.7, 3.7],
    "karla": [3.9, 3.8, 3.7, 3.8],
    "monica": [4.8, 4.9, 4.8, 4.7],
    "nicolas": [4.0, 4.1, 4.0, 3.9],
    "olivia": [5.1, 5.0, 5.2, 5.1], 
    "pablo": [3.7, 3.6, 3.8, 3.7]
}

# 1) Calcular promedios
promedios = {}
for estudiante, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    promedios[estudiante] = round(promedio, 2)

print("1) Promedios de estudiantes:")
for e, p in promedios.items():
    print(f"{e}: {p}")

# 2) Mayor y menor promedio 
max_promedio = max(promedios.values())
min_promedio = min(promedios.values())

mejores = [e for e, p in promedios.items() if p == max_promedio]
peores = [e for e, p in promedios.items() if p == min_promedio]

print("\nMayor promedio:", ", ".join(mejores), f"con {max_promedio}")
print("Menor promedio:", ", ".join(peores), f"con {min_promedio}")

# 3) Estudiantes que aprobaron todas las asignaturas
aprobados = [e for e, notas in estudiantes.items() if all(n >= 4.0 for n in notas)]
print("\n2) Estudiantes que aprobaron todas las asignaturas:", ", ".join(aprobados))

# 4) Nota más frecuente
todas_notas = []
for notas in estudiantes.values():
    todas_notas.extend(notas)

frecuencias = {}
for nota in todas_notas:
    frecuencias[nota] = frecuencias.get(nota, 0) + 1

max_frec = max(frecuencias.values())
modas = [str(n) for n, f in frecuencias.items() if f == max_frec]
print(f"3) Notas más frecuentes: [{', '.join(modas)}] (aparecen {max_frec} veces)")

# 5) Porcentaje de estudiantes con al menos una nota < 4
con_reprobadas = [e for e, notas in estudiantes.items() if any(n < 4.0 for n in notas)]
porcentaje = (len(con_reprobadas) / len(estudiantes)) * 100
print(f"4) {porcentaje:.2f}% de estudiantes tiene al menos una nota bajo 4.0")

# 6) Estudiantes ordenados por promedio
ordenados = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
print("5) Estudiantes ordenados por promedio:")
for e, p in ordenados:
    print(f"{e}: {p}")
